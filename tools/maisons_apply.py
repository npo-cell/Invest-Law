#!/usr/bin/env python3
"""Remplit des champs vides de fiches maisons à partir d'un fichier de propositions.
  python3 tools/maisons_apply.py <propositions.json> [--statut pret] [--apply]
Ne touche jamais un champ déjà rempli sur le site ; sans --apply, affiche seulement ancien -> nouveau.
Le PUT /api/maisons/{id} est reconstruit depuis l'état actuel (contacts omis = inchangés)."""
import json, re, sys
from investlaw_upload import api

KEYS = {'Nom': 'name', 'Adresse': 'adresse', 'Slogan': 'slogan', 'Sponsor': 'sponsor', 'Site': 'site', 'FID': 'fid',
        'FondsExternes': 'fonds_externes', 'PointsForts': 'points_forts', 'FID_Specialites': 'fid_specialites',
        'FID_TypeGestion': 'fid_type_gestion', 'FondsExternes_Description': 'fonds_externes_description',
        'FondsExternes_Specialites': 'fonds_externes_specialites',
        'FondsExternes_TypeGestion': 'fonds_externes_type_gestion', 'FID_Seuil': 'fid_seuil', 'Logo': 'logo'}


def empty(v):
    return not (v and re.sub(r'<[^>]+>|&nbsp;|\s', '', str(v)))


def main():
    args = sys.argv[1:]
    apply = '--apply' in args
    statut = args[args.index('--statut') + 1] if '--statut' in args else 'pret'
    props = json.load(open(args[0]))
    st, maisons = api('GET', '/api/maisons')
    if st != 200:
        sys.exit('GET /api/maisons -> %s : relancer investlaw_upload.py login/verify' % st)
    cur = {str(m['MaisonId']): m for m in maisons}
    for mid, p in props.items():
        m = cur[mid]
        body = {KEYS[k]: ('' if m.get(k) is None else m[k]) for k in KEYS}
        changes = []
        for k, c in p['champs'].items():
            if c.get('statut') != statut or not c.get('valeur'):
                continue
            if not empty(m.get(k)):
                print('  %s %s : déjà rempli sur le site, ignoré' % (m['Nom'], k))
                continue
            body[KEYS[k]] = c['valeur']
            changes.append(k)
        if not changes:
            continue
        print('%s (%s)' % (m['Nom'], mid))
        for k in changes:
            print('  %s : %r -> %s' % (k, m.get(k), c_short(body[KEYS[k]])))
        if apply:
            st, r = api('PUT', '/api/maisons/%s' % mid, body)
            print('  PUT ->', st, '' if st == 200 else r)
            if st != 200:
                sys.exit(1)


def c_short(v):
    v = re.sub(r'\s+', ' ', v)
    return v if len(v) <= 90 else v[:87] + '...'


if __name__ == '__main__':
    main()
