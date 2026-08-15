# 🧩 Exercices - Concevoir le Model Router v0.6

Fais les exercices avant de lire les solutions. L'objectif n'est pas d'écrire beaucoup de
code, mais de produire une spécification assez précise pour être implémentée ensuite.

## 📝 Exercice 1 - Schéma de métriques

Définis le schéma minimal d'un événement `run_metrics` pour la Factory.

Contraintes :

- il doit permettre de relier un run au workflow ;
- il doit distinguer tokens d'entrée, de sortie et de cache ;
- il doit expliquer la route choisie ;
- il doit permettre de calculer le coût par tâche réussie ;
- il doit préparer le chapitre 07 sans imposer un outil d'observabilité.

Livrable attendu : une table de champs avec type, sens et exemple.

## 🧾 Exercice 2 - Budgets par node

Choisis trois nodes du workflow parmi `ANALYZE`, `PLAN`, `IMPLEMENT`, `TEST`, `REVIEW`,
`PR`.

Pour chaque node, écris un budget :

```yaml
agent:
  max_iterations:
  max_tool_calls:

tokens:
  max_input:
  max_output:

cost:
  max_run_usd:

retry:
  max_attempts:
```

Justifie chaque limite en une phrase. Un budget sans justification est une valeur magique.

## 🔀 Exercice 3 - Classifier et router

Classe les demandes suivantes en `simple`, `medium` ou `complex`, puis choisis une route
initiale et un fallback autorisé.

| # | Demande |
| - | ------- |
| 1 | Résumer un log de test de 80 lignes. |
| 2 | Proposer un plan pour modifier trois fichiers Python. |
| 3 | Reviewer un patch de sécurité touchant l'authentification. |
| 4 | Générer le brouillon d'une PR à partir d'un diff déjà validé. |
| 5 | Diagnostiquer une régression intermittente en CI. |

Livrable attendu : une table `demande -> classe -> route -> fallback -> raison`.

## 💸 Exercice 4 - Coût par tâche réussie

Tu observes ce lot de tâches `medium` :

| Run | Route | Coût | Succès |
| --- | ----- | ---- | ------ |
| 1 | `local-large` | 0,02 | oui |
| 2 | `local-large` | 0,02 | non |
| 3 | `local-large` + fallback | 0,08 | oui |
| 4 | `local-large` | 0,02 | oui |
| 5 | `local-large` + fallback | 0,09 | non |

Calcule le coût par tâche réussie et explique pourquoi la moyenne par run est insuffisante.

## ✅ Critère de réussite

Tu as réussi le chapitre si ta spécification permet à quelqu'un d'autre de prédire :

- quelle route sera choisie ;
- quand le run s'arrêtera ;
- pourquoi un fallback a eu lieu ;
- combien coûte une tâche réussie sur un lot donné.
