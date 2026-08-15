# 🧪 Slides - Evaluation Engineering

## 🧭 Parcours de lecture

1. [`01-dataset-evaluation.md`](01-dataset-evaluation.md) - dataset, expected,
   contraintes et tags.
1. [`02-evals-deterministes-code.md`](02-evals-deterministes-code.md) - checks sans LLM
   et evals code-based.
1. [`03-llm-as-judge.md`](03-llm-as-judge.md) - rubric, evidence et limites du judge.
1. [`04-pairwise-regression.md`](04-pairwise-regression.md) - comparaison A/B et
   regression set.
1. [`05-seuils-gates.md`](05-seuils-gates.md) - thresholds, blockers et governance.

## 🎯 Fil conducteur

À la fin des slides, une évolution de la Factory n'est plus validée parce qu'elle « semble
meilleure ». Elle est validée parce qu'elle passe un dataset versionné, produit une trace
lisible, respecte ses budgets et ne régresse pas sur les cas critiques.
