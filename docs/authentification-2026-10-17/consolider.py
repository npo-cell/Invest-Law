#!/usr/bin/env python3
"""Consolide l'authentification : passage automatique + relecture humaine (relecture/lot-*-verdicts.json)
+ second contrôle dans le KID (fundinfo) pour les fiches du site, + fraîcheur des documents (fundinfo).
Usage : python3 -I consolider.py <res1.json> <dossier KID> <fundinfo.json> <sortie.json>
"""
import glob, json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import authentifier as au

ICI = os.path.dirname(os.path.abspath(__file__))
AUTRE_PART = {  # factsheet utilisée = celle d'une autre part (relecture)
    'LU2389405163': 'factsheet de la part A EUR (LU2389405080)',
    'LU2381585830': 'factsheet de la classe C1 (LU2381586309)',
    'BE6370437590': 'factsheet de la classe R (BE6370436584)',
    'BE6327306930': 'factsheet de la classe R (BE6269807184)',
    'BE6327307946': 'factsheet de la classe R (BE6304593781)',
    'DE000A1JCWX9': 'factsheet de la part R (le classeur vise la part UI)',
    'LU0757431068': 'factsheet de la catégorie AE (le classeur vise AU)',
    'FR0007072160': 'factsheet de la part R (le classeur vise la part A)',
    'LU0558384706': 'factsheet des parts C1, P, I1 (pas C3)',
    'LU0366797354': 'factsheet des parts C1, P, I1 (pas C3)',
    'LU3149167358': 'factsheet de la part S-H (LU1670714226)',
    'FR0013393345': 'factsheet de la part R EUR (FR0013393329)',
    'FR0011978238': 'factsheet de la part R EUR (FR0010923383)',
    'IE00BD4LCP84': 'factsheet de la part USD-I',
}
RENOMME = {  # même ISIN, fonds renommé : pas une erreur
    'FR0013202140': 'fonds renommé : le KID s’intitule « Sextant Credit Opportunities Action N » (One Life : Sextant Bond Picking)',
    'LU0935228691': 'fonds renommé : le document s’intitule « Ostrum All Roads Macro Allocation » (One Life : Seeyond Multi Asset Conservative Growth)',
}
KID_WORDS = ('informations clés', 'key information document', 'document d’informations clés',
             "document d'informations clés", 'basisinformationsblatt')


def kid_match(k, v, raw):
    R = au.norm(raw)
    if k in ('date_creation', 'encours_date'):
        return au.trouve_date(v, raw)
    if k in ('devise', 'encours_devise'):
        return bool(re.search(r'\b' + re.escape(v) + r'\b', raw))
    if k in ('encours', 'frais_gestion', 'frais_courants', 'durable_pct'):
        return au.trouve_nombre(v, R, raw)
    if k == 'duration':
        m = re.match(r'-?[\d.,]+', v)
        return bool(m and au.trouve_nombre(m.group().replace(',', '.'), R, raw))
    if k == 'sri':
        return au.trouve_sri(v, raw)
    if k == 'sfdr':
        return bool(re.search(r'(article|art\.?)\s*' + v + r'\b', raw, re.I))
    if k == 'gerants':
        return all(au.norm(g.split()[-1]) in R for g in re.split(r',|;| et | and ', v) if g.strip())
    if k in ('compartiment', 'indice', 'disclaimer', 'politique_fr', 'politique_en', 'qualite'):
        p, _ = au.part_trouvee(v, R)
        return p >= 0.9
    return False


def main(res1, kiddir, fundinfo, sortie):
    R = json.load(open(res1))
    V = {}
    for f in glob.glob(os.path.join(ICI, 'relecture', 'lot-*-verdicts.json')):
        for e in json.load(open(f)):
            V[e['isin']] = e
    V2 = {}  # relecture du 19/10 après correction (prioritaire)
    for f in glob.glob(os.path.join(ICI, 'relecture2', 'lot-*-verdicts.json')):
        for e in json.load(open(f)):
            V2[e['isin']] = e
    OLD = {}  # valeurs relues le 17/10 : un ancien verdict ne vaut que si la valeur n'a pas changé
    if os.environ.get('OLD_RES1'):
        OLD = {(r['isin'], k): x['v'] for r in json.load(open(os.environ['OLD_RES1'])) for k, x in r['cells'].items()}
    FI = json.load(open(fundinfo))
    kids = {os.path.basename(p).split('__')[0]: p for p in glob.glob(os.path.join(kiddir, '*.pdf'))}
    out = []
    for r in R:
        isin = r['isin']
        v = V.get(isin, {})
        v2 = V2.get(isin, {})
        corrige = r['origine'].startswith('Corrigée')
        kidtxt = au.texte(kids[isin]) if isin in kids else ''
        cells = {}
        for k, x in r['cells'].items():
            st, note, vdoc = x['st'], x.get('det', ''), ''
            if st == 'OK':
                st, note = 'CONFORME', 'retrouvé automatiquement dans le document'
            elif st == 'NON_RETROUVE':
                h = v2.get('cases', {}).get(k) or (v.get('cases', {}).get(k, {}) if not OLD or OLD.get((isin, k)) == x['v'] else {})
                st, note, vdoc = h.get('verdict', 'ABSENT'), h.get('note', ''), h.get('valeur_document', '')
            if st in ('ABSENT', 'DIFFERENT', 'SANS_SOURCE') and kidtxt and kid_match(k, x['v'], kidtxt):
                st, note = 'CONFORME', 'retrouvé dans le KID (fundinfo, %s)' % os.path.basename(kids[isin])
            if st == 'SANS_SOURCE':
                st, note = 'ABSENT', 'aucun document pour ce fonds'
            cells[k] = {'v': x['v'], 'st': st, 'note': note, 'vdoc': vdoc}
        al = v2.get('allocations') or (None if corrige else v.get('allocations'))
        if r['alloc_total'] == 0:
            alloc = None
        elif not r['alloc_bad']:
            alloc = {'st': 'CONFORME', 'note': 'toutes les lignes retrouvées automatiquement'}
        else:
            alloc = {'st': al.get('verdict', 'ABSENT'), 'note': al.get('note', '')} if al else {'st': 'ABSENT', 'note': ''}
        # fraîcheur
        fi = FI.get(isin, {'MR': {}, 'KID': {}})
        mr_fr = fi['MR'].get('FR', {}).get('Date', '')
        mr_en = fi['MR'].get('EN', {}).get('Date', '')
        fresh = ''
        if r['fs_date']:
            best = mr_fr or mr_en
            if best and best > r['fs_date']:
                fresh = 'Factsheet plus récente sur fundinfo : %s (%s)' % (best, 'FR' if mr_fr else 'EN')
        elif mr_fr or mr_en:
            fresh = 'Aucune factsheet dans le classeur, mais fundinfo en publie une (%s)' % (mr_fr or mr_en)
        doc_kid = not corrige and bool(r['sources']) and r['sources'][0].endswith('__site.pdf') and \
            any(w in au.texte(os.path.join(os.path.dirname(kiddir), 'pdf', r['sources'][0]))[:3000].lower() for w in KID_WORDS)
        out.append({'n': r['n'], 'isin': isin, 'nom': r['nom'], 'statut': r['statut'], 'origine': r['origine'],
                    'fs_date': r['fs_date'], 'kid_date': r['kid_date'], 'cells': cells, 'alloc': alloc,
                    'alloc_total': r['alloc_total'], 'fraicheur': fresh, 'autre_part': '' if corrige else AUTRE_PART.get(isin, ''), 'renomme': RENOMME.get(isin, ''),
                    'doc_site_est_kid': doc_kid, 'kid_fundinfo': os.path.basename(kids[isin]) if isin in kids else ''})
    json.dump(out, open(sortie, 'w'), ensure_ascii=False)
    c = collections.Counter(x['st'] for r in out for x in r['cells'].values())
    print('cases', dict(c))
    print('allocations', collections.Counter(r['alloc']['st'] for r in out if r['alloc']))
    print('fraîcheur', sum(1 for r in out if r['fraicheur']), 'autre part', sum(1 for r in out if r['autre_part']),
          'doc site = KID', sum(1 for r in out if r['doc_site_est_kid']))


if __name__ == '__main__':
    main(*sys.argv[1:5])
