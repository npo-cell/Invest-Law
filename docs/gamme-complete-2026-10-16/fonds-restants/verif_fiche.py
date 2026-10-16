import json, re, subprocess, sys, csv
BASE = "/home/user/Invest-Law/"


def txt(pdf):
    out = ""
    for mode in ([], ["-raw"], ["-layout"]):
        out += subprocess.run(["pdftotext", *mode, BASE + pdf, "-"], capture_output=True, text=True).stdout + "\n"
    return out

def norm(s):
    s = re.sub(r"-\s*\n\s*", "", s)  # césure
    return re.sub(r"\s+", "", s)

for isin in sys.argv[1:]:
    d = json.load(open(f"{BASE}docs/gamme-complete-2026-10-16/fonds-restants/fiches/{isin}.json", encoding="utf-8"))
    r = {"Factsheet_fichier": d.get("factsheet_fichier", ""), "KID_fichier": d.get("kid_fichier", "")}
    src = ""
    for k in ("Factsheet_fichier", "KID_fichier"):
        if r[k]:
            src += txt(r[k])
    S, S2 = norm(src), re.sub(r"\s+", "", src)
    miss = []
    chunks = []
    for f in ("politique_fr", "disclaimer", "compartiment", "indice", "gerants"):
        for line in d[f].split("\n"):
            for sent in re.split(r"(?<=[.;:])\s+", line):
                if sent.strip():
                    chunks.append((f, sent.strip()))
    for a in d["allocations"]:
        chunks.append(("alloc", a["libelle"]))
        chunks.append(("alloc", a["libelle"] + "|" + a["pct"]))
    for f, c in chunks:
        if f == "alloc" and "|" in c:
            lab, pct = c.split("|")
            if pct.replace(".", ",") not in src and pct not in src:
                miss.append((f, c))
            continue
        if f == "gerants":
            for g in c.split(", "):
                if g.replace(" ", "") not in S2 and g.split()[-1] not in src:
                    miss.append((f, g))
            continue
        n = re.sub(r"\s+", "", c)
        if n not in S and n not in S2:
            miss.append((f, c[:90]))
    print(isin, "manquants:", len(miss))
    for m in miss:
        print("   ", m)
    # sommes
    tot = {}
    for a in d["allocations"]:
        tot[a["type"]] = round(tot.get(a["type"], 0) + float(a["pct"]), 2)
    print("   sommes:", tot)
