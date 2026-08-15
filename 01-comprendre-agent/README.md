# 🤖 01 - Comprendre réellement ce qu'est un Agent

> Livrable : **Agent v0.1** - un agent Python minimal, sans framework, capable d'exécuter
> 2 à 3 tools et de terminer une tâche.

## 🎯 Objectifs pédagogiques

- Sortir de la définition marketing "un LLM qui utilise des outils".
- Comprendre la boucle fondamentale : LLM -> Tool calling -> Think/Act/Observe -> State ->
  Loop -> Agent.
- Distinguer LLM application, chain, workflow, agent et système multi-agent.
- Savoir répondre à : quand NE PAS utiliser un agent ?
- Écrire soi-même la boucle agentique, sans framework, derrière une abstraction de modèle.

## ✅ Prérequis

- Chapitre 00 (environnement fonctionnel : Python 3.11+ géré par
  [uv](https://docs.astral.sh/uv/), une clé LLM cloud **ou** Ollama).
- Bases Python (fonctions, classes, boucles, `dict`/`json`).
- Durée estimée : **3 h** (1 h théorie + 1 h demos + 1 h exercices).

## 🚪 Gate du chapitre

> **Gate 1 (partie 1/2)** : tu dois pouvoir exécuter un agent que tu as écrit toi-même,
> sans aucun framework agentique, et expliquer ligne par ligne pourquoi c'est un agent et
> pas une chaîne.

## 🧭 Parcours pas à pas

| Étape | Support                                                                                      | Ce que tu fais                                  |
| ----- | -------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| 1     | [`slides/01-definitions.md`](slides/01-definitions.md)                                       | Lire : le spectre autonomie, les 5 niveaux      |
| 2     | [`demos/01_llm_brut.py`](demos/01_llm_brut.py)                                               | Exécuter : un LLM seul, constater ce qui manque |
| 3     | [`slides/02-boucle-think-act-observe.md`](slides/02-boucle-think-act-observe.md)             | Lire : anatomie de la boucle                    |
| 4     | [`demos/02_boucle_manuelle.py`](demos/02_boucle_manuelle.py)                                 | Exécuter : c'est **toi** qui joues la boucle    |
| 5     | [`slides/03-state-et-terminaison.md`](slides/03-state-et-terminaison.md)                     | Lire : state, budget, conditions d'arrêt        |
| 6     | [`demos/03_agent_minimal/`](demos/03_agent_minimal/)                                         | Lire puis exécuter l'agent complet              |
| 7     | [`slides/04-quand-ne-pas-utiliser-un-agent.md`](slides/04-quand-ne-pas-utiliser-un-agent.md) | Lire : critères de décision                     |
| 8     | [`exercices/`](exercices/)                                                                   | Faire les 3 exercices -> **Agent v0.1**         |

## 📚 Plan théorique

1. Définitions : LLM application vs chain vs workflow vs agent vs multi-agent.
1. La boucle Think -> Act -> Observe.
1. Notion de state et de terminaison.
1. Construction d'un agent minimal sans framework (`agent.py`, `tools.py`, `state.py`).
1. Discussion : critères de décision agent vs non-agent.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : zéro dépendance agentique. Uniquement `requests`/SDK HTTP.
- **Model-agnostic** : tout passe par `ModelClient` (`demos/03_agent_minimal/model.py`).
  Aucun `if model == ...` dans le code métier. C'est l'embryon du Model Gateway du ch. 05.
- **Eval-first** : pas encore d'evals (ch. 07+), mais les demos loguent déjà chaque tour
  de boucle - ce log est la matière première du tracing du ch. 07.

## ⚙️ Installation

```sh
cd 01-comprendre-agent
uv sync                # crée .venv et installe les dépendances de pyproject.toml
cp .env.example .env   # renseigne ANTHROPIC_API_KEY ou laisse le provider ollama
```

Tout script se lance ensuite avec `uv run` (pas d'activation manuelle du venv) :

```sh
uv run demos/01_llm_brut.py
```

## 🔗 Ressources

- Anthropic -
  [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
  (distinction workflow / agent).
- Hugging Face -
  [Agents Course, Unit 1](https://huggingface.co/learn/agents-course/en/unit1/introduction).
- ReAct -
  [Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629).

## 📝 Auto-évaluation

Tu peux passer au chapitre 02 quand tu réponds sans hésiter :

1. Quelle est la différence structurelle entre un workflow et un agent ?
1. Qui décide de l'arrêt dans un agent, et quels garde-fous doit-on ajouter ?
1. Pourquoi le résultat d'un tool doit-il retourner dans l'historique du modèle ?
1. Cite 3 situations où un agent est le mauvais choix.
1. Où placerais-tu la frontière entre `agent.py` et `model.py` - et pourquoi ?
