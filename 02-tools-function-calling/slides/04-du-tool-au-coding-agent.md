# 🧭 02.4 - Du tool au Coding Agent

## 🎯 Ce qu'il faut retenir

Le chapitre 02 ne vise pas encore un agent "intelligent". Il vise un agent **capable** :

- de voir un repo ;
- de choisir un petit ensemble de tools ;
- de modifier un fichier ;
- de vérifier le résultat ;
- de produire un résumé fiable.

## 🧵 La boucle minimale

```text
inspecter -> choisir un tool -> exécuter -> valider -> corriger -> diff final -> résumé
```

Cette boucle devient crédible seulement si :

- les tools sont bien nommés ;
- les permissions sont explicites ;
- les erreurs reviennent dans l'historique ;
- les tests sont exécutables ;
- le runtime garde la main.

## 🪜 Le bon niveau d'ambition

Un `Coding Agent v0.2` n'a pas besoin de :

- planification longue ;
- mémoire externe ;
- multi-agent ;
- MCP ;
- routage modèle complexe.

Il a besoin d'un environnement propre, et d'un contrat d'exécution propre.

## 🔭 Pont vers le chapitre 03

Une fois l'environnement maîtrisé, la vraie question devient :

> comment faire coopérer plusieurs étapes, plusieurs agents ou plusieurs responsabilités
> sans perdre le contrôle ?

C'est exactement le sujet du chapitre 03.

## 💡 À retenir

1. Le chapitre 02 transforme une boucle abstraite en agent de code concret.
1. La qualité du résultat dépend du design des tools autant que du prompt.
1. Un bon environnement simplifie le chapitre 03 au lieu de l'alourdir.
