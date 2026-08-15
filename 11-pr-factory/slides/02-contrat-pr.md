# 🧾 Contrat de PR automatique

## 🎯 Objectif

Une PR automatique doit réduire le travail du mainteneur, pas le déplacer dans une chasse
aux informations. Elle doit résumer le contexte et pointer vers les preuves.

## 🧩 Sections obligatoires

1. **Summary** : demande initiale, intention reformulée, résultat.
1. **Architecture / Design** : décisions, alternatives rejetées, zones touchées.
1. **Changes** : fichiers et types de changements.
1. **Validation** : tests/checks réellement exécutés et résultats.
1. **Evaluation** : suites, baseline, seuils, score actuel, delta.
1. **Cost and Traceability** : `run_id`, `trace_id`, modèles, tokens, coût, latence.
1. **Security and Governance** : sandbox, permissions, secrets, findings, policy decision.
1. **Human Review Required** : questions restantes et conditions avant merge.

## ✅ Bon résumé

```markdown
## 🧭 Summary
- User request: add a cost budget gate to the model router.
- Implemented: budget field, enforcement path, error message, regression tests.
- Limits: no pricing table change; uses the existing cost estimator.
```

Le résumé dit ce qui est fait, ce qui ne l'est pas et où vérifier.

## ❌ Mauvais résumé

```markdown
## 🧭 Summary
Done.
```

Ce résumé force le reviewer à reconstruire toute la trace. Il n'est pas acceptable pour
une PR générée par agent.

## 🔍 Validation honnête

Une validation honnête peut contenir un échec ou une absence de test, si elle l'explique :

```markdown
## ✅ Validation
- PASS: targeted unit tests for budget enforcement.
- NOT RUN: full CI, unavailable in local sandbox.
- FOLLOW-UP: required checks must pass before merge.
```

Ne pas exécuter un test est parfois normal. Ne pas le dire rend la PR trompeuse.
