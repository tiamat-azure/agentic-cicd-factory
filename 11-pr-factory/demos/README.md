# 🧪 Démo commentée - une PR automatique de bout en bout

## 🎯 Objectif

Cette démo est une étude de cas textuelle. Elle ne dépend d'aucun outil spécifique : elle
montre les artefacts que la Factory doit produire, quelle que soit son implémentation.

## 📨 Demande utilisateur

> Ajoute un garde-fou qui bloque une tâche agentique si son coût estimé dépasse le budget
> du segment `medium`, et rends la raison visible dans la PR.

## 🔁 Trace synthétique

| Étape | Sortie utile | Décision |
| ----- | ------------ | -------- |
| Requirement | critère : dépassement coût -> blocage explicite | `auto` |
| Architecture | toucher budget policy, router, tests de dépassement | `auto` |
| Policy pre-check | fichiers autorisés, pas de secret, pas de déploiement | `auto` |
| Coding | diff limité au budget et aux tests | `auto` |
| Test | tests ciblés passés ; full CI requis avant merge | `human` pour merge |
| Review | pas de régression bloquante détectée | `auto` |
| Security | permissions inchangées, aucun secret | `auto` |
| Evaluation | score stable, coût du run sous budget | `auto` |
| PR Composer | PR ouverte avec reviewer mainteneur | `auto-open` |

## 🧾 PR body attendu

```markdown
## 🧭 Summary
- Added an explicit cost-budget gate for `medium` tasks.
- Budget failures now surface as a clear run outcome and PR risk note.
- Scope excluded pricing-table changes.

## 🏗️ Architecture / Design
- Kept routing model-agnostic: the router consumes a segment budget, not a provider name.
- Reused the existing run metrics contract from chapter 06.

## 🧩 Changes
- Code: budget decision path.
- Tests: budget-exceeded scenario.
- Docs/PR: reason included in generated summary.

## ✅ Validation
- PASS: targeted budget enforcement tests.
- NOT RUN: full CI in this local exercise; required checks must pass before merge.

## 📊 Evaluation
- Suite: routing-budget-regression
- Baseline: 0.91 / Current: 0.92 / Threshold: 0.90 / Delta: +0.01
- Decision: pass

## 💸 Cost and Traceability
- run_id: run-2026-08-15-pr-factory-demo
- task_class: medium
- route: local-large -> no fallback
- tokens: input 18400, output 2100, cached 6200
- tool_calls: 9, iterations: 4, latency_ms: 128000, cost_usd: 0.18
- cost_per_success: 0.18

## 🔐 Security and Governance
- Sandbox: branch write only, no secrets, network restricted to repository services.
- Policy decision: auto-open PR, human review required before merge.
- Residual risk: budget numbers depend on the existing estimator.

## 👤 Human Review Required
- Confirm budget threshold matches product expectations.
- Confirm required CI checks pass before merge.
```

## 🔍 Lecture pédagogique

La PR est ouverte automatiquement, mais elle ne demande pas un merge automatique. Le merge
reste protégé par les checks requis et par le reviewer humain, car la politique distingue
`open PR` de `merge PR`.
