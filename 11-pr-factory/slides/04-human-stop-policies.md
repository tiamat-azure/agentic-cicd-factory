# 🛑 Human-stop policies

## 🎯 Objectif

Le but n'est pas de supprimer l'humain. Le but est de l'appeler au moment où son jugement
ajoute de la sécurité, pas à chaque étape mécanique.

## 🔐 Trois décisions

| Décision | Sens |
| -------- | ---- |
| `auto` | la Factory peut continuer dans le sandbox et le budget prévus |
| `human` | la Factory s'arrête ou ouvre une PR explicitement bloquée pour review |
| `deny` | l'action est interdite, même avec un bon score de modèle |

## 🧱 Règles minimales

- `deny` pour secrets, tokens personnels, droits admin, merge direct ou déploiement non
  autorisé.
- `human` pour auth, policy, workflow critique, coût hors budget, validation incomplète ou
  demande ambiguë.
- `auto` seulement si le scope est clair, les fichiers sont autorisés, les checks passent
  et la trace est complète.

## ⚖️ Pourquoi pas tout en validation humaine ?

Tout mettre en `human` détruit la valeur de la Factory : le reviewer devient scheduler,
testeur et auditeur. Les arrêts doivent être proportionnés au risque et justifiés dans la
PR.

## 🚪 Dernière règle avant chapitre 12

Une plateforme de production devra gérer plusieurs PR automatiques en parallèle. Si les
human-stop policies ne sont pas claires ici, le chapitre 12 amplifie le désordre au lieu de
l'opérer.
