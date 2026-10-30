# 1903RGB · Studio web à Nancy

**Site en ligne : https://1903rgb.github.io/Site-1903rgb/**

Site vitrine du studio web 1903RGB : sites vitrines sur mesure, boutiques en ligne, référencement local et identité visuelle pour les commerces, artisans et indépendants. Le site présente 20 maquettes de démonstration (une par métier) et permet de demander un rendez-vous, avec un devis sous 48 h.

- Contact : 1903rgb@gmail.com
- Instagram : [@_1903rgb_](https://www.instagram.com/_1903rgb_/)
- Mentions légales : https://1903rgb.github.io/Site-1903rgb/mentions-legales.html

## Pages

| Page | Lien |
|---|---|
| Accueil | https://1903rgb.github.io/Site-1903rgb/ |
| Réalisations (20 maquettes) | https://1903rgb.github.io/Site-1903rgb/#realisations |
| Prendre rendez-vous | https://1903rgb.github.io/Site-1903rgb/#rdv |
| Mentions légales et données personnelles | https://1903rgb.github.io/Site-1903rgb/mentions-legales.html |

Les maquettes sont dans `maquettes/<nom>/` (page d'accueil + une page intérieure chacune). Ce sont des marques fictives, non indexées par les moteurs de recherche.

## Organisation du dépôt

```
index.html              page d'accueil (générée, ne pas modifier à la main)
src/page.html           source de la page d'accueil : contenu et styles
src/maquettes.json      liste des 20 maquettes (nom, métier, ville, catégorie…)
build.py                génère index.html à partir de src/
assets/js/main.js       interactions : menu, filtres, mur animé, formulaire
assets/css/  assets/fonts/   polices hébergées sur le site (aucun appel à Google)
assets/vendor/          GSAP, ScrollTrigger, Lenis (copies locales vérifiées)
assets/thumbs/          vignettes WebP des maquettes
assets/video/           vidéo de présentation (720p) et son aperçu
assets/brand/           logo, icônes
maquettes/              les 20 maquettes de démonstration
mentions-legales.html   mentions légales et RGPD
404.html, robots.txt, sitemap.xml, .well-known/security.txt
```

## Modifier le site

1. Modifier `src/page.html` (textes, sections, styles) ou `assets/js/main.js`.
2. Régénérer la page d'accueil : `python3 build.py`
3. Enregistrer et publier : `git add -A && git commit -m "…" && git push`
4. GitHub Pages met le site à jour en 1 à 2 minutes.

## Formulaire de rendez-vous

Les demandes sont envoyées par [Web3Forms](https://web3forms.com) (offre gratuite, 250 envois par mois) vers 1903rgb@gmail.com. La clé d'accès se trouve dans `assets/js/main.js` (`ACCESS_KEY`). Elle est publique par conception ; la limiter au domaine du site dans l'espace Web3Forms (« Allowed domains »).

## Hébergement et sécurité

- Hébergé sur GitHub Pages (branche `main`, dossier racine), HTTPS.
- Politique de sécurité du contenu (CSP) sur chaque page, aucun script ni police chargé depuis un service tiers, aucun cookie, aucune mesure d'audience.
- Signaler une faille : voir [SECURITY.md](SECURITY.md).

## Passage au nom de domaine 1903rgb.fr

1. Dans `build.py`, remplacer `BASE` par `https://1903rgb.fr/`, puis relancer `python3 build.py`.
2. Mettre à jour les adresses dans `mentions-legales.html` (balise canonical), `robots.txt`, `sitemap.xml` et `404.html`.
3. Ajouter un fichier `CNAME` contenant `1903rgb.fr`.
4. Chez le registraire du domaine : enregistrements A vers 185.199.108.153, 185.199.109.153, 185.199.110.153 et 185.199.111.153, et `www` en CNAME vers `1903rgb.github.io`.
5. Dans les réglages Pages du dépôt : renseigner le domaine et cocher « Enforce HTTPS ».

## Crédits

Conception et développement : 1903RGB. Photographies des maquettes : [Unsplash](https://unsplash.com) (licence Unsplash). Polices : Google Fonts (licence SIL Open Font License), hébergées localement.
