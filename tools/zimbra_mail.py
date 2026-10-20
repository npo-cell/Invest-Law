#!/usr/bin/env python3
"""Lecture seule de la boîte Zimbra d'invest-law (API REST Zimbra, en HTTPS).

L'IMAP (port 993) est bloqué par le proxy des sessions cloud : seul HTTPS (443) passe.
Identifiants lus dans l'environnement : ZIMBRA_USER, ZIMBRA_PASSWORD
(optionnel : ZIMBRA_HOST, défaut zimbra1.mail.ovh.net). Procédure : docs/2026-10-19-guide-zimbra.md.

  python3 tools/zimbra_mail.py test                 # vérifie la connexion
  python3 tools/zimbra_mail.py list [N] [--query "from:leleux after:10/15/2026"]
  python3 tools/zimbra_mail.py get <id> [--save DIR]    # texte + pièces jointes
"""
import base64, email, html, json, os, re, sys, urllib.parse, urllib.request
from datetime import datetime
from email.header import decode_header, make_header

HOST = os.environ.get('ZIMBRA_HOST') or os.environ.get('ZIMBRA_IMAP_HOST') or 'zimbra1.mail.ovh.net'
HOST = urllib.parse.urlsplit(HOST if '//' in HOST else '//' + HOST).hostname  # tolère une URL complète


def rest(path, **params):
    params['auth'] = 'ba'  # authentification Basic
    url = f"https://{HOST}/home/~/{path}?" + urllib.parse.urlencode(params)
    tok = base64.b64encode(f"{os.environ['ZIMBRA_USER']}:{os.environ['ZIMBRA_PASSWORD']}".encode()).decode()
    req = urllib.request.Request(url, headers={'Authorization': 'Basic ' + tok})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def h(v):
    return str(make_header(decode_header(v or '')))


def opt(args, name):
    return args[args.index(name) + 1] if name in args else None


def messages(query=None):
    params = {'fmt': 'json'}
    if query:
        params['query'] = query
    return json.loads(rest('inbox', **params) or b'{}').get('m', [])


def cmd_list(args):
    n = int(args[0]) if args and args[0].isdigit() else 20
    for m in sorted(messages(opt(args, '--query')), key=lambda m: -m['d'])[:n]:
        frm = next((e.get('a') for e in m.get('e', []) if e.get('t') == 'f'), '')
        print(f"{m['id']}\t{datetime.fromtimestamp(m['d'] / 1000):%Y-%m-%d %H:%M}\t{frm}\t{m.get('su', '')}")


def cmd_get(args):
    msg = email.message_from_bytes(rest('', id=args[0]))
    for k in ('From', 'To', 'Date', 'Subject'):
        print(f"{k}: {h(msg[k])}")
    out = opt(args, '--save')
    has_plain = any(p.get_content_type() == 'text/plain' and not p.get_filename() for p in msg.walk())
    for part in msg.walk():
        name = part.get_filename()
        if name:
            name = os.path.basename(h(name))
            if out:
                os.makedirs(out, exist_ok=True)
                with open(os.path.join(out, name), 'wb') as f:
                    f.write(part.get_payload(decode=True))
            print(f"[pièce jointe] {name}" + (f" -> {out}/{name}" if out else ''))
        elif part.get_content_type() == 'text/plain':
            print('\n' + part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', 'replace'))
        elif part.get_content_type() == 'text/html' and not has_plain:  # newsletter sans partie texte
            t = part.get_payload(decode=True).decode(part.get_content_charset() or 'utf-8', 'replace')
            t = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', '', t)
            t = re.sub(r'(?i)<br\s*/?>|</(p|div|tr|li|h\d)>', '\n', t)
            t = html.unescape(re.sub(r'<[^>]+>', '', t))
            print('\n' + re.sub(r'\n\s*\n+', '\n\n', re.sub(r'[ \t\xa0]+', ' ', t)).strip())


if __name__ == '__main__':
    c, rest_args = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ('', [])
    if c == 'test':
        print('Connexion OK,', len(messages()), 'messages lus dans la boîte de réception')
    elif c == 'list':
        cmd_list(rest_args)
    elif c == 'get':
        cmd_get(rest_args)
    else:
        sys.exit(__doc__)
