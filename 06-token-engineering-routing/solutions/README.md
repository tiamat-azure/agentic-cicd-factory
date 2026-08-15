# ✅ Solutions - Model Router v0.6

Ces solutions sont des exemples, pas une vérité unique. Compare-les à tes réponses surtout
sur la justification des décisions.

## 📝 Solution 1 - Schéma de métriques

| Champ | Type | Exemple | Sens |
| ----- | ---- | ------- | ---- |
| `run_id` | string | `run-001` | corrélation du workflow |
| `workflow_node` | string | `PLAN` | étape responsable |
| `task_type` | string | `plan` | regroupement fonctionnel |
| `task_class` | string | `medium` | résultat du classifier |
| `route` | string | `local-large` | profil demandé au gateway |
| `model` | string | `gateway:local-large` | modèle réellement appelé |
| `input_tokens` | number | `12400` | contexte envoyé |
| `output_tokens` | number | `1800` | réponse générée |
| `cached_tokens` | number | `6000` | contexte réutilisé ou cacheable |
| `tool_calls` | number | `3` | actions externes demandées |
| `iterations` | number | `2` | tours agentiques consommés |
| `latency_ms` | number | `9200` | durée mesurée |
| `cost_usd` | number | `0.018` | coût estimé |
| `success` | boolean | `true` | succès métier vérifié |
| `failure_reason` | string/null | `null` | raison qualifiée en cas d'échec |
| `retry_count` | number | `0` | retries consommés |
| `fallback_count` | number | `0` | escalades consommées |

Ce schéma suffit pour le chapitre 07 : il peut devenir un span ou un événement sans
dépendre d'un outil précis.

## 🧾 Solution 2 - Budgets par node

Exemple raisonnable :

```yaml
ANALYZE:
  agent:
    max_iterations: 3
    max_tool_calls: 8
  tokens:
    max_input: 30000
    max_output: 4000
  cost:
    max_run_usd: 0.12
  retry:
    max_attempts: 1

IMPLEMENT:
  agent:
    max_iterations: 6
    max_tool_calls: 12
  tokens:
    max_input: 25000
    max_output: 6000
  cost:
    max_run_usd: 0.20
  retry:
    max_attempts: 1

REVIEW:
  agent:
    max_iterations: 4
    max_tool_calls: 6
  tokens:
    max_input: 35000
    max_output: 5000
  cost:
    max_run_usd: 0.25
  retry:
    max_attempts: 1
```

Justification : `ANALYZE` lit beaucoup mais agit peu ; `IMPLEMENT` peut appeler plus de
tools mais doit rester borné ; `REVIEW` mérite plus de contexte car un faux négatif peut
coûter cher.

## 🔀 Solution 3 - Classifier et router

| # | Classe | Route | Fallback | Raison |
| - | ------ | ----- | -------- | ------ |
| 1 | `simple` | `local-small` | `local-large` | entrée courte, sortie vérifiable |
| 2 | `medium` | `local-large` | `cloud-frontier` | plusieurs fichiers et plan structuré |
| 3 | `complex` | `cloud-frontier` | humain | sécurité, coût d'erreur élevé |
| 4 | `simple` | `local-small` | `local-large` | synthèse à partir d'un diff validé |
| 5 | `complex` | `cloud-frontier` | humain | intermittence CI, incertitude forte |

Le point important : le fallback n'est pas toujours "modèle plus gros". Pour sécurité ou
ambiguïté, l'arrêt humain peut être le meilleur fallback.

## 💸 Solution 4 - Coût par tâche réussie

Coût total : `0,02 + 0,02 + 0,08 + 0,02 + 0,09 = 0,23`.

Succès : 3.

```text
cost_per_success = 0,23 / 3 = 0,0767
```

La moyenne par run est `0,23 / 5 = 0,046`. Elle semble meilleure, mais elle cache les deux
échecs. Pour piloter une Factory, le coût utile est celui des tâches qui atteignent le
résultat attendu.

## 🚦 Critère de sortie

Une solution est prête si elle rend ces décisions auditables :

- le classifier explique la classe ;
- le routeur explique le profil ;
- les budgets expliquent les arrêts ;
- retries et fallback sont bornés ;
- le coût par succès inclut les échecs.
