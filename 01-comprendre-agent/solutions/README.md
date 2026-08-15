# Solutions - chapitre 01

> À ouvrir **après** avoir tenté. Une solution lue trop tôt supprime l'apprentissage.

| Fichier                                        | Exercice                    |
| ---------------------------------------------- | --------------------------- |
| [`01-classification.md`](01-classification.md) | 1 - niveaux d'autonomie     |
| [`02-tool-recherche.py`](02-tool-recherche.py) | 2 - ajout d'un tool         |
| [`03-agent-v0.1/`](03-agent-v0.1/)             | 3 - **livrable Agent v0.1** |

## Utiliser la solution de l'exercice 3

```sh
cp solutions/03-agent-v0.1/{agent.py,state.py} demos/03_agent_minimal/
cd demos/03_agent_minimal && python main.py
cat run.json
```

## Lecture critique attendue

La solution 3 est correcte mais pas parfaite. Sais-tu dire :

1. Pourquoi `_arreter(state, "succes_implicite", ...)` est un **filet**, et pourquoi il ne
   faut pas s'y fier ? (indice : que vaut ce statut dans un jeu d'evals ?)
1. Pourquoi `max_tokens_total` est vérifié **après** l'appel et pas avant, et ce que ça
   coûte au pire ? (corrigé au ch. 06 par une estimation a priori)
1. Pourquoi `run.json` est écrasé à chaque run, et pourquoi c'est inacceptable dès le ch.
   07 ?
1. Pourquoi la détection de ping-pong ne regarde que le **tour précédent**, et quel cycle
   elle laisse donc passer ?

Ces quatre limites sont voulues : elles sont les points d'entrée des chapitres suivants.
