# 🛡️ 02.3 - Permissions, erreurs et idempotence

## 🎯 Ce qu'il faut comprendre

Le runtime doit répondre à trois questions avant d'exécuter un tool :

1. Ai-je le droit ?
1. Est-ce sûr ?
1. Est-ce rejouable ?

## 🔐 Permissions

| Action | Règle saine |
| ------ | ----------- |
| Lire un fichier | autorisé si le chemin est dans la zone de travail |
| Écrire un fichier | autorisé seulement dans un répertoire borné |
| Lancer un shell | autorisé uniquement pour des commandes explicites |
| Accéder au réseau | interdit par défaut |
| Écrire dans git | demande une validation explicite avant toute action irréversible |

Le modèle peut proposer. Le runtime décide.

## ⏱️ Timeouts et retries

- tout tool lent doit avoir un timeout ;
- tout retry doit être borné ;
- toute erreur réseau doit être lisible ;
- toute commande dangereuse doit échouer de façon nette.

## 🔁 Idempotence

Une action est saine si la rejouer ne casse rien.

Exemples :

- `read_file` est naturellement idempotent ;
- `run_tests` est généralement rejouable ;
- `write_file` doit écrire de façon atomique ;
- `delete_file` ou `git push` ne devraient pas être exposés sans garde-fou fort.

## 🚨 Erreur utile

Un bon message d'erreur :

- dit ce qui a été refusé ;
- dit pourquoi ;
- dit comment corriger ;
- ne révèle pas plus que nécessaire.

## 💡 À retenir

1. Les permissions font partie du contrat de tool.
1. Un tool non rejouable doit être borné ou protégé.
1. Une erreur bien formulée aide l'agent à se corriger au lieu de tourner en rond.
