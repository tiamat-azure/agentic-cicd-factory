# 🧑‍⚖️ Placer l'humain dans la boucle

## 🎯 Idée clé

Human-in-the-loop ne signifie pas "tout faire valider". Cela signifie que les décisions à
fort impact restent humaines, tandis que les tâches faibles risques restent automatisées.

## 🚦 Trois décisions possibles

| Décision | Sens | Exemple |
| -------- | ---- | ------- |
| `auto` | l'agent peut continuer | ouvrir une PR sur branche dédiée après evals vertes |
| `human` | l'agent prépare, l'humain décide | merger une PR, changer une policy sensible |
| `deny` | l'action est interdite | lire un secret de production, pousser sur `main` |

## 🧭 Critères de passage humain

Une validation humaine devient obligatoire si au moins un critère est vrai :

- impact production ou données sensibles ;
- changement de policy, prompt système, tool critique ou workflow de déploiement ;
- score d'eval sous le seuil ;
- alerte sécurité ou incertitude élevée ;
- action irréversible ou difficile à auditer.

## ✅ Bon comportement agentique

Quand une action passe en `human`, l'agent ne doit pas se bloquer en silence. Il doit
préparer une demande exploitable : résumé, diff, risques, evals, logs pertinents et option
recommandée.

L'humain ne doit pas refaire le travail de l'agent ; il doit décider avec assez de contexte.
