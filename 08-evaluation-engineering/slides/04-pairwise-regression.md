# 🔁 Pairwise evaluation et regression set

## 🎯 Objectif

Comparer deux versions sur les mêmes cas, puis protéger les comportements déjà validés.

## ⚔️ Pourquoi pairwise

Les scores absolus dérivent facilement : un judge peut noter plus sévèrement lundi que
mardi. En pairwise, on demande : pour le même cas, la sortie A ou B satisfait-elle mieux
l'expected et les constraints ?

## 🧪 Protocole minimal

1. Figer le dataset.
1. Exécuter la version courante et la version candidate.
1. Appliquer les checks déterministes aux deux sorties.
1. Comparer les sorties restantes avec la même rubric.
1. Agréger par segment : `task_type`, `task_class`, route, tags.
1. Bloquer toute régression sur les blockers.

## 🧱 Regression set

Un regression set contient :

- incidents déjà rencontrés ;
- bugs corrigés ;
- cas client importants ;
- comportements de sécurité ou de coût à préserver ;
- exemples où un modèle moins cher échouait malgré un bon score moyen.

Chaque cas doit indiquer pourquoi il est protégé. Sinon, il deviendra une archive morte.

## 📊 Lire le résultat

Une version candidate peut être meilleure en moyenne et quand même non publiable :

| Segment | Résultat | Décision |
| ------- | -------- | -------- |
| `simple` | +8 % qualité, coût stable | Bon signal |
| `medium` | +2 % qualité, +15 % coût | À discuter |
| `regression` | 1 cas bloqué | Publication bloquée |
| `security-adjacent` | Evidence insuffisante | Revue humaine |

## ✅ Critère de passage

La candidate gagne seulement si elle améliore les segments ciblés **et** préserve tous les
cas protégés.
