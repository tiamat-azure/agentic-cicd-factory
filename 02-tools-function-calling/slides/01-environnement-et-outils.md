# 🧰 02.1 - Définir l'environnement d'action

## 🎯 Ce qu'il faut comprendre

Un agent n'est pas "un modèle + des fonctions". C'est un modèle placé dans un
**environnement d'action** borné, observable et validé.

Le bon point de départ n'est donc pas : "quelles fonctions avons-nous déjà ?"
mais : "quelles actions voulons-nous autoriser, et pourquoi ?"

## 🧭 La bonne forme d'environnement

Un environnement utile à un Coding Agent contient peu de choses :

- lecture du dépôt ;
- écriture bornée ;
- diff et statut git ;
- exécution de tests ;
- éventuellement HTTP en lecture seule ;
- éventuellement GitHub, mais avec permissions explicites.

> Plus l'environnement est large, plus l'agent devient imprévisible. Le but n'est pas de
> tout exposer, mais d'exposer juste assez.

## 🔁 Le réflexe "read before write"

L'ordre sain ressemble à ceci :

1. l'agent lit ;
1. il comprend ce qui existe ;
1. il propose une modification ;
1. le runtime vérifie que la modification est autorisée ;
1. seulement ensuite, il écrit.

Cela paraît trivial. C'est pourtant ce qui sépare un agent de code sérieux d'un script
qui "bricole" dans le dépôt.

## 🧱 Les 4 familles de tools

| Famille | Exemples | Risque principal |
| ------- | -------- | ---------------- |
| Lecture | `list_files`, `read_file`, `git_diff` | trop de contexte, pas assez de filtre |
| Écriture | `write_file`, `apply_patch` | fuite hors sandbox, corruption |
| Exécution | `run_tests`, `run_shell` | commandes destructives, latence |
| Réseau | `http_get`, `github_*` | données non fiables, permissions |

## 💡 À retenir

1. L'environnement d'action fait partie du design produit.
1. Un agent de code commence par lire, pas par réécrire.
1. Moins de tools, mais mieux délimités, vaut presque toujours mieux.
