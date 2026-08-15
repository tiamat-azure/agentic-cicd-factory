# 🧪 10.2 - Déclencher les bonnes evals

## 🎯 Le problème

Tout relancer à chaque commit coûte trop cher. Ne rien relancer sur les prompts, tools ou
policies est trop risqué. La solution est une matrice de déclenchement.

## 🗺️ Matrice de déclenchement

| Changement | Evals minimales | Signal de blocage |
| ---------- | --------------- | ----------------- |
| Prompt | intent, instruction following, safety, regression | score critique sous seuil |
| Tool schema | sélection de tool, validation, erreurs | appel invalide accepté |
| Tool implementation | idempotence, erreur transitoire, permission | effet de bord non autorisé |
| Route modèle | qualité par segment, coût, latence | coût par succès hors budget |
| Workflow | end-to-end, ordre des gates, rollback | approbation contournée |
| Policy | allow/deny matrix, escalation, audit | permission inversée sans justification |
| Dataset ou seuil | meta-eval, couverture, stabilité | baseline non comparable |

## 🧠 Règle de décision

Un changement déclenche l'eval qui mesure le risque qu'il introduit. Une modification de
prompt n'a pas besoin d'un test de syntaxe de workflow ; une modification de workflow doit
prouver que les gates critiques restent dans le bon ordre.

## 🧾 Baseline obligatoire

Une eval sans baseline ne sait pas dire si la nouvelle version est meilleure, stable ou en
régression. Chaque suite doit donc produire au moins :

- le score courant ;
- le score de référence ;
- la tolérance acceptée ;
- la décision `pass`, `block` ou `needs-human-approval`.
