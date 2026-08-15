# 🧩 Exercices - Concevoir la Factory v1.0

Fais les exercices avant de lire les solutions. L'objectif est de produire un contrat de
CI/CD agentique clair, pas un workflow complet d'un outil particulier.

## 📝 Exercice 1 - Matrice de déclenchement

Pour chaque changement, indique les suites d'evals à lancer et le risque mesuré.

| # | Changement |
| - | ---------- |
| 1 | Modification du prompt de `PLAN`. |
| 2 | Ajout d'un argument optionnel à un tool de lecture de fichiers. |
| 3 | Passage de `local-large` à `cloud-frontier` pour les tâches `complex`. |
| 4 | Déplacement du gate humain après le node `IMPLEMENT`. |
| 5 | Changement d'un seuil d'eval de `0.80` à `0.75`. |

Livrable attendu : une table `changement -> evals -> risque -> décision si échec`.

## 🚦 Exercice 2 - Règles de blocage

Écris cinq règles de blocage pour la Factory v1.0.

Contraintes :

- au moins une règle de qualité ;
- au moins une règle de coût ;
- au moins une règle de sécurité ou policy ;
- au moins une règle de traçabilité ;
- chaque règle doit produire `pass`, `block` ou `needs-human-approval`.

## 🧾 Exercice 3 - Décision de pipeline

Tu observes ce run :

| Signal | Valeur |
| ------ | ------ |
| Eval `plan_validity` | `0.88`, seuil `0.85`, baseline `0.90` |
| Eval `tool_safety` | `0.79`, seuil `0.80`, baseline `0.83` |
| Coût par succès | `0.31 USD`, budget `0.35 USD` |
| Policy allow/deny | conforme |
| Trace | manque la version du prompt |

Décide si la pipeline passe, bloque ou demande une approbation humaine. Justifie avec les
règles de l'exercice 2.

## 🌉 Exercice 4 - Préparer le chapitre 11

Liste les artefacts qu'une PR générée par agent devra joindre pour être reviewable.

Contraintes :

- au moins un artefact lié à la demande initiale ;
- au moins un artefact lié aux evals ;
- au moins un artefact lié aux policies ;
- au moins un artefact lié aux exceptions humaines.

## ✅ Critère de réussite

Tu as réussi le chapitre si quelqu'un d'autre peut lire ton contrat et prédire :

- quelles evals se déclenchent ;
- quand la pipeline bloque ;
- qui peut approuver une exception ;
- quelles preuves seront attachées à une future PR automatique.
