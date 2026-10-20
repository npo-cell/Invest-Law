"""Régénère docs/nouvelles/gestion.html (page « Gestion des nouvelles ») depuis docs/nouvelles/.

Usage : python3 tools/nouvelles_gestion.py
Source des mails : uniquement la boîte data@invest-law.eu (Zimbra) — articles de veille avec "boite" = BOITE ;
les articles « document » et « recherche » sont toujours repris. Mails non retenus : ecartes-data.txt ; date : etat-data.json.
Les articles de l'ancienne veille Gmail (npo@lifeb2b.com) restent dans le dépôt mais ne sont pas affichés (consigne du 20/10/2026).
Les statuts (à valider, validée, publiée…) ne sont pas dans le dépôt : l'équipe les règle sur la page (base partagée de l'artéfact).
"""
import glob, json, os, datetime

ROOT = os.path.join(os.path.dirname(__file__), '..', 'docs', 'nouvelles')
BOITE = 'data@invest-law.eu'


def main():
    A = [json.load(open(p)) for p in glob.glob(os.path.join(ROOT, 'articles', '*.json'))]
    A = [a for a in A if a.get('origine', 'veille') != 'veille' or a.get('boite') == BOITE]
    A.sort(key=lambda a: (a['date_source'], a['thread']), reverse=True)
    E = []
    for l in open(os.path.join(ROOT, 'ecartes-data.txt')):
        p = [x.strip() for x in l.split(' | ')]
        if len(p) >= 3:
            E.append({'thread': p[0], 'sujet': ' | '.join(p[1:-1]), 'raison': p[-1]})
    etat = json.load(open(os.path.join(ROOT, 'etat-data.json')))
    maj = datetime.date.fromisoformat(etat['derniere_verification']).strftime('%d/%m/%Y')
    data = json.dumps({'articles': A, 'ecartes': E, 'maj': maj, 'boite': BOITE}, ensure_ascii=False).replace('</', '<\\/')
    page = open(os.path.join(os.path.dirname(__file__), 'nouvelles_gestion_modele.html')).read()
    open(os.path.join(ROOT, 'gestion.html'), 'w').write(page.replace('__DATA__', data))
    print(len(A), 'articles,', len(E), 'mails non retenus ; dernière vérification', maj)


if __name__ == '__main__':
    main()
