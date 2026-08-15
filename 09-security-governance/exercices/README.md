# 🧩 Exercices - Concevoir le Policy Engine v0.9

Fais les exercices avant de lire les solutions. L'objectif est de produire une policy assez
claire pour être branchée en CI/CD au chapitre 10.

## 🪪 Exercice 1 - Séparer les identités

Décris les identités de la Factory : `agent_code_writer`, `human_maintainer`, `ci_runner`,
`requester`.

Pour chacune, précise :

- ce qu'elle peut demander ;
- ce qu'elle peut exécuter ;
- ce qu'elle peut approuver ;
- ce qu'elle ne doit jamais faire.

Livrable attendu : une table `identité -> droits -> interdits -> trace d'audit`.

## 🧮 Exercice 2 - Matrice de permissions

Construis une matrice pour ces actions :

- lire le repo ;
- écrire une branche `agent/*` ;
- modifier une policy ;
- ouvrir une PR ;
- merger une PR ;
- déployer en staging ;
- déployer en production ;
- lire un secret.

Chaque cellule doit être `auto`, `human` ou `deny`, avec une justification courte.

## 🧱 Exercice 3 - Définir le sandbox

Écris le contrat de sandbox minimal de l'agent :

```toml
[sandbox.default]
secrets = "deny"
network = "restricted"
max_tool_calls = 0
max_minutes = 0
writable_paths = []
readonly_paths = []
```

Remplace les valeurs et justifie chaque limite. Une limite sans raison est une valeur
magique.

## 🧪 Exercice 4 - Scénarios d'eval sécurité

Écris au moins cinq scénarios d'eval avec :

| Champ | Sens |
| ----- | ---- |
| `id` | nom stable du scénario |
| `actor` | identité qui agit |
| `action` | capacité demandée |
| `target` | cible de l'action |
| `signals` | tests, score sécurité, criticité |
| `expected_decision` | `auto`, `human` ou `deny` |

Inclue obligatoirement : push sur `main`, lecture d'un secret, PR avec score faible,
déploiement production et changement de policy.

## ✅ Critère de réussite

Tu as réussi le chapitre si une autre personne peut appliquer ta policy à une action sans
te demander ton intention, et obtenir la même décision que toi.
