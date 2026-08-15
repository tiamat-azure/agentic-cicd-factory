# 🧪 Démos - Lire des traces et décider une route

Ces démos sont des traces commentées, pas du code à exécuter. Elles servent à apprendre le
raisonnement de routing avant d'automatiser quoi que ce soit.

## 🎯 Objectif

Pour chaque scénario, entraîne-toi à répondre dans cet ordre :

1. Quelle est la classe de tâche ?
1. Quel budget appliquer ?
1. Quelle route choisir via le Model Gateway ?
1. Quel retry est autorisé ?
1. Quel fallback est autorisé ?
1. Comment le run apparaîtra-t-il dans les traces du chapitre 07 ?

## 📏 Démo 1 - Run instrumenté

```json
{
  "run_id": "demo-001",
  "task_type": "review",
  "route": "local-large",
  "input_tokens": 18200,
  "output_tokens": 2400,
  "cached_tokens": 7200,
  "tool_calls": 4,
  "iterations": 3,
  "latency_ms": 14100,
  "cost_usd": 0.031,
  "success": false,
  "failure_reason": "quality_gate_failed",
  "retry_count": 1,
  "fallback_count": 0
}
```

Lecture : le run n'est pas "bon marché" s'il échoue. Le routeur doit décider si ce type de
review mérite un fallback vers `cloud-frontier` ou une clarification humaine.

## 🔀 Démo 2 - Décision de routing

Demande : "Résume les erreurs du dernier rapport de tests et propose l'étape suivante."

Décision attendue :

```json
{
  "task_class": "simple",
  "route": "local-small",
  "reason": "entrée courte, pas de modification, sortie textuelle vérifiable"
}
```

Fallback : `local-large` seulement si la sortie structurée demandée est invalide. Pas de
cloud par défaut.

## 🧾 Démo 3 - Budget par node

Node `IMPLEMENT` :

```yaml
agent:
  max_iterations: 6
  max_tool_calls: 12

tokens:
  max_input: 25000
  max_output: 6000

cost:
  max_run_usd: 0.20
```

Lecture : ce budget protège contre une boucle de modification. Si le patch ne converge pas,
le statut doit être `budget_exhausted:max_iterations`, pas un échec flou.

## 🔁 Démo 4 - Retry ou fallback

Erreur : sortie JSON invalide au premier appel, aucun tool non idempotent exécuté.

Décision : un retry est acceptable, avec un rappel du schéma attendu. Si le second essai
échoue, on ne boucle pas : fallback borné ou arrêt qualifié selon la criticité.

## 💸 Démo 5 - Coût par succès

Lot de 10 tâches `medium` :

| Route | Coût total | Succès | Coût par succès |
| ----- | ---------- | ------ | ---------------- |
| `local-large` seul | 0,18 USD | 6 | 0,030 USD |
| `local-large` puis fallback | 0,42 USD | 9 | 0,047 USD |
| `cloud-frontier` direct | 0,70 USD | 10 | 0,070 USD |

Lecture : la meilleure route dépend du seuil qualité attendu. Si 90 % de succès est
obligatoire, `local-large` seul ne suffit pas malgré son coût apparent.
