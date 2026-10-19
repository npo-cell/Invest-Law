#!/usr/bin/env python3
"""Lecture seule de la boîte Zimbra d'invest-law (IMAP).

Identifiants lus dans l'environnement : ZIMBRA_IMAP_HOST, ZIMBRA_USER, ZIMBRA_PASSWORD
(optionnel : ZIMBRA_IMAP_PORT, défaut 993). Procédure : docs/2026-10-19-guide-zimbra.md.

  python3 tools/zimbra_mail.py test                 # vérifie la connexion
  python3 tools/zimbra_mail.py list [N] [--from X] [--since 15-Oct-2026] [--subject Y]
  python3 tools/zimbra_mail.py get <uid> [--save DIR]   # texte + pièces jointes
"""
import email, imaplib, os, sys
from email.header import decode_header, make_header


def connect():
    m = imaplib.IMAP4_SSL(os.environ['ZIMBRA_IMAP_HOST'], int(os.environ.get('ZIMBRA_IMAP_PORT', 993)))
    m.login(os.environ['ZIMBRA_USER'], os.environ['ZIMBRA_PASSWORD'])
    m.select('INBOX', readonly=True)  # lecture seule : ne marque rien comme lu
    return m


def h(v):
    return str(make_header(decode_header(v or '')))


def opt(args, name):
    return args[args.index(name) + 1] if name in args else None


def cmd_list(m, args):
    n = int(args[0]) if args and args[0].isdigit() else 20
    crit = []
    for flag, key in (('--from', 'FROM'), ('--since', 'SINCE'), ('--subject', 'SUBJECT')):
        if opt(args, flag):
            crit += [key, '"%s"' % opt(args, flag)]
    _, data = m.uid('search', None, *(crit or ['ALL']))
    for uid in data[0].split()[-n:][::-1]:
        _, d = m.uid('fetch', uid, '(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)])')
        msg = email.message_from_bytes(d[0][1])
        print(f"{uid.decode()}\t{h(msg['Date'])}\t{h(msg['From'])}\t{h(msg['Subject'])}")


def cmd_get(m, args):
    _, d = m.uid('fetch', args[0], '(BODY.PEEK[])')
    msg = email.message_from_bytes(d[0][1])
    for k in ('From', 'To', 'Date', 'Subject'):
        print(f"{k}: {h(msg[k])}")
    out = opt(args, '--save')
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


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    m = connect()
    c, rest = sys.argv[1], sys.argv[2:]
    if c == 'test':
        print('Connexion OK,', m.select('INBOX', readonly=True)[1][0].decode(), 'messages dans INBOX')
    elif c == 'list':
        cmd_list(m, rest)
    elif c == 'get':
        cmd_get(m, rest)
    else:
        sys.exit(__doc__)
    m.logout()
