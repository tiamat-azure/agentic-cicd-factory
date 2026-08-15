# 🧰 00 - Setup

> Livrable : **environnement fonctionnel** - un poste prêt à suivre le parcours, avec
> `uv`, Git, un accès LLM cloud, et un moteur local disponible pour la suite.

## 🎯 Objectifs pédagogiques

- Préparer l’environnement technique avant d’entrer dans le fond.
- Installer et valider les outils communs du parcours.
- Vérifier que le dépôt se clone, se synchronise et se lit correctement.
- Séparer clairement ce qui relève du setup du reste du contenu pédagogique.

## ✅ Prérequis

- [uv](https://docs.astral.sh/uv/) et Python 3.11+ - `uv` pilote lui-même
  l’interpréteur et les environnements.
- Git configuré (nom, email, clé SSH ou token HTTPS).
- Un compte GitHub et un token personnel si tu travailles avec GitHub depuis la CLI.
- Une clé API pour au moins un LLM cloud (Anthropic ou OpenAI).
- [Ollama](https://ollama.com) ou [vLLM](https://docs.vllm.ai) pour la partie locale,
  utile à partir du chapitre 05.

## 🚪 Gate du chapitre

> **Gate 0** : tu peux ouvrir le dépôt, installer ses prérequis et lancer un appel LLM de
> test sans contournement manuel.

## 🧭 Parcours pas à pas

| Étape | Ce que tu fais |
| ----- | -------------- |
| 1 | Installer `uv` puis vérifier qu’il est disponible dans le terminal. |
| 2 | Cloner le dépôt et te placer à la racine du projet. |
| 3 | Vérifier la structure générale du parcours et le sommaire du `README.md` racine. |
| 4 | Préparer les accès nécessaires : Git, clé LLM cloud, moteur local si disponible. |
| 5 | Tester la synchronisation d’un chapitre Python avec `uv sync` puis `uv run`. |
| 6 | Faire un premier appel LLM de validation avec le chapitre concerné quand tu y arrives. |

## 📚 Plan théorique

1. Pourquoi le setup est séparé du contenu métier.
1. Pourquoi `uv` est l’unique gestionnaire Python du parcours.
1. Ce qui doit déjà être prêt avant d’aborder les agents.
1. Comment vérifier qu’un environnement est vraiment utilisable.

## ⚙️ Installation

```sh
uv --version
git clone <url-du-repo>
cd agentic-cicd-factory
```

Pour les chapitres Python, la règle reste toujours la même :

```sh
cd NN-titre-reel
uv sync
uv run <script-ou-test>
```

## 🔎 Vérifications attendues

- `uv` répond dans le terminal.
- Le dépôt est accessible localement.
- Le sommaire du `README.md` racine affiche bien le chapitre 00.
- Un chapitre Python peut être synchronisé avec `uv sync`.
- Tu sais identifier quelle clé ou quel service LLM sera utilisé pour les chapitres
  suivants.

## 📦 Livrable

Un environnement prêt pour le chapitre 01, avec les outils d’exécution et les accès de
base validés.

## 📝 Auto-évaluation

Tu peux passer au chapitre 01 quand tu sais répondre sans hésiter :

1. Quel outil gère les dépendances Python du parcours ?
1. Quel accès LLM utilises-tu pour les chapitres cloud ?
1. Pourquoi le chapitre 00 ne contient-il pas encore de code métier ?
1. Quelle commande utilises-tu pour exécuter un script Python de chapitre ?
