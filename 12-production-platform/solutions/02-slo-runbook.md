# 📊 Solution 2 - SLO, budgets et modes dégradés

## 🎯 SLO proposés

| Dimension | SLO | Seuil pilote | Action si rouge |
| --------- | --- | ------------ | --------------- |
| Qualité | PR utiles / PR ouvertes | >= 70 % | réduire automatisation, analyser evals rouges |
| Latence | p95 demande -> PR prête | <= 2 h | inspecter backlog, tools lents, workers |
| Coût | coût par PR utile | <= budget tenant | limiter tâches non urgentes, revoir routing |
| Sécurité | régression critique eval sécurité | 0 | bloquer merge et demander review sécurité |

## 💸 Budgets par tenant

| Budget | Exemple | Action |
| ------ | ------- | ------ |
| coût journalier | 50 USD / jour | passer les nouvelles demandes en validation |
| concurrence | 5 workflows actifs | mettre en attente sans bloquer les autres tenants |

## 🚦 Backpressure

Si le backlog `implementation` d'un tenant dépasse 3 fois sa concurrence autorisée, les
nouvelles demandes de ce tenant restent en `intake_waiting`. Les workflows déjà en
`verification` continuent pour éviter de perdre du travail presque terminé.

## 🔀 Failover modèle

| Classe | Route normale | Incident fournisseur principal |
| ------ | ------------- | ------------------------------ |
| `simple` | `local-small` | inchangé si evals vertes |
| `medium` | `local-large` | rester local, budget réduit, alerte qualité |
| `complex` | `cloud-frontier` | suspendre ou demander validation humaine |

## 🧯 Mode dégradé evals instables

Quand le taux de régression eval dépasse le seuil :

1. bloquer merge et déploiement automatiques ;
1. autoriser analyse, plan et PR brouillon ;
1. exiger review humaine ;
1. rejouer les traces récentes ;
1. corriger le jeu d'evals ou la policy avant réactivation.

## 🚨 Alerte actionnable

Alerte : `cost_per_useful_pr` augmente de 50 % sur 24 h pour un tenant.

Action : inspecter retries, failovers, tâches échouées, modèle choisi et taux de PR utiles.
Si l'augmentation vient de retries non idempotents ou d'evals rouges, suspendre la route
concernée.
