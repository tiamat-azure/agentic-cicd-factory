# 🔧 02 - Tools, Function Calling & environnement

> Livrable : **Agent v0.2 - Coding Agent** - un agent Python sans framework qui sait
> choisir ses tools, respecter des permissions, valider ses entrées/sorties et modifier
> un petit repository en sécurité.

## 🎯 Objectifs pédagogiques

- Comprendre que la puissance d'un agent vient de son environnement d'action.
- Savoir décrire un tool proprement : nom, but, schéma, contraintes, sortie attendue.
- Concevoir un environnement minimal : filesystem, git, shell, pytest, HTTP, GitHub.
- Maîtriser schémas, structured outputs, validation, gestion d'erreurs, permissions,
  idempotence et timeouts.
- Distinguer ce que le modèle propose de ce que le runtime autorise réellement.
- Préparer le terrain du chapitre 03 : un agent outillé, mais pas encore orchestré.

## ✅ Prérequis

- Chapitre 01 (Agent v0.1).
- Être à l'aise avec JSON, shell, `git status` / `git diff` et la notion de sandbox.
- Durée estimée : **3 h** (1 h théorie + 1 h demos + 1 h exercices).

## 🚪 Gate du chapitre

> **Gate 1 (partie 2/2)** : tu dois pouvoir expliquer et faire tourner un agent qui
> choisit ses tools, sans framework agentique, avec des permissions et des validations
> explicites.

## 🗺️ Plan

1. Anatomie d'un tool : nom, description, schéma, sortie, erreurs.
1. Structured output et validation (JSON Schema, Pydantic, postconditions).
1. Construction de l'environnement : filesystem, git, shell, tests, HTTP.
1. Permissions : lecture, écriture, exécution, réseau, validation humaine.
1. Idempotence, timeouts, retries et ce que le runtime refuse d'exécuter.
1. Du set de tools au `Coding Agent` minimal : inspecter, modifier, tester, résumer.

## 🧭 Parcours pas à pas

| Étape | Support                                                                 | Ce que tu fais                                             |
| ----- | ----------------------------------------------------------------------- | ---------------------------------------------------------- |
| 1     | [`slides/`](slides/)                                                     | Lire les 4 leçons : contrats, validation, permissions     |
| 2     | [`demos/`](demos/)                                                       | Étudier les exemples de design d'environnement             |
| 3     | [`exercices/`](exercices/)                                               | Résoudre les 3 exercices -> **Agent v0.2**                |
| 4     | [`solutions/`](solutions/)                                               | Comparer seulement après tentative                         |
| 5     | [`../03-workflows-orchestration/`](../03-workflows-orchestration/)      | Enchaîner : un agent outillé ne suffit pas, il faut gérer l'orchestration |

## 🧱 Ce que le chapitre met en place

### 🛠️ Tools minimaux

- `list_files` / `read_file` pour inspecter.
- `write_file` / `apply_patch` pour modifier.
- `run_tests` pour vérifier.
- `git_diff` / `git_status` pour expliquer le patch.
- `http_get` ou `github_*` seulement si le besoin justifie l'accès réseau.

### 🧪 Validation minimale

- le modèle ne voit que des **contrats**, jamais l'implémentation brute ;
- chaque argument est validé avant exécution ;
- chaque erreur est réinjectée comme observation lisible ;
- toute écriture doit être bornée par un répertoire autorisé ;
- tout tool dangereux doit exiger une permission explicite ou humaine.

### 🔐 Permissions minimales

| Capability | Autorisé par défaut | Notes |
| ---------- | ------------------- | ----- |
| Lecture    | oui                 | sandbox de projet uniquement |
| Écriture   | non / bornée        | seulement dans les chemins autorisés |
| Shell      | oui, mais limité    | tests, formatage, pas d'actions destructives |
| Réseau     | non                 | à ouvrir au cas par cas |
| Git        | lecture d'abord     | `diff` avant `write` avant `commit` |

## 📚 Plan théorique

1. Pourquoi un agent vaut autant par ses tools que par son prompt.
1. Comment écrire un contrat de tool qui aide vraiment le modèle.
1. Validation, erreurs, timeouts, retries : rendre l'agent fiable.
1. Permissions et sandbox : empêcher le modèle de sortir du cadre.
1. Quel sous-ensemble de tools suffit pour un Coding Agent v0.2.

## 🧩 Principes directeurs appliqués ici

- **Framework-agnostic** : aucun framework d'agent imposé, seulement une boucle et des
  tools explicites.
- **Model-agnostic** : le modèle consomme des contrats structurés, pas du code métier.
- **Eval-first** : les validations de ce chapitre préparent les traces et jeux d'evals
  des chapitres 07 et 08.

## 🚦 Critère de sortie

Tu peux passer au chapitre 03 quand tu sais répondre clairement à ces 4 questions :

1. Quels tools donner à un agent de code, et lesquels lui interdire ?
1. Pourquoi le schéma d'entrée d'un tool est une partie du produit ?
1. Que fait le runtime quand une entrée est invalide ou hors permissions ?
1. En quoi un agent outillé diffère-t-il encore d'un workflow ?

## 🔗 Ressources

- [`slides/`](slides/) — leçons du chapitre.
- [`demos/`](demos/) — exemples de design d'environnement.
- [`exercices/`](exercices/) — mise en pratique guidée.
- [`solutions/`](solutions/) — correction repliée dans le site.
