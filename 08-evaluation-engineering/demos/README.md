# 🧪 Demos - Lire une évaluation complète

## 🎯 Objectif

Ces demos sont des exemples commentés, sans runner imposé. Elles montrent les artefacts
qu'un framework d'évaluation doit produire avant d'être branché à une CI.

## 📚 Dataset minimal

```yaml
- case_id: doc-link-001
  task_type: code
  task_class: simple
  task: "Corriger le lien cassé vers la documentation API dans billing/README.md."
  expected:
    files_changed: ["billing/README.md"]
    must_contain: ["../docs/api.md"]
  constraints:
    forbidden_paths: ["site/"]
    max_tool_calls: 6
    max_cost_usd: 0.05
  trace_requirements:
    required_spans: ["analyze", "edit", "verify"]
  tags: ["documentation", "regression"]

- case_id: review-plan-002
  task_type: review
  task_class: medium
  task: "Comparer deux plans de correction et choisir le plus sûr."
  expected:
    decision_required: true
    must_discuss: ["tests", "rollback", "blast radius"]
  constraints:
    max_latency_ms: 90000
  judge_rubric:
    min_correctness: 4
    min_grounding: 4
  tags: ["quality", "pairwise"]
```

## 🔭 Résultat de run observé

```yaml
case_id: doc-link-001
run_id: run-2026-08-15-001
route: local-small
metrics:
  input_tokens: 4200
  output_tokens: 650
  tool_calls: 4
  latency_ms: 18000
  cost_usd: 0.012
checks:
  deterministic:
    files_changed: pass
    must_contain: pass
    forbidden_paths: pass
    required_spans: pass
  code_based:
    markdown_links: pass
blockers: []
decision: pass
```

## ⚖️ Exemple de judge avec evidence

```yaml
case_id: review-plan-002
judge_input:
  task: "Comparer deux plans de correction et choisir le plus sûr."
  expected_evidence:
    - "tests"
    - "rollback"
    - "blast radius"
  trace_excerpt:
    spans: ["analyze", "compare", "decide"]
judge_output:
  correctness: 4
  completeness: 5
  grounding: 4
  safety: pass
  rationale: >
    Le plan B est préféré car il ajoute un test de non-régression, limite le blast radius
    au module de routing et décrit un rollback explicite.
decision: pass
```

## 🔁 Exemple pairwise

| Case | Version A | Version B | Gagnant | Raison |
| ---- | --------- | --------- | ------- | ------ |
| `doc-link-001` | pass | pass | tie | Même correction, coût équivalent |
| `review-plan-002` | correctness 3 | correctness 4 | B | B cite rollback et tests |
| `routing-reg-003` | pass | block | A | B dépasse `max_cost_usd` |

Conclusion : B progresse sur la qualité de review, mais ne peut pas être promue tant que
`routing-reg-003` régresse.

## 🚦 Décision de gate

```yaml
gate_decision: block
summary:
  global_score_delta: "+3.2%"
  blockers:
    - case_id: routing-reg-003
      reason: "budget_exhausted"
      observed_cost_usd: 0.31
      max_cost_usd: 0.20
next_action: "corriger le routing ou demander une revue humaine"
```

Le score moyen est positif, mais la publication est bloquée : un regression case protégé a
échoué.
