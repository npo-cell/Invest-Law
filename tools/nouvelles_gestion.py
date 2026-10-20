"""Régénère docs/nouvelles/gestion.html (page « Gestion des nouvelles ») depuis docs/nouvelles/.

Usage : python3 tools/nouvelles_gestion.py
Articles : articles/*.json ; mails non retenus : ecartes.txt ; date de vérification : etat.json.
Les statuts (à valider, validée, publiée…) ne sont pas dans le dépôt : l'équipe les règle sur la page (base partagée de l'artéfact).
"""
import glob, json, os, datetime

ROOT = os.path.join(os.path.dirname(__file__), '..', 'docs', 'nouvelles')


def main():
    A = [json.load(open(p)) for p in glob.glob(os.path.join(ROOT, 'articles', '*.json'))]
    A.sort(key=lambda a: (a['date_source'], a['thread']), reverse=True)
    E = []
    for l in open(os.path.join(ROOT, 'ecartes.txt')):
        p = [x.strip() for x in l.split(' | ')]
        if len(p) >= 3:
            E.append({'thread': p[0], 'sujet': ' | '.join(p[1:-1]), 'raison': p[-1]})
    etat = json.load(open(os.path.join(ROOT, 'etat.json')))
    maj = datetime.date.fromisoformat(etat['derniere_verification']).strftime('%d/%m/%Y')
    data = json.dumps({'articles': A, 'ecartes': E, 'maj': maj}, ensure_ascii=False).replace('</', '<\\/')
    page = open(os.path.join(os.path.dirname(__file__), 'nouvelles_gestion_modele.html')).read()
    open(os.path.join(ROOT, 'gestion.html'), 'w').write(page.replace('__DATA__', data))
    print(len(A), 'articles,', len(E), 'mails non retenus ; dernière vérification', maj)


if __name__ == '__main__':
    main()
