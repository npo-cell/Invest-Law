import re,sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
NAVY=colors.HexColor('#1F3864')
base=ParagraphStyle('b',fontName='Helvetica',fontSize=10,leading=14.5,spaceAfter=6)
h1=ParagraphStyle('h1',fontName='Helvetica-Bold',fontSize=20,leading=24,textColor=NAVY,spaceAfter=4)
h2=ParagraphStyle('h2',fontName='Helvetica-Bold',fontSize=13.5,leading=17,textColor=NAVY,spaceBefore=12,spaceAfter=6)
meta=ParagraphStyle('m',parent=base,textColor=colors.HexColor('#5d6878'),fontSize=9)
def inl(t):
    t=t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t); t=re.sub(r'\*(.+?)\*',r'<i>\1</i>',t); return t
story=[];buf=[];kind=None
def flush():
    global buf,kind
    if buf:
        items=[ListItem(Paragraph(inl(x),base),leftIndent=12) for x in buf]
        story.append(ListFlowable(items,bulletType='1' if kind=='ol' else 'bullet',start='1' if kind=='ol' else '•',leftIndent=14,bulletFontSize=9 if kind=='ul' else 10,bulletFontName='Helvetica'))
        story.append(Spacer(1,4))
    buf=[];kind=None
lines=open(sys.argv[1]).read().split('\n')
for i,l in enumerate(lines):
    s=l.strip()
    m_ul=re.match(r'^- (.*)',s); m_ol=re.match(r'^\d+\. (.*)',s)
    if m_ul or m_ol:
        k='ul' if m_ul else 'ol'
        if kind and kind!=k: flush()
        kind=k; buf.append((m_ul or m_ol).group(1)); continue
    flush()
    if not s: continue
    if s.startswith('# '): story.append(Paragraph(inl(s[2:]),h1))
    elif s.startswith('## '): story.append(Paragraph(inl(s[3:]),h2))
    elif i==2: story.append(Paragraph(inl(s),meta))
    else: story.append(Paragraph(inl(s),base))
flush()
def foot(c,d):
    c.saveState();c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#5d6878'))
    c.drawString(18*mm,10*mm,'Comprendre les fonds de la gamme One Life · Invest-Law · 19/10/2026');c.drawRightString(A4[0]-18*mm,10*mm,'Page %d'%d.page);c.restoreState()
doc=SimpleDocTemplate(sys.argv[2],pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=18*mm,bottomMargin=18*mm,title='Comprendre les fonds de la gamme One Life',author='Invest-Law')
doc.build(story,onFirstPage=foot,onLaterPages=foot)
