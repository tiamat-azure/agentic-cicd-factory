# 🧩 Exercices - Evaluation Framework v0.8

## 🎯 Objectif

Produire un framework d'évaluation sur papier suffisamment précis pour être implémenté
ensuite dans la Factory sans changer de vocabulaire.

## 🧪 Exercice 1 - Dataset versionné

Crée 5 cas d'eval pour le workflow `REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW -> PR`.

Chaque cas doit contenir :

- `case_id` ;
- `task_type` et `task_class` ;
- `task` ;
- `expected` ;
- `constraints` ;
- `trace_requirements` ;
- `tags`.

Inclure au moins :

- 1 cas `simple` ;
- 1 cas `medium` ;
- 1 cas `complex` ;
- 1 cas de coût ou latence ;
- 1 cas marqué `regression`.

## ✅ Exercice 2 - Checks avant judge

Pour chaque cas, liste les checks déterministes ou code-based qui doivent passer avant un
LLM-as-judge.

Exemples de checks attendus :

- fichiers modifiés autorisés ;
- sortie structurée valide ;
- tests existants verts ;
- `max_tool_calls` respecté ;
- `required_spans` présents ;
- `failure_reason` explicite en cas d'échec.

## ⚖️ Exercice 3 - Pairwise et thresholds

Compare une version A et une version B fictives de la Factory.

À produire :

- une table pairwise par `case_id` ;
- une rubric LLM-as-judge pour les cas non déterministes ;
- une liste de blockers ;
- une décision finale : `pass`, `block` ou `needs_human_review` ;
- une phrase expliquant le lien avec la gouvernance du chapitre 09.

## 📦 Livrable attendu

Un document court nommé librement dans ton espace de travail contenant :

1. le dataset ;
1. les checks ;
1. la rubric ;
1. les résultats pairwise ;
1. la décision de gate.

Ne cherche pas à écrire un runner complet. Le but est de stabiliser le contrat
d'évaluation.
