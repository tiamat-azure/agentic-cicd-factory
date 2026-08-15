# 🏭 03.5 - Factory v0.3

## 🧵 Le flux cible

```text
REQUEST -> ANALYZE -> PLAN -> APPROVE_PLAN -> IMPLEMENT -> TEST -> REVIEW -> APPROVE_PR -> PR
```

Ce n'est pas encore une plateforme complète. C'est le premier squelette de la Factory : un
processus lisible, borné, et prêt à recevoir de meilleurs tools.

## 🧾 Contrat des nodes

| Node           | Rôle                                                        | Sortie principale       |
| -------------- | ----------------------------------------------------------- | ----------------------- |
| `REQUEST`      | figer la demande et les contraintes                         | `request`               |
| `ANALYZE`      | comprendre le contexte, risques, fichiers probables         | `analysis`              |
| `PLAN`         | proposer étapes et critères d'acceptation                   | `plan`                  |
| `APPROVE_PLAN` | attendre une décision humaine                               | `human_decision`        |
| `IMPLEMENT`    | appliquer le plan validé avec tools du ch. 02               | `changes`               |
| `TEST`         | exécuter la validation disponible                           | `test_report`           |
| `REVIEW`       | relire diff, tests, conformité au plan                      | `review`                |
| `APPROVE_PR`   | attendre l'accord humain avant publication                  | `human_decision`        |
| `PR`           | préparer titre, description, checklist, sans merger         | `pr_draft`              |

## 🔐 Permissions par node

Le workflow n'a pas un seul niveau de permission global :

| Node        | Permissions typiques                                  |
| ----------- | ----------------------------------------------------- |
| `ANALYZE`   | lire fichiers, rechercher, lire historique git        |
| `PLAN`      | pas d'écriture, pas de commande destructive           |
| `IMPLEMENT` | écrire dans le workspace autorisé, lire diff          |
| `TEST`      | lancer les tests autorisés, lire les rapports         |
| `REVIEW`    | lecture seule sur diff, plan, tests                   |
| `PR`        | préparer ou ouvrir une PR, jamais merger              |

Cette séparation prépare le chapitre 09 : les policies seront plus faciles à appliquer si
les frontières existent déjà.

## 🧪 Conditions de sortie

Un workflow publication-ready ne termine pas par "ça marche". Il termine par un statut :

```text
ready_for_pr
needs_clarification
changes_requested
tests_failed
budget_exhausted
blocked_by_permissions
```

Le statut doit être lisible par une machine et compréhensible par un humain.

## 🌉 Pont vers le chapitre 04

Au chapitre 04, certains tools locaux deviendront des capabilities exposées via MCP : lire
un ticket, interroger GitHub, inspecter un runner, créer une PR. Le graphe ne doit pas
changer pour autant : seul l'adaptateur du node change.

C'est le test d'une bonne orchestration : **remplacer un tool sans redessiner le flux**.

## 💡 À retenir

1. Factory v0.3 est un squelette de production, pas une démo magique.
1. Les permissions suivent les nodes, pas l'agent global.
1. Un bon graphe survit au remplacement des tools par MCP.
