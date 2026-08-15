# 🧪 Démo - Lire une pipeline Agentic CI/CD

Cette démo est une étude de cas papier. Elle ne demande pas d'installer un outil :
l'objectif est de savoir lire une décision de CI/CD agentique avant de l'automatiser.

## 🧾 Changement étudié

Un commit modifie :

- un prompt de `REVIEW` pour demander une réponse plus courte ;
- une policy qui autorise le tool `create_pull_request` seulement après evals vertes ;
- le seuil de réussite de l'eval `review_finds_security_bug` de `0.82` à `0.85`.

## 🔁 Déclenchement attendu

| Élément modifié | Suite déclenchée | Raison |
| --------------- | ---------------- | ------ |
| Prompt de review | evals de review, safety, regression | le comportement du reviewer change |
| Policy PR | allow/deny matrix, escalation | une action externe critique est contrôlée |
| Seuil d'eval | meta-eval, stabilité | le thermomètre change |

## 📊 Résultat de run

| Gate | Résultat | Décision |
| ---- | -------- | -------- |
| Checks classiques | vert | continuer |
| Evals review | `0.84`, baseline `0.86`, seuil `0.85` | bloquer |
| Budget coût | dans le budget | continuer |
| Policy allow/deny | conforme | continuer |
| Audit trace | complète | continuer |

## 🚦 Décision

La pipeline bloque. Le seuil annoncé est `0.85`, le score courant est `0.84`, et la
régression par rapport à la baseline est visible. Le bon réflexe n'est pas de baisser le
seuil dans le même commit, mais d'inspecter les cas échoués ou de demander une exception
humaine tracée.

## 🧠 Question à retenir

La CI/CD agentique ne demande pas seulement « est-ce que ça passe ? ». Elle demande :
« quel risque a changé, quelle preuve l'a mesuré, et qui accepte l'écart ? ».
