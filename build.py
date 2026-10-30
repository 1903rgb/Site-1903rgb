# Génère index.html (site en ligne, avec CSP) et _artifact.html (aperçu claude.ai, sans CSP propre)
import html, sys
sys.path.insert(0, "/home/claude/portfolio/promo")
from data import sites

BASE = "https://1903rgb.github.io/Site-1903rgb/"   # passer à https://1903rgb.fr/ quand le domaine sera branché
FONTCSS = "gf-edcd27a86c.css"
CSP = ("default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self'; "
       "img-src 'self' data:; media-src 'self'; connect-src https://api.web3forms.com; form-action 'self'; "
       "base-uri 'none'; object-src 'none'; upgrade-insecure-requests")
CAT = {"01":"commerce","02":"commerce","05":"commerce","09":"commerce","11":"commerce","20":"commerce",
       "07":"sante","14":"sante","16":"sante","19":"sante","12":"sante",
       "03":"artisans","08":"artisans","10":"artisans","17":"artisans",
       "04":"services","06":"services","15":"services","13":"services","18":"services"}
E = html.escape
S = sites()

def card(s):
    en = s["lang"] == "EN"
    return (f'<a class="card" data-cat="{CAT[s["n"]]}" href="maquettes/{s["slug"]}/index.html"{" hreflang=\"en\"" if en else ""}>'
            f'<figure><img src="assets/thumbs/s{s["n"]}.webp" alt="Page d’accueil de la maquette {E(s["name"])}" loading="lazy" decoding="async" width="960" height="600"></figure>'
            f'<div class="meta"><div><h3{" lang=\"en\"" if en else ""}>{E(s["name"])}</h3><p>{E(s["biz_fr"])} · <span class="nw">{E(s["city"])}</span></p></div>'
            f'<span class="go" aria-hidden="true">Voir →</span></div></a>')

cards = "".join(card(s) for s in S)
order = [1, 12, 6, 20, 5, 16, 9, 14, 3, 18, 2, 19, 8, 13, 11, 7, 4, 17, 10, 15]
def col(ids):
    imgs = [f'<img src="assets/thumbs/w/s{i:02d}.webp" alt="" width="480" height="300" decoding="async"{"" if k < len(ids) else " loading=\"lazy\""}>'
            for k, i in enumerate(ids * 2)]
    return '<div class="col">' + "".join(imgs) + "</div>"
wall = col(order[::2]) + col(order[1::2])

src = open("src/page.html").read()
for k, v in {"{{CARDS}}": cards, "{{WALL}}": wall, "{{BASE}}": BASE, "{{FONTCSS}}": FONTCSS}.items():
    src = src.replace(k, v)
script = '<script src="assets/js/main.js" defer></script>'

art = src.replace("{{HEADMETA}}", '<meta name="claude:viewport-fit-sides" content="cover">').replace("{{SCRIPT}}", script)
open("_artifact.html", "w").write(art)

page = src.replace("{{HEADMETA}}\n", "").replace("{{SCRIPT}}", script)
head_end = page.index("</style>") + len("</style>")
head, body = page[:head_end], page[head_end:]
full = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        f'<meta http-equiv="Content-Security-Policy" content="{CSP}">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head + "\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n")
open("index.html", "w").write(full)
print("ok", len(full))
