# 📏 Instrumenter avant d'optimiser

## 🎯 Idée clé

On ne peut pas optimiser une Factory agentic avec une impression générale du type "ce
modèle coûte moins cher". Il faut mesurer chaque run avec le même vocabulaire, quel que
soit le modèle appelé.

## 🧾 Événement minimal de run

Un événement de run doit être assez petit pour être produit partout, mais assez riche pour
expliquer un coût.

```json
{
  "run_id": "run-2026-06-001",
  "task_type": "plan",
  "route": "local-large",
  "model": "gateway:local-large",
  "input_tokens": 12400,
  "output_tokens": 1800,
  "cached_tokens": 6000,
  "tool_calls": 3,
  "iterations": 2,
  "latency_ms": 9200,
  "cost_usd": 0.018,
  "success": true,
  "failure_reason": null
}
```

Le nom du modèle réel peut varier selon l'environnement. Le routeur, lui, raisonne sur des
profils stables : `local-small`, `local-large`, `cloud-frontier`.

## 🧮 Tokens à distinguer

| Métrique | Question à laquelle elle répond |
| -------- | -------------------------------- |
| `input_tokens` | Combien de contexte a-t-on envoyé ? |
| `output_tokens` | Combien le modèle a-t-il généré ? |
| `cached_tokens` | Quelle part du contexte répétitif bénéficie du cache ? |
| `total_tokens` | Quelle charge brute le run impose-t-il ? |

Ne mélange pas ces métriques : réduire `output_tokens` n'a pas le même effet que réduire
un contexte d'entrée mal sélectionné.

## 🛠️ Tools et itérations

Les tokens ne suffisent pas. Un run peu coûteux en tokens peut être dangereux s'il appelle
20 tools ou boucle sans progresser.

À mesurer au même endroit :

- `tool_calls` : nombre total d'actions externes ;
- `iterations` : tours agentiques consommés ;
- `retry_count` : tentatives supplémentaires ;
- `fallback_count` : escalades vers un autre profil ;
- `budget_exhausted` : limite atteinte avant succès.

## ✅ Succès métier

`success: true` ne signifie pas seulement "pas d'exception". Pour la Factory, le succès
doit correspondre à une sortie vérifiée : plan valide, tests passés, review exploitable,
PR prête, etc.

Sans cette colonne, tu optimises le coût des runs terminés, pas le coût des tâches utiles.

## ⚠️ Anti-patterns

- Comparer deux modèles sans la même définition de succès.
- Compter seulement les tokens et ignorer retries, fallback et tool calls.
- Masquer un dépassement de budget comme une erreur générique.
- Mesurer uniquement les appels modèle, sans les relier au `run_id` du workflow.
