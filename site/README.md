# site/ - le parcours en version web

Site statique [Astro Starlight](https://starlight.astro.build/) qui rend le parcours de
façon pédagogique : navigation par chapitre, recherche, thème clair/sombre, progression
pas à pas.

> **Le markdown des chapitres reste la seule source de vérité.** Ce dossier ne contient
> aucun contenu pédagogique : il lit directement `../NN-*/**` au build. Pour corriger une
> leçon, on édite le fichier du chapitre, jamais un fichier de `site/`.

## Commandes

`npm` est l'outil de build **du site uniquement** (le code Python des chapitres reste sous
`uv`).

```sh
cd site
npm ci        # installe les dépendances (package-lock.json commité)
npm run dev   # serveur local, rechargement à chaud sur les fichiers de chapitre
npm run build # génère dist/
npm run preview
```

## Ce que le site ajoute au markdown

| Élément                  | Origine                                                                 |
| ------------------------ | ----------------------------------------------------------------------- |
| Bandeau **Livrable**     | ligne `> Livrable : **...** - ...` du `README.md` du chapitre           |
| Badge **Gate**           | table des 5 gates, dans `src/loaders/chapitres.ts`                      |
| Badge **durée**          | `Durée estimée : **...**` du `README.md` du chapitre                    |
| **Principes** directeurs | encart automatique en tête de chaque chapitre                           |
| **Progression**          | cases à cocher en `localStorage`, aucun backend, aucun compte           |
| **Solutions** repliées   | toute page issue de `solutions/` est rendue dans un `<details>`         |
| Pages de code            | les `.py` / `.toml` / `.sh` des chapitres sont rendus en pages lisibles |

## Structure

```
site/
├─ astro.config.mjs          # sidebar = les 12 chapitres, base GitHub Pages
├─ src/
│  ├─ content.config.ts      # collection `docs` alimentée par le loader
│  ├─ loaders/chapitres.ts   # lit ../NN-*/**, réécrit les liens, extrait les métadonnées
│  ├─ components/            # PageTitle (livrable/gate/principes), Sidebar (progression)
│  └─ styles/custom.css
└─ dist/                     # sortie statique (non commitée)
```

## Ajouter un chapitre

Rien à faire ici : créer le dossier `NN-titre/` avec son `README.md` à la racine du dépôt
suffit. Tant qu'un chapitre n'a pas de `README.md`, le site publie une page « à venir »
pour que les 12 chapitres restent visibles.

## Déploiement

`.github/workflows/deploy-site.yml` construit le site sur chaque PR et le publie sur
GitHub Pages depuis `main` (`https://tiamat-azure.github.io/agentic-cicd-factory/`).
