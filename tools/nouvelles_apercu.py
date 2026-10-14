"""Régénère docs/nouvelles/apercu.html (page « Nouvelles à valider ») depuis docs/nouvelles/articles/*.json.

Usage : python3 tools/nouvelles_apercu.py
Chaque article : {thread, date_source, maison_id, maison, type, titre, html, notes}
"""
import glob, html, json, os, datetime

ROOT = os.path.join(os.path.dirname(__file__), '..', 'docs', 'nouvelles')
TYPES = ['Marchés', 'Fonds', 'Événement', 'Étude']
CLS = {'Marchés': 'mar', 'Fonds': 'fon', 'Événement': 'evt', 'Étude': 'etu'}


def carte(i, a):
    d = a['date_source']
    note = ('<p class="note"><b>À vérifier :</b> %s</p>' % html.escape(a['notes'])) if a.get('notes') else ''
    return ('<article class="card" data-type="%s"><div class="meta"><span class="tag t-%s">%s</span><span>%s</span>'
            '<span class="mono">%s/%s/%s</span><span class="mono">n° %d</span></div><h2>%s</h2><div class="body">%s</div>%s</article>'
            % (html.escape(a['type']), CLS.get(a['type'], 'mar'), html.escape(a['type']), html.escape(a['maison'] or ''),
               d[8:], d[5:7], d[:4], i, html.escape(a['titre']), a['html'], note))


def main():
    A = [json.load(open(p)) for p in glob.glob(os.path.join(ROOT, 'articles', '*.json'))]
    A.sort(key=lambda a: (a['date_source'], a['thread']), reverse=True)
    etat = json.load(open(os.path.join(ROOT, 'etat.json')))
    maj = datetime.date.fromisoformat(etat['derniere_verification']).strftime('%d/%m/%Y')
    cartes = ''.join(carte(i, a) for i, a in enumerate(A, 1))
    page = open(os.path.join(os.path.dirname(__file__), 'nouvelles_apercu_modele.html')).read()
    page = page.replace('__N__', str(len(A))).replace('__MAJ__', maj).replace('__CARTES__', cartes)
    open(os.path.join(ROOT, 'apercu.html'), 'w').write(page)
    print(len(A), 'articles ; dernière vérification', maj)


if __name__ == '__main__':
    main()
