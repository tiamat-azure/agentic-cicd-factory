# 📝 Exercices - construire PR Factory v1.1

## 🎯 Objectif

Produire les artefacts du Gate 5 sans écrire de code inutile : chaîne d'agents, PR body,
évaluation, coût et décision human-stop.

## 🧩 Exercice 1 - contrat de chaîne

Pour la demande suivante, remplis le handoff de chaque agent :

> Ajoute une vérification qui refuse une PR automatique si une eval sécurité critique est
> sous son seuil.

Pour chaque étape, indique :

- entrée minimale ;
- sortie attendue ;
- décision `auto`, `human` ou `deny` ;
- raison de la décision.

## 🧾 Exercice 2 - PR body

À partir des métadonnées suivantes, rédige les sections `Summary`, `Validation`,
`Evaluation`, `Cost and Traceability`, `Security and Governance` et `Human Review
Required`.

| Champ | Valeur |
| ----- | ------ |
| `run_id` | `run-pr-117` |
| `task_class` | `medium` |
| `eval_suite` | `security-regression` |
| `baseline_score` | `0.96` |
| `current_score` | `0.94` |
| `threshold` | `0.95` |
| `cost_usd` | `0.31` |
| `budget_usd` | `0.40` |
| `tests` | tests ciblés passés, full CI non lancée localement |
| `security` | seuil critique sous la limite |
| `policy` | `human` avant ouverture ou PR bloquée |

## 🛑 Exercice 3 - politique human-stop

Décide `auto`, `human` ou `deny` pour chaque cas.

| Cas | Contexte |
| --- | -------- |
| A | typo de documentation, tests non requis, coût faible, trace complète |
| B | changement de workflow CI, evals passées, coût sous budget |
| C | Coding Agent demande un token personnel pour pousser sur `main` |
| D | tests ciblés passés, eval critique sous seuil |
| E | PR body généré sans trace_id ni résultat de validation |

Justifie chaque décision en une phrase.

## 📦 Critère de réussite

Ton livrable est prêt si un mainteneur peut comprendre quoi reviewer, quelles preuves
existent, combien le run a coûté et pourquoi la Factory s'est arrêtée ou non.
