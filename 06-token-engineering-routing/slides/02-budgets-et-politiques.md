# 🧾 Budgets et policy gates

## 🎯 Idée clé

Un budget n'est pas un conseil donné au prompt. C'est une limite appliquée par le runtime.
Le modèle peut demander plus de contexte, plus d'itérations ou plus de tools ; la Factory
doit savoir refuser.

## 📐 Budget minimal

```yaml
agent:
  max_iterations: 8
  max_tool_calls: 20

tokens:
  max_input: 30000
  max_output: 8000

cost:
  max_run_usd: 0.25

retry:
  max_attempts: 2
```

Ces valeurs ne sont pas universelles. Elles servent de point de départ pour raisonner :
chaque node du workflow peut avoir un budget différent.

## 🧩 Budgets par node

| Node | Budget typique | Raison |
| ---- | -------------- | ------ |
| `ANALYZE` | contexte élevé, peu de tools | comprendre la demande et le repo |
| `PLAN` | sortie structurée, retries faibles | éviter des plans instables |
| `IMPLEMENT` | tools bornés, itérations bornées | empêcher les boucles de modification |
| `TEST` | coût modèle faible | exécuter surtout des validations déterministes |
| `REVIEW` | modèle plus fort si risque élevé | détecter les erreurs coûteuses |

Le budget suit la responsabilité du node, pas la préférence du modèle.

## 🚦 Policy gates

Un budget dépassé doit produire un statut lisible :

- `budget_exhausted:max_iterations` ;
- `budget_exhausted:max_tool_calls` ;
- `budget_exhausted:max_input` ;
- `budget_exhausted:max_run_usd`.

Ces statuts deviennent des gates CI/CD : on peut bloquer, demander une validation humaine,
ou réduire le scope de la tâche.

## 🔒 Ce que le prompt ne garantit pas

Écrire "sois concis" ou "n'appelle pas trop de tools" aide parfois, mais ne remplace pas :

- un compteur d'itérations ;
- une estimation de coût avant appel ;
- une limite de contexte ;
- un refus runtime quand un tool dépasse les permissions ;
- une trace expliquant pourquoi le run s'est arrêté.

## 🧠 Discipline de conception

Avant d'optimiser, pose trois questions :

1. Quelle limite protège la qualité ?
1. Quelle limite protège le coût ?
1. Quelle limite protège la sécurité ou la reprise ?

Un bon budget rend le système prévisible sans rendre le modèle inutile.
