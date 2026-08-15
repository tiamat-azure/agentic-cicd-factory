# AGENTS.md

## What this project does

Contenu (markdown) d'une formation, découpée en chapitres numérotés sur `main` (pas de
branche par chapitre - voir `ressources/prd/PRD.md` pour le raisonnement). Chaque chapitre
est un dossier autonome avec ses slides, démos, exercices et solutions.

## Commands

Aucun build : contenu markdown statique. Vérification des liens morts via CI
(`.github/workflows/check-links.yml`), déclenchée sur push/PR vers `main`.

## Architecture

```
README.md          # sommaire du parcours, source de vérité des chapitres publiés
00-setup/           # pré-requis techniques avant chapitre 1
NN-chapitre/        # un dossier par chapitre (01 à 12)
  README.md         #   objectifs, durée, prérequis, plan
  slides/
  demos/
  exercices/
  solutions/
ressources/
  prd/PRD.md        # raisonnement sur l'organisation du repo (branches vs dossiers)
```

## Code conventions

- Numéroter sur 2 chiffres (`01-`, `02-`, ...) - le tri lexicographique casse sinon.
- Un `README.md` par chapitre : objectifs pédagogiques, durée estimée, prérequis, plan.
- Ne jamais dupliquer une ressource commune dans un chapitre : elle vit dans
  `ressources/`.
- Chapitre en cours de rédaction : soit préfixer `_wip-NN-...`, soit simplement ne pas le
  lister dans le sommaire du `README.md` racine (source de vérité).
- Rédiger un chapitre sur une branche `feat/chapitre-NN`, merger dans `main` seulement
  quand il est publiable.

## Tests

Pas de tests automatisés au-delà de la CI de liens morts. Si un fil rouge applicatif
(`app/`) est ajouté (scénario C du `ressources/prd/PRD.md`), ses exemples de code devront
être exécutés en CI.

## Known pitfalls

- Ne pas utiliser de branche par chapitre pour du contenu permanent (coût de rebase qui
  explose - voir `ressources/prd/PRD.md`, scénario B).
- Les dossiers `NN-chapitre/` sont des placeholders génériques : les renommer avec un
  titre réel dès que le sujet du chapitre est défini.
