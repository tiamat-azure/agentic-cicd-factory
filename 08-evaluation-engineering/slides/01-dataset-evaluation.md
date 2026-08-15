# 📚 Construire un dataset d'évaluation

## 🎯 Objectif

Un dataset d'eval décrit les tâches que la Factory doit réussir de manière répétable. Il
sert à comparer les versions, pas à impressionner pendant une démo.

## 🧱 Un cas d'eval n'est pas seulement un prompt

Un prompt seul ne dit pas ce qui est attendu. Un cas utile contient :

| Élément | Pourquoi c'est nécessaire |
| ------- | ------------------------- |
| `case_id` | Suivre les régressions dans le temps |
| `task` | Décrire la demande utilisateur |
| `expected` | Définir le résultat observable attendu |
| `constraints` | Fixer les interdits, budgets et formats |
| `tags` | Segmenter les scores : sécurité, coût, doc, code, regression |
| `trace_requirements` | Vérifier que la trace raconte bien le run |
| `metric_limits` | Relier l'eval aux budgets du chapitre 06 |

## 🔭 Partir des traces du chapitre 07

Les meilleurs cas viennent de runs réels : succès importants, échecs, incidents,
régressions corrigées, demandes ambiguës. Pour chaque trace, on extrait :

- la tâche initiale ;
- les spans attendus (`analyze`, `plan`, `implement`, `test`, `review`) ;
- les métriques : tokens, latence, coût, tool calls, retries ;
- le résultat métier ;
- la raison d'échec si le run a été bloqué.

## 🧩 Granularité

Un bon dataset contient plusieurs familles :

- **golden cases** : comportements essentiels que toute version doit préserver ;
- **regression cases** : bugs déjà corrigés, jamais autorisés à revenir ;
- **stress cases** : budgets, latence, contexte long, retries ;
- **quality cases** : tâches où le résultat est partiellement subjectif ;
- **security-adjacent cases** : consignes interdites, fichiers sensibles, escalade humaine.

## ✅ Critère de qualité

Un cas est prêt quand une autre personne peut lire le fichier, exécuter la Factory, puis
expliquer pourquoi le résultat est `pass`, `block` ou `needs_human_review` sans demander
l'intention originale de l'auteur.
