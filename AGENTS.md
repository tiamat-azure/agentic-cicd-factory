# 🤖 AGENTS.md

## 📖 What this project does

Contenu (markdown) d'une formation, découpée en chapitres numérotés sur `main` (pas de
branche par chapitre - voir `ressources/prd/PRD.md` pour le raisonnement). Chaque chapitre
est un dossier autonome avec ses slides, démos, exercices et solutions. Le parcours (12
chapitres + setup) suit un fil rouge unique, la "Agentic CI/CD Factory" - voir
`ressources/prd/01-PRD.md` pour le raisonnement derrière ce parcours.

## 💻 Commands

Le contenu pédagogique est du markdown statique. Vérification des liens morts via CI
(`.github/workflows/check-links.yml`), déclenchée sur push/PR vers `main`.

Le site web du parcours (`site/`) est le seul artefact buildé, avec **npm** :

```sh
cd site
npm ci                   # dépendances (Node 22+, package-lock.json commité)
npm run dev              # aperçu local avec rechargement à chaud
npm run build            # sortie statique dans site/dist/
```

Deux outils, deux périmètres disjoints : **`uv` pour le code Python des chapitres**,
**`npm` pour `site/` uniquement**. Ne jamais introduire Node hors de `site/`, ni `pip`
nulle part.

Le code des chapitres est en Python et **`uv` est le seul outil de build/exécution
autorisé** (jamais `pip`, `python -m venv`, `poetry`, `conda`) :

```sh
cd NN-titre-reel
uv sync                  # crée .venv + installe pyproject.toml (dont le groupe dev)
uv run demos/xxx.py      # exécuter un script
uv run pytest -q         # exécuter les tests
uv add <paquet>          # ajouter une dépendance
```

## 🏗️ Architecture

```
README.md          # sommaire du parcours, source de vérité des chapitres publiés
00-setup/           # pré-requis techniques avant chapitre 1
NN-titre-reel/      # un dossier par chapitre (01 à 12), titre explicite du sujet
  README.md         #   objectifs, durée, prérequis, plan
  slides/
  demos/
  exercices/
  solutions/
ressources/
  prd/PRD.md        # raisonnement sur l'organisation du repo (branches vs dossiers)
  prd/01-PRD.md     # raisonnement sur le parcours en 12 chapitres (fil rouge)
site/               # site Astro Starlight - AUCUN contenu pédagogique, voir site/README.md
```

### 🌐 Le site (`site/`)

Le site lit `../NN-*/**` au build via un loader Astro (`site/src/loaders/chapitres.ts`) :
**il ne duplique jamais le contenu**. Conséquences à respecter :

- Corriger une leçon = éditer le fichier du chapitre, jamais un fichier de `site/`.
- Ajouter un chapitre = créer `NN-titre/README.md` ; aucune config du site à toucher (un
  chapitre sans `README.md` est publié comme page « à venir »).
- Le loader dérive du markdown : titre (premier `#`), livrable (`> Livrable : **...**`),
  durée (`Durée estimée : **...**`), gate (table des 5 gates dans le loader). Ne pas
  casser ces conventions d'écriture dans les `README.md` de chapitre.
- Toute page issue de `solutions/` est repliée automatiquement côté site.

### 📚 Les 12 chapitres et leur livrable (fil rouge Agentic CI/CD Factory)

| #   | Chapitre                                | Livrable                  |
| --- | --------------------------------------- | ------------------------- |
| 01  | Comprendre l'Agent                      | Agent v0.1                |
| 02  | Tools, Function Calling & environnement | Agent v0.2 - Coding Agent |
| 03  | Workflows & orchestration               | Factory v0.3              |
| 04  | MCP                                     | Tools via MCP             |
| 05  | LLM Agnostic                            | Model Gateway v0.5        |
| 06  | Token Engineering & Model Routing       | Model Router v0.6         |
| 07  | Observability & Tracing                 | Observability v0.7        |
| 08  | Evaluation Engineering                  | Evaluation Framework v0.8 |
| 09  | Agent Security & Governance             | Policy Engine v0.9        |
| 10  | Agentic CI/CD                           | Factory v1.0              |
| 11  | Automatic PR Factory                    | PR Factory v1.1           |
| 12  | Production : Agent Platform             | Factory v2.0              |

Chaque chapitre doit produire un livrable concret et cumulatif sur le même projet fil
rouge - pas d'exercices isolés. Raisonnement complet : `ressources/prd/01-PRD.md`.

## 📐 Code conventions

- Un chapitre contenant du code déclare ses dépendances dans son propre `pyproject.toml`
  (+ `uv.lock` commité). Jamais de `requirements.txt`. Toute commande montrée à
  l'apprenant, dans les slides, démos, énoncés d'exercices ou solutions, doit utiliser
  `uv run` / `uv sync` - aucune activation manuelle de venv.
- Dans le code, ne jamais invoquer `"python"` en sous-processus : utiliser
  `sys.executable` pour rester correct sous l'environnement géré par `uv`.
- Numéroter sur 2 chiffres (`01-`, `02-`, ...) - le tri lexicographique casse sinon.
- Un `README.md` par chapitre : objectifs pédagogiques, durée estimée, prérequis, plan.
- Ne jamais dupliquer une ressource commune dans un chapitre : elle vit dans
  `ressources/`.
- Chapitre en cours de rédaction : soit préfixer `_wip-NN-...`, soit simplement ne pas le
  lister dans le sommaire du `README.md` racine (source de vérité).
- Rédiger un chapitre sur une branche `feat/chapitre-NN`, merger dans `main` seulement
  quand il est publiable.
- Tout contenu de chapitre doit respecter 3 principes directeurs (voir
  `ressources/prd/01-PRD.md`) : framework-agnostic (jamais un pattern présenté comme
  propre à un framework), model-agnostic (jamais de code métier conditionné sur un modèle
  donné - toujours via une abstraction de type Model Gateway), eval-first (à partir du
  chapitre 07, toute évolution proposée dans les exemples doit être mesurable via des
  evals, pas seulement affirmée meilleure).
- 5 gates jalonnent le parcours et doivent rester identifiables dans le contenu : agent
  sans framework (ch. 01-02), workflow multi-agents (ch. 03-04), changement de LLM sans
  modifier l'agent (ch. 05), preuve par evals qu'une version est meilleure (ch. 06-08), PR
  générée automatiquement à partir d'une demande (ch. 11, gate final).
- Tout titre markdown (`#`, `##`, ...) dans n'importe quel fichier `.md` du dépôt (hors
  `site/`) doit être préfixé d'un émoji adéquat au sens du titre, suivi d'un espace, ex.
  `## 🎯 Objectifs pédagogiques`. S'applique à tout nouveau fichier et à toute nouvelle
  section ajoutée à un fichier existant.

## 🧪 Tests

La CI vérifie les liens morts et construit le site (`npm run build` échoue si un chapitre
casse le loader) : c'est le filet de sécurité du contenu. Si un fil rouge applicatif
(`app/`) est ajouté (scénario C du `ressources/prd/PRD.md`), ses exemples de code devront
être exécutés en CI.

## ⚠️ Known pitfalls

- Ne pas utiliser de branche par chapitre pour du contenu permanent (coût de rebase qui
  explose - voir `ressources/prd/PRD.md`, scénario B).
- Les dossiers de chapitre doivent toujours porter un titre réel (ex. `05-llm-agnostic/`),
  jamais un placeholder générique.
- Ne jamais copier du contenu de chapitre dans `site/` : le site deviendrait une seconde
  source de vérité et divergerait.
- `npm` reste confiné à `site/`. Aucun `package.json` ailleurs dans le dépôt.
