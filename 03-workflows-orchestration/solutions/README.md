# ✅ Solutions - chapitre 03

Ces solutions donnent une cible raisonnable, pas un corrigé unique. Compare-les à ton
travail après avoir tenté les exercices.

## 🧱 Solution 1 - State minimal

```text
request:
  text: "Ajoute une validation qui empêche la Factory d'ouvrir une PR si les tests n'ont pas été exécutés."
  source: "user"
  immutable: true

analysis:
  intent: "block PR creation when no test report exists"
  affected_nodes: ["TEST", "REVIEW", "PR"]
  risks: ["confondre tests non exécutés et tests échoués", "bloquer une PR documentation sans règle explicite"]

plan:
  steps:
    - "rendre test_report obligatoire avant PR"
    - "faire échouer REVIEW si test_report est absent"
    - "ajouter un message de blocage exploitable"
  acceptance:
    - "PR impossible si test_report.status est missing"
    - "PR possible si test_report.status est green et review approved"

status: plan_ready
```

Le point important : `request` reste immuable ; `analysis` et `plan` sont séparés.

## 🔀 Solution 2 - Edges depuis TEST

| Condition                         | Prochain node       | Statut écrit                 | Reprise nécessaire                    |
| --------------------------------- | ------------------- | ---------------------------- | ------------------------------------- |
| `test_report.status == green`     | `REVIEW`            | `tests_passed`               | checkpoint du rapport de tests        |
| `status == red` et budget restant | `IMPLEMENT`         | `needs_fix`                  | erreurs, budget restant, plan validé  |
| `status == red` hors plan         | `APPROVE_PLAN`      | `plan_change_required`       | commentaire expliquant le hors scope  |
| commande indisponible             | `STOP_FAILED`       | `blocked_missing_test_tool`  | commande attendue, environnement      |
| budget épuisé                     | `STOP_FAILED`       | `budget_exhausted`           | dernier diff, dernier rapport d'erreur |

Une boucle `TEST -> IMPLEMENT -> TEST` doit être bornée par un compteur, par exemple deux
corrections maximum.

## 📦 Solution 3 - Factory v0.3

### 🧾 State proposé

```text
request: demande originale et métadonnées
analysis: intention, risques, fichiers probables, type de demande
plan: étapes validables, critères d'acceptation, budget
human_decisions: liste horodatée des décisions humaines
changes: fichiers modifiés, résumé du diff, limites connues
test_report: commande, statut, erreurs, durée
review: statut, remarques bloquantes, confiance
pr_draft: titre, description, checklist
status: running | waiting_human | ready_for_pr | failed
```

### 🧩 Contrats de nodes

| Node           | Lit                         | Écrit                 | Tools autorisés                   |
| -------------- | --------------------------- | --------------------- | --------------------------------- |
| `REQUEST`      | entrée utilisateur          | `request`, `status`   | aucun                             |
| `ANALYZE`      | `request`                   | `analysis`            | recherche et lecture seulement   |
| `PLAN`         | `request`, `analysis`       | `plan`                | aucun tool d'écriture             |
| `APPROVE_PLAN` | `plan`                      | `human_decisions`     | interface humaine                 |
| `IMPLEMENT`    | `plan`, décision approuvée  | `changes`             | écriture bornée, diff             |
| `TEST`         | `changes`, `plan`           | `test_report`         | commande de test autorisée        |
| `REVIEW`       | `plan`, `changes`, `tests`  | `review`              | lecture seule                     |
| `APPROVE_PR`   | `review`, `pr_draft`        | `human_decisions`     | interface humaine                 |
| `PR`           | `review`, décisions, tests  | `pr_draft`, `status`  | création ou préparation de PR     |

### 💾 Checkpoints

- `plan_created` : sauvegarde `request`, `analysis`, `plan`, statut et décision humaine
  associée. Reprise possible directement à `IMPLEMENT` si le plan est approuvé.
- `tests_finished` : sauvegarde `changes`, `test_report`, budget restant et statut.
  Reprise possible à `REVIEW` si vert, ou à `IMPLEMENT` si correction autorisée.

### 🛂 Approbations humaines

```text
APPROVE_PLAN:
  decision: approved | rejected | needs_changes
  comment_required_unless: approved

APPROVE_PR:
  decision: approved | rejected | needs_changes
  comment_required_unless: approved
```

La décision est une donnée du state, pas un message perdu dans une conversation.

### 🌉 Préparation MCP

Au chapitre 04, les tools `read_issue`, `inspect_repo`, `run_tests` et `create_pr` peuvent
être remplacés par des tools MCP. Le graphe reste identique : seuls les adaptateurs des
nodes changent.
