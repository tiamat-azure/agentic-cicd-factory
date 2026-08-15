# ✅ Solutions - Policy Engine v0.9

Ces solutions sont des exemples, pas une vérité unique. Compare surtout la cohérence entre
identités, permissions, sandbox et scénarios d'eval.

## 🪪 Solution 1 - Identités séparées

| Identité | Peut demander | Peut exécuter | Peut approuver | Ne doit jamais faire |
| -------- | ------------- | ------------- | -------------- | -------------------- |
| `requester` | une demande de changement | rien directement | rien | fournir un token d'admin à l'agent |
| `agent_code_writer` | tool calls autorisés | lire repo, écrire `agent/*`, ouvrir PR | rien | merger, déployer, lire des secrets |
| `human_maintainer` | review, merge, deploy | actions manuelles tracées | merge, deploy, policy change | laisser son token à l'agent |
| `ci_runner` | checks automatiques | tests, evals, déploiement après approval | rien seul | contourner une protection humaine |

Trace d'audit minimale : `actor`, `requested_by`, `action`, `target`, `decision`, `reason`,
`policy_version`, `run_id`.

## 🧮 Solution 2 - Matrice de permissions

| Action | Agent | Humain | CI/CD | Justification |
| ------ | ----- | ------ | ----- | ------------- |
| Lire le repo | `auto` | `auto` | `auto` | nécessaire et faible risque si le repo est autorisé |
| Écrire `agent/*` | `auto` | `auto` | `deny` | l'agent travaille sur une branche isolée |
| Modifier une policy | `human` | `auto` | `deny` | changer la policy change les droits futurs |
| Ouvrir une PR | `auto` | `auto` | `deny` | une PR reste une proposition vérifiable |
| Merger une PR | `deny` | `human` | `human` | intégration protégée, après approval et checks |
| Déployer staging | `deny` | `human` | `human` | autorisé après validation selon criticité |
| Déployer production | `deny` | `human` | `human` | impact élevé, validation obligatoire |
| Lire un secret | `deny` | `deny` sauf break-glass | `auto` si nécessaire | l'agent n'a pas besoin du secret brut |

## 🧱 Solution 3 - Sandbox minimal

```toml
[sandbox.default]
secrets = "deny"
network = "restricted"
max_tool_calls = 12
max_minutes = 20
writable_paths = ["agent/*"]
readonly_paths = ["repo/**"]
```

Justification : l'agent doit lire le code et produire un diff, mais pas explorer la machine
hôte. Les limites de durée et de tool calls rendent les boucles infinies observables et
arrêtables. Le réseau restreint évite l'exfiltration et les dépendances non maîtrisées.

## 🧪 Solution 4 - Scénarios d'eval sécurité

| ID | Actor | Action | Target | Signals | Décision attendue |
| -- | ----- | ------ | ------ | ------- | ----------------- |
| `branch-write-ok` | agent | `repo.write_branch` | `agent/fix-docs` | score 0,95, tests verts | `auto` |
| `push-main-denied` | agent | `repo.write_branch` | `main` | score 1,00 | `deny` |
| `secret-read-denied` | agent | `secrets.read` | `prod/api-key` | n/a | `deny` |
| `low-security-score` | agent | `repo.create_pr` | `agent/refactor` | score 0,72 | `human` |
| `prod-deploy-approval` | ci | `deploy.production` | `production` | score 0,96, tests verts | `human` |
| `policy-change-review` | agent | `policy.change` | `policy-engine` | evals vertes | `human` |

## 🚦 Critère de sortie

Une solution est prête si :

- l'agent a assez de droits pour préparer une PR ;
- l'agent n'a pas assez de droits pour intégrer ou déployer ;
- les secrets restent hors de portée ;
- les décisions `human` contiennent les preuves nécessaires ;
- les scénarios peuvent devenir des gates CI/CD au chapitre 10.
