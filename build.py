# Génère index.html (site complet, pour GitHub Pages) et _artifact.html (fragment pour l'aperçu claude.ai)
import html, re, sys
sys.path.insert(0, "/home/claude/portfolio/promo")
from data import sites

CAT = {"01":"commerce","02":"commerce","05":"commerce","09":"commerce","11":"commerce","20":"commerce",
       "07":"sante","14":"sante","16":"sante","19":"sante","12":"sante",
       "03":"artisans","08":"artisans","10":"artisans","17":"artisans",
       "04":"services","06":"services","15":"services","13":"services","18":"services"}
E = html.escape
S = sites()
cards = "".join(
    f'<a class="card" data-cat="{CAT[s["n"]]}" href="maquettes/{s["slug"]}/index.html">'
    f'<figure><img src="assets/thumbs/s{s["n"]}.jpg" alt="Page d\'accueil de la maquette {E(s["name"])}" loading="lazy" width="960" height="600"></figure>'
    f'<div class="meta"><div><h3>{E(s["name"])}</h3><p>{E(s["biz_fr"])} · {E(s["city"])}</p></div><span class="go">Voir →</span></div></a>'
    for s in S)
order = [1, 12, 6, 20, 5, 16, 9, 14, 3, 18, 2, 19, 8, 13, 11, 7, 4, 17, 10, 15]
a, b = order[::2], order[1::2]
col = lambda ids: '<div class="col">' + "".join(f'<img src="assets/thumbs/s{i:02d}.jpg" alt="">' for i in ids * 2) + "</div>"
wall = col(a) + col(b)

src = open("src/page.html").read().replace("{{CARDS}}", cards).replace("{{WALL}}", wall)
open("_artifact.html", "w").write(src)

head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]
full = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
open("index.html", "w").write(full)
print("ok", len(full))
