# 🔑 Solutions - PR Factory v1.1

## 🧩 Exercice 1 - contrat de chaîne

| Étape | Sortie attendue | Décision |
| ----- | --------------- | -------- |
| Requirement | critère : refuser ou bloquer si eval sécurité critique < seuil | `auto` si la demande est claire |
| Architecture | plan : brancher la décision d'eval sécurité dans le final gate PR | `human` si le workflow de sécurité est critique dans l'organisation |
| Policy pre-check | autorisation de modifier policy/eval gate, pas de secret | `human` par défaut pour changement de policy |
| Coding | diff limité à la règle de gate et aux tests associés | `auto` après approbation du plan |
| Test | cas seuil au-dessus, seuil en-dessous, absence de résultat | `auto` si tests passent |
| Review | vérifie que l'échec critique ne peut pas être masqué | `auto` ou `human` selon criticité |
| Security | confirme que `deny` reste prioritaire sur score qualité | `auto` si aucun risque nouveau |
| Evaluation | suite sécurité avec baseline, seuil et delta | `human` si le seuil critique échoue |
| PR Composer | PR résumant décision, preuves et arrêt humain | `human-before-open` si la policy a changé |

## 🧾 Exercice 2 - PR body possible

```markdown
## 🧭 Summary
- Added a PR gate for critical security eval failures.
- The run detected that the current score is below the configured threshold.
- The PR must not be treated as automatically mergeable.

## ✅ Validation
- PASS: targeted tests for the new security gate.
- NOT RUN: full CI locally; required checks must pass before merge.

## 📊 Evaluation
- Suite: security-regression
- Baseline: 0.96
- Current: 0.94
- Threshold: 0.95
- Decision: needs-human-approval because the critical threshold is not met.

## 💸 Cost and Traceability
- run_id: run-pr-117
- task_class: medium
- cost_usd: 0.31 / budget_usd: 0.40

## 🔐 Security and Governance
- Security result is below threshold.
- Policy decision: human before opening, or open only as explicitly blocked.

## 👤 Human Review Required
- Decide whether the threshold failure is a true regression or an accepted exception.
- Do not merge until the security gate is green or an approved exception exists.
```

## 🛑 Exercice 3 - décisions

| Cas | Décision | Justification |
| --- | -------- | ------------- |
| A | `auto` | scope faible, pas de validation utile manquante, trace complète |
| B | `human` | un workflow CI est une zone sensible même si les evals passent |
| C | `deny` | token personnel et push sur `main` violent la gouvernance |
| D | `human` ou `deny` | une eval critique sous seuil ne peut pas passer silencieusement |
| E | `human` | une PR sans trace ni validation est impossible à auditer |

## 📌 À retenir

Le Gate 5 n'est pas "l'agent ouvre une PR". C'est "l'agent ouvre une PR que l'humain peut
reviewer efficacement, avec preuves, coûts et arrêts explicites".
