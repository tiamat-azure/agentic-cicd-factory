# 🧩 03.2 - Graphe, state, nodes et edges

## 🗺️ Le vocabulaire minimal

| Concept              | Question à poser                                      | Exemple dans la Factory v0.3               |
| -------------------- | ----------------------------------------------------- | ------------------------------------------ |
| `State`              | Qu'est-ce que le workflow sait maintenant ?           | demande, plan, diff, rapport de tests      |
| `Node`               | Quelle transformation isolée applique-t-on ?          | analyser, planifier, tester                |
| `Edge`               | Quelle est la prochaine étape normale ?               | `PLAN -> IMPLEMENT`                        |
| `Conditional Edge`   | Quelle branche selon le state ?                       | `TEST -> IMPLEMENT` si échec réparable     |
| `Checkpoint`         | Quel état stable faut-il sauvegarder ?                | plan validé, résultats de tests            |
| Human approval       | Quelle décision ne doit pas être automatique ?        | valider le plan, autoriser la PR           |

## 🧠 Le state n'est pas un prompt géant

Le state est un objet métier. Il doit contenir des données nommées, pas seulement une
conversation brute.

```text
request: texte utilisateur original
analysis: contraintes, fichiers probables, risques
plan: étapes proposées, critères d'acceptation
changes: résumé du diff produit
test_report: commandes lancées, statut, erreurs
review: points bloquants, niveau de confiance
pr_draft: titre, description, checklist
status: running | waiting_human | failed | ready_for_pr
```

Chaque node lit une partie du state et écrit une partie précise. Cette discipline évite
qu'un node réécrive silencieusement une décision validée.

## 🧱 Un node doit avoir un contrat

Un bon node se décrit en quatre lignes :

1. **Entrées lues** : les champs nécessaires du state.
1. **Sorties écrites** : les champs modifiés.
1. **Tools autorisés** : ce que le node peut appeler.
1. **Échec attendu** : comment il signale un blocage.

Exemple :

```text
Node TEST
Lit : changes, plan
Écrit : test_report, status
Tools : run_tests, git_diff (lecture)
Échec : status = tests_failed, avec message exploitable
```

## 🔀 Les edges portent les règles de flux

Les edges ne sont pas de la décoration. Ils encodent la politique de passage :

```text
ANALYZE -> PLAN
PLAN -> APPROVE_PLAN
APPROVE_PLAN -> IMPLEMENT si approved
APPROVE_PLAN -> STOP_NEEDS_CLARIFICATION si rejected
TEST -> REVIEW si tests green
TEST -> IMPLEMENT si tests red mais correction autorisée
TEST -> STOP_FAILED si tests red non réparable dans le budget
```

## 💡 À retenir

1. Le state est la source de vérité du run.
1. Un node sans contrat devient vite un mini-agent incontrôlé.
1. Les conditional edges sont l'endroit naturel pour rendre les règles auditables.

-> Slide suivante : [`03-patterns-orchestration.md`](03-patterns-orchestration.md)
