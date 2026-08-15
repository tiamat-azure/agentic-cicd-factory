# ✅ Solutions - Factory v1.0

Ces solutions sont des exemples. Compare-les à tes réponses surtout sur la clarté des
seuils, des déclencheurs et des décisions.

## 📝 Solution 1 - Matrice de déclenchement

| # | Evals | Risque | Décision si échec |
| - | ----- | ------ | ----------------- |
| 1 | plan validity, instruction following, regression | plans moins fiables | `block` si seuil critique raté |
| 2 | tool schema, validation, error handling | arguments invalides acceptés | `block` si validation contournée |
| 3 | quality by segment, cost, latency, fallback | coût/qualité différents | `block` si coût par succès hors budget |
| 4 | end-to-end, human approval, rollback | action avant validation | `block` si gate contourné |
| 5 | meta-eval, couverture, stabilité | seuil trop permissif | `needs-human-approval` avec justification |

Le point important : modifier un seuil est aussi un changement de comportement. Il doit
être reviewé comme un changement de code.

## 🚦 Solution 2 - Règles de blocage

Exemple de contrat :

| Règle | Décision |
| ----- | -------- |
| Toute eval critique sous son seuil absolu | `block` |
| Régression supérieure à 3 points sur une suite obligatoire | `block` |
| Coût par tâche réussie supérieur au budget du segment | `block` |
| Permission critique passée de `deny` à `allow` | `needs-human-approval` ou `block` |
| Trace sans version de prompt, modèle, tools ou commit | `block` |

Une équipe peut choisir d'autres seuils, mais ils doivent être explicites avant le run.

## 🧾 Solution 3 - Décision de pipeline

La pipeline bloque.

Raisons :

- `tool_safety` vaut `0.79`, sous le seuil `0.80` ;
- la trace ne contient pas la version du prompt, donc la décision n'est pas auditable ;
- le coût et `plan_validity` sont acceptables, mais ils ne compensent pas un gate critique
  en échec.

Une approbation humaine pourrait seulement créer une exception limitée si la policy de
l'organisation l'autorise explicitement. Elle ne doit pas masquer la trace incomplète.

## 🌉 Solution 4 - Artefacts pour une PR automatique

Une PR générée par agent devrait joindre au minimum :

- demande initiale et interprétation retenue ;
- plan exécuté et limites connues ;
- diff ou résumé des fichiers modifiés ;
- matrice des changements détectés ;
- suites d'evals lancées, scores, baseline et cas échoués ;
- coût par succès et budget consommé ;
- décisions de policy `allow` / `deny` / `escalate` ;
- exceptions humaines avec propriétaire, raison, portée et expiration ;
- lien vers les traces de run.

## 🚦 Critère de sortie

Une solution est prête si elle rend la livraison prédictible : mêmes changements, mêmes
evals, mêmes règles, même décision. Sans cette stabilité, le chapitre 11 ne pourrait pas
faire confiance à une PR automatique.
