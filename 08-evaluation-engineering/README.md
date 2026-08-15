# 🧪 08 - Evaluation Engineering

> Livrable : **Evaluation Framework v0.8** - un cadre d'évaluation versionné qui relie
> datasets, traces, scores, comparaisons pairwise et seuils de blocage pour empêcher les
> régressions de la Factory.

## 🎯 Objectifs pédagogiques

- Construire un dataset d'évaluation utile : tâche, contexte, résultat attendu,
  contraintes, tags, trace de référence et métriques observables.
- Distinguer eval déterministe, eval code-based, LLM-as-judge et pairwise evaluation.
- Transformer les traces du chapitre 07 en preuves : tokens, latence, coût, tool calls,
  erreurs, route modèle, succès et `failure_reason`.
- Composer un score global sans cacher les échecs critiques.
- Maintenir un regression set qui bloque une évolution dès qu'un comportement validé se
  dégrade.
- Préparer le chapitre 09 : les seuils d'eval deviennent des policies de gouvernance.

## ✅ Prérequis

- Chapitre 07 (Observability v0.7 : traces corrélées, spans, coût, latence, tokens).
- Comprendre les budgets et le routing du chapitre 06.
- Savoir lire un résultat de test ou une trace de run.
- Durée estimée : **3 h** (1 h théorie + 45 min lecture d'exemples + 1 h exercices +
  15 min synthèse).

## 🚪 Gate du chapitre

> **Gate 4 (partie 3/3)** : tu dois pouvoir comparer deux versions de la Factory sur un
> même dataset, prouver laquelle est meilleure par segment, et bloquer automatiquement une
> version qui régresse sur un critère non négociable.

## 🧭 Parcours pas à pas

| Étape | Support | Ce que tu fais |
| ----- | ------- | --------------- |
| 1 | [`slides/01-dataset-evaluation.md`](slides/01-dataset-evaluation.md) | Lire : transformer des traces en dataset d'eval |
| 2 | [`slides/02-evals-deterministes-code.md`](slides/02-evals-deterministes-code.md) | Lire : vérifier ce qui peut l'être sans LLM |
| 3 | [`slides/03-llm-as-judge.md`](slides/03-llm-as-judge.md) | Lire : juger la qualité avec une grille explicite |
| 4 | [`slides/04-pairwise-regression.md`](slides/04-pairwise-regression.md) | Lire : comparer A/B et protéger le regression set |
| 5 | [`slides/05-seuils-gates.md`](slides/05-seuils-gates.md) | Lire : score global, blockers et passage vers la governance |
| 6 | [`demos/README.md`](demos/README.md) | Parcourir : exemples de dataset, résultats et décision de gate |
| 7 | [`exercices/README.md`](exercices/README.md) | Faire les 3 exercices -> **Evaluation Framework v0.8** |
| 8 | [`solutions/README.md`](solutions/README.md) | Comparer après tentative |

## 📚 Plan théorique

1. Pourquoi une eval agentique part d'un **dataset**, pas d'une impression de qualité.
1. Anatomie d'un cas d'eval : `case_id`, `task`, `expected`, `constraints`, `tags`,
   `trace_requirements`, `metric_limits`.
1. Evals déterministes : égalité exacte, schéma JSON, présence d'artefacts, absence de
   fichiers interdits.
1. Evals code-based : tests, parseurs, linters existants, calculs de coût et de latence.
1. LLM-as-judge : utile pour la qualité sémantique, dangereux sans rubric ni evidence.
1. Pairwise evaluation : comparer deux sorties sur la même tâche avant de déclarer un
   gagnant.
1. Regression set : conserver les cas validés, les incidents et les bugs corrigés.
1. Blocking thresholds : séparer les métriques qui scorent de celles qui arrêtent.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : une eval est un contrat de données et de décision ; elle peut
  être exécutée par n'importe quel runner.
- **Model-agnostic** : les résultats comparent des comportements observés, pas des marques
  de modèles. Le judge passe lui aussi par le Model Gateway.
- **Eval-first** : une amélioration n'est acceptée que si elle gagne sur un dataset
  versionné sans dégrader les blockers.

## 🔁 Pont avec les chapitres voisins

Le chapitre 07 explique **ce qui s'est passé** dans un run. Le chapitre 08 répond :
**est-ce assez bon pour continuer ?**

Le chapitre 09 utilisera cette réponse comme entrée de gouvernance : une policy ne doit
pas seulement dire « coût trop élevé » ou « risque sécurité » ; elle doit pointer vers un
cas d'eval, une trace et un seuil explicite.

```text
Trace v0.7 ──► Eval case ──► Scores ──► Gate decision ──► Policy v0.9
 run_id        expected      quality     pass / block      approve / escalate
 spans         constraints   cost        reason            audit trail
 tokens        tags          latency
```

## 📏 Vocabulaire d'évaluation

| Champ | Source | Rôle dans l'eval |
| ----- | ------ | ---------------- |
| `case_id` | dataset | Identifiant stable du scénario évalué |
| `run_id` | trace | Lien vers l'exécution observée |
| `task_type` | trace / dataset | Segment : analyse, plan, code, review, PR |
| `task_class` | routeur | Segment de complexité : `simple`, `medium`, `complex` |
| `route` | routeur | Profil choisi : `local-small`, `local-large`, `cloud-frontier` |
| `expected` | dataset | Résultat fonctionnel attendu |
| `constraints` | dataset | Interdits, formats, fichiers autorisés, budgets locaux |
| `judge_rubric` | dataset | Grille utilisée si la qualité n'est pas déterministe |
| `score` | runner d'eval | Score agrégé, jamais seul critère de décision |
| `blockers` | runner d'eval | Raisons non négociables : régression, test rouge, budget dépassé |
| `failure_reason` | trace / runner | Cause explicable : `quality_gate_failed`, `budget_exhausted`, ... |

## 🧾 Contrat minimal d'un cas d'eval

Un cas d'eval doit être lisible sans connaître le code interne de la Factory.

```yaml
case_id: fix-readme-link-001
task_type: code
task_class: simple
task: "Corriger un lien relatif cassé dans le README du module billing."
expected:
  files_changed:
    - "billing/README.md"
  must_contain:
    - "../docs/api.md"
constraints:
  forbidden_paths:
    - "site/"
  max_tool_calls: 6
  max_cost_usd: 0.05
trace_requirements:
  required_spans:
    - "analyze"
    - "edit"
    - "verify"
tags:
  - regression
  - documentation
  - low-risk
```

La règle : **si l'expected est déterministe, le judge LLM ne décide pas à sa place**.

## 🛑 Seuils de blocage recommandés

| Seuil | Décision |
| ----- | -------- |
| Test ou vérification déterministe rouge | Bloquer |
| Régression sur un cas marqué `regression` | Bloquer |
| Budget `max_cost_usd`, tokens, latence ou tool calls dépassé | Bloquer ou escalader selon policy |
| Judge score sous le minimum avec evidence insuffisante | Bloquer et demander revue humaine |
| Amélioration moyenne mais échec sur un segment critique | Bloquer le rollout global |

Un score moyen ne compense jamais un blocker. C'est le pont naturel vers le chapitre 09 :
les policies rendront ces décisions auditables et opposables.

## 📦 Livrable

**Evaluation Framework v0.8** - une spécification complète contenant :

- un format de dataset d'eval ;
- au moins 5 cas couvrant `simple`, `medium`, `complex`, coût, latence et qualité ;
- des checks déterministes avant tout judge LLM ;
- une rubric LLM-as-judge avec evidence obligatoire ;
- une comparaison pairwise entre deux versions ;
- un regression set versionné ;
- une matrice de thresholds qui produit `pass`, `block` ou `needs_human_review`.

## 🔗 Ressources

- [`../06-token-engineering-routing/`](../06-token-engineering-routing/) - budgets,
  routing, coût par tâche réussie.
- [`../07-observability-tracing/`](../07-observability-tracing/) - traces, spans,
  corrélation, coût, latence et tokens.
- OpenAI Evals - concepts de datasets, graders et régressions.
- LangChain Academy - Agent Observability & Evaluation.
- Humanloop - guides sur LLM evaluation et LLM-as-judge.

## 📝 Auto-évaluation

Tu peux passer au chapitre 09 quand tu réponds sans hésiter :

1. Quelles informations minimales doit contenir un cas d'eval agentique ?
1. Pourquoi faut-il exécuter les checks déterministes avant un judge LLM ?
1. Quand une pairwise evaluation est-elle plus fiable qu'un score absolu ?
1. Comment transformer une trace du chapitre 07 en preuve d'eval ?
1. Quelle différence fais-tu entre un mauvais score et un blocker ?
