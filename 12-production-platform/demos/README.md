# 🎬 Demos - chapitre 12

Ces demos sont des lectures guidées, pas du code à exécuter. Elles servent à entraîner le
raisonnement de production : diagnostiquer, décider, documenter.

| Demo | Situation | Question posée |
| ---- | --------- | -------------- |
| 1 | Une équipe lance 80 demandes en 10 minutes | Comment éviter qu'un tenant sature la plateforme ? |
| 2 | Le modèle cloud principal devient indisponible | Que fait le Model Gateway sans casser les budgets ? |
| 3 | Une PR générée passe les tests mais échoue une eval sécurité | Quelle décision prend la plateforme ? |

______________________________________________________________________

## 🧺 Demo 1 - Backlog par tenant

Contexte : `team-a` envoie 80 demandes de refactor. `team-b` a 3 corrections urgentes. La
file `implementation` grossit, la latence p95 double et le coût horaire dépasse le budget.

Décision saine :

1. appliquer un quota de concurrence par tenant ;
1. laisser `team-b` consommer sa capacité réservée ;
1. ralentir les nouvelles demandes `team-a` ;
1. finir les workflows déjà proches de la PR ;
1. alerter avec coût, backlog et ETA ;
1. garder les traces pour réviser le capacity planning.

Piège : ajouter plus de workers sans quota peut augmenter le coût et la pression sur les
tools, tout en dégradant les deux équipes.

______________________________________________________________________

## 🔀 Demo 2 - Failover modèle

Contexte : le profil `cloud-frontier` renvoie des erreurs transitoires. Les tâches simples
peuvent passer sur `local-small`, les tâches medium sur `local-large`, les tâches complexes
nécessitent une validation humaine.

Décision saine :

| Classe | Action |
| ------ | ------ |
| `simple` | router vers `local-small` si les evals de compatibilité sont vertes |
| `medium` | router vers `local-large`, réduire budget et surveiller qualité |
| `complex` | suspendre l'automatisation ou demander validation humaine |

Piège : basculer toutes les tâches vers un modèle moins capable peut faire baisser le coût
par appel et augmenter le coût par PR utile.

______________________________________________________________________

## 🧪 Demo 3 - Eval sécurité rouge

Contexte : une PR générée compile, les tests passent, mais l'eval sécurité détecte une
régression de permissions sur le Policy Engine.

Décision saine :

1. bloquer la progression automatique ;
1. marquer la PR comme nécessitant review sécurité ;
1. attacher trace, résultat d'eval et diff de policy ;
1. empêcher le merge tant que le scénario rouge n'est pas résolu ;
1. ajouter le cas au jeu de régression si c'est un nouveau pattern.

Piège : considérer les tests verts comme supérieurs aux evals. En production, un gate rouge
explicable bloque tant qu'il n'est pas explicitement levé.
