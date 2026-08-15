# 🤖 Agent v0.1 - agent minimal sans framework

```sh
cd demos/03_agent_minimal
uv run demos/03_agent_minimal/main.py
uv run demos/03_agent_minimal/main.py "Combien de fichiers Python contient ce dépôt et que fait chacun ?"
```

## 🏗️ Architecture

```text
main.py     point d'entrée, objectif
  └── agent.py    LA BOUCLE : think -> act -> observe -> loop
        ├── model.py   abstraction LLM (anthropic | ollama)  -> ch. 05
        ├── tools.py   3 tools + bac à sable                  -> ch. 02
        └── state.py   contexte ⊂ state, garde-fous           -> ch. 06
```

Aucune dépendance agentique : `requests` et `python-dotenv`, rien d'autre. C'est la
condition du **Gate 1**.

## 🚧 Ce que cet agent ne sait pas encore faire

| Manque                         | Chapitre qui le comble |
| ------------------------------ | ---------------------- |
| Écrire des fichiers, corriger  | 02                     |
| Déléguer à d'autres agents     | 03                     |
| Exposer ses tools à d'autres   | 04                     |
| Router vers le bon modèle      | 05-06                  |
| Être tracé et mesuré           | 07-08                  |
| Être gouverné (policies, HITL) | 09                     |

Ne cherche pas à ajouter ces briques maintenant : chaque chapitre suivant les introduit
avec le raisonnement qui va avec.
