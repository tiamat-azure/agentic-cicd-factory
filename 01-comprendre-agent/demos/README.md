# Demos - chapitre 01

Exécute-les dans l'ordre. Chaque demo répond à une question laissée ouverte par la
précédente.

| Demo                                             | Question posée                             |
| ------------------------------------------------ | ------------------------------------------ |
| [`01_llm_brut.py`](01_llm_brut.py)               | Que manque-t-il à un LLM seul ?            |
| [`02_boucle_manuelle.py`](02_boucle_manuelle.py) | À quoi ressemblent Think / Act / Observe ? |
| [`03_agent_minimal/`](03_agent_minimal/)         | Comment automatiser cette boucle ?         |

## Préparation

```sh
cd 01-comprendre-agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt pytest
cp .env.example .env    # renseigne ta clé, ou LLM_PROVIDER=ollama
```

Vérifie d'abord que le bac à sable échoue bien, sans agent :

```sh
cd demos/03_agent_minimal/sandbox && python -m pytest -q
```

## Exécution

```sh
python demos/01_llm_brut.py
python demos/02_boucle_manuelle.py
python demos/02_boucle_manuelle.py --sans-observation   # expérience du ping-pong
cd demos/03_agent_minimal && python main.py
```

## Ordre de lecture du code de `03_agent_minimal/`

1. `agent.py` -> `Agent.run()` : **tout le chapitre est là**, lis-la en premier.
1. `state.py` : ce que le runtime sait vs ce que le modèle voit.
1. `tools.py` : le contrat d'un tool, et le bac à sable.
1. `model.py` : l'abstraction model-agnostic (ancêtre du Model Gateway, ch. 05).

## Preuve model-agnostic

Le même agent, sans une ligne de code modifiée, sur deux fournisseurs :

```sh
LLM_PROVIDER=anthropic python main.py
LLM_PROVIDER=ollama    python main.py
```

Compare les traces : nombre d'itérations, ordre des tools, qualité du diagnostic. C'est ta
première observation empirique de la différence entre modèles - on la rendra mesurable au
chapitre 08.
