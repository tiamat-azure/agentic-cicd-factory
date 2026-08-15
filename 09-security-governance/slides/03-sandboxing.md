# 🧱 Sandboxing d'un coding agent

## 🎯 Idée clé

Le sandbox n'est pas seulement une protection système. C'est le contrat qui dit à l'agent :
"voici ton espace de travail, voici ce qui n'existe pas pour toi".

## 📦 Dimensions à contrôler

| Dimension | Limite typique |
| --------- | -------------- |
| Fichiers | lecture du repo, écriture sur chemins autorisés, aucun accès aux secrets locaux |
| Réseau | accès aux APIs nécessaires, blocage des destinations inconnues |
| Commandes | allowlist de commandes, pas de commande destructive globale |
| Temps | timeout par action et budget global par run |
| Ressources | quota CPU/mémoire si l'environnement le permet |
| Sorties | journalisation des diff, tool calls, erreurs et décisions |

## 🔒 Ressources hors limites

Pour la Factory, un agent de code ne doit jamais lire directement :

- secrets de production ;
- clés personnelles de mainteneurs ;
- jetons permettant de merger ou déployer ;
- données client non nécessaires à la tâche ;
- fichiers hors dépôt ou hors workspace autorisé.

## 🧪 Lien avec les evals

Un sandbox doit être testé comme une fonctionnalité :

- scénario qui tente de lire un secret -> `deny` ;
- scénario qui modifie un fichier interdit -> `deny` ;
- scénario qui dépasse le budget de tool calls -> arrêt contrôlé ;
- scénario normal sur branche dédiée -> `auto`.

Si ces cas ne sont pas rejouables, la sécurité repose sur une intention, pas sur une preuve.
