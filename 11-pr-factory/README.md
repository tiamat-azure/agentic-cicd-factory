# 🔀 11 - Automatic PR Factory

> Livrable : **PR Factory v1.1** - une demande utilisateur en langage naturel devient
> une PR GitHub complète, vérifiée, expliquée et arrêtée au bon endroit si le risque
> dépasse ce que la Factory peut assumer seule.

## 🎯 Objectifs pédagogiques

- Enchaîner toute la chaîne Requirement Agent -> Architecture Agent -> Coding Agent ->
  Test Agent -> Review Agent -> Security Agent -> Evaluation -> PR.
- Transformer chaque sortie d'agent en artefact relisible : décision, hypothèse,
  fichier touché, test, trace, coût, risque et prochain arrêt possible.
- Faire produire par la PR un contenu directement exploitable par un humain : résumé,
  changements d'architecture, fichiers modifiés, validations, sécurité, evals, coût et
  risques résiduels.
- Définir les politiques `auto`, `human` et `deny` qui empêchent une PR automatique de
  devenir un merge automatique implicite.
- Réaliser le **Gate 5** du parcours : une PR générée automatiquement à partir d'une
  demande, mais encore gouvernée par les evals et la policy.

## ✅ Prérequis

- Chapitre 10 (Factory v1.0 : checks classiques, evals, budgets et policies en CI/CD).
- Savoir lire une trace de run, un résultat d'eval et une décision du Policy Engine.
- Savoir distinguer ouvrir une PR, demander une review, merger et déployer.
- Durée estimée : **3 h** (1 h théorie + 45 min étude de cas + 1 h exercices + 15 min
  synthèse).

## 🚪 Gate du chapitre

> **Gate 5** : tu dois pouvoir partir d'une demande en langage naturel, produire une PR
> complète, prouver quels agents ont contribué, quelles validations ont été exécutées,
> combien le run a coûté, et expliquer pourquoi la Factory peut continuer seule ou doit
> s'arrêter pour un humain.

## 🧭 Parcours pas à pas

| Étape | Support | Ce que tu fais |
| ----- | ------- | -------------- |
| 1 | [`slides/01-chaine-agentique.md`](slides/01-chaine-agentique.md) | Lire : le contrat de passage entre agents |
| 2 | [`slides/02-contrat-pr.md`](slides/02-contrat-pr.md) | Lire : ce qu'une PR automatique doit contenir |
| 3 | [`slides/03-evals-cout-risques.md`](slides/03-evals-cout-risques.md) | Lire : evals, coût et risque dans le même artefact |
| 4 | [`slides/04-human-stop-policies.md`](slides/04-human-stop-policies.md) | Lire : où l'humain devient obligatoire |
| 5 | [`demos/README.md`](demos/README.md) | Examiner : une PR automatique commentée de bout en bout |
| 6 | [`exercices/README.md`](exercices/README.md) | Faire les exercices -> **PR Factory v1.1** |
| 7 | [`solutions/README.md`](solutions/README.md) | Comparer après tentative |
| 8 | [`../12-production-platform/`](../12-production-platform/) | Enchaîner : transformer la Factory en plateforme opérable |

## 📚 Plan théorique

1. Le flux complet : demande -> clarification -> architecture -> implémentation -> tests ->
   reviews -> evals -> PR.
1. Les contrats de handoff : chaque agent transmet un état vérifiable, pas seulement du
   texte libre.
1. Le contenu minimal d'une PR automatique : intention, diff, architecture, validations,
   evals, coût, sécurité, risques et limites.
1. La traçabilité : relier demande, trace, commit, run CI, suites d'eval et décision de
   policy.
1. Les politiques d'arrêt humain : ambiguïté, sécurité, coût, échec d'eval, changement
   sensible ou privilège trop large.
1. La frontière avec le chapitre 12 : une PR automatique est un produit livrable ; une
   plateforme de production doit ensuite gérer files d'attente, quotas, incidents et SLO.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : la chaîne est décrite comme des rôles, contrats et artefacts ;
  elle peut être implémentée avec n'importe quel orchestrateur.
- **Model-agnostic** : chaque agent passe par le Model Gateway et le Model Router. La PR
  expose le profil utilisé et les métriques, jamais une logique métier dépendante d'un
  fournisseur.
- **Eval-first** : la PR ne dit pas seulement "ça marche". Elle publie les suites d'eval,
  les seuils, les deltas, le coût par succès et les raisons d'arrêt éventuelles.

## 🔁 Chaîne agentique cible

La PR Factory ne demande pas à un seul agent de tout deviner. Elle compose des agents
spécialisés et borne leurs responsabilités.

```text
User request
  -> Requirement Agent     : clarifie l'intention, le scope et les critères d'acceptation
  -> Architecture Agent    : propose le plan technique et les zones à risque
  -> Policy pre-check      : autorise, demande un humain ou refuse avant modification
  -> Coding Agent          : modifie uniquement les fichiers autorisés
  -> Test Agent            : exécute les validations adaptées et capture les résultats
  -> Review Agent          : cherche régressions, incohérences et dette introduite
  -> Security Agent        : vérifie permissions, secrets, injection, dépendances, sandbox
  -> Evaluation runner     : compare qualité, sécurité, coût et baseline
  -> PR Composer           : assemble branche, commits, PR body, labels et reviewers
  -> Policy final gate     : décide auto-open, human-before-open ou deny
```

Le point important : **un agent ne valide jamais son propre travail seul**. Le Coding Agent
produit un diff ; les agents de test, review, sécurité et eval produisent les preuves qui
rendent ce diff proposable.

## 📜 Contrats de handoff

Chaque étape doit produire une sortie structurée assez simple pour être inspectée dans la
trace et résumée dans la PR.

| Étape | Entrée minimale | Sortie attendue | Arrêt possible |
| ----- | --------------- | --------------- | -------------- |
| Requirement | demande utilisateur, contexte repo | intention, hors-scope, critères d'acceptation | `human` si la demande est ambiguë ou conflictuelle |
| Architecture | critères, carte du code, contraintes | plan, fichiers probables, risques, stratégie de test | `human` si changement d'architecture sensible |
| Policy pre-check | plan, permissions, sandbox | décision `auto` / `human` / `deny` | `deny` si action interdite ou secret requis |
| Coding | plan autorisé, budget, sandbox | diff limité, notes d'implémentation | `human` si le scope dérive |
| Test | diff, matrice de checks | commandes réellement lancées, résultat, logs utiles | `human` si validation impossible à exécuter |
| Review | diff, intention, tests | findings bloquants ou acceptation motivée | `human` si risque non tranché |
| Security | diff, policy, secrets, dépendances | risques sécurité et décision | `deny` si fuite secret ou privilège excessif |
| Evaluation | traces, baseline, seuils | scores, deltas, coût, décision de qualité | `human` ou `deny` si seuil critique échoue |
| PR Composer | toutes les preuves | branche, commits, PR body, labels, reviewers | `human` si la PR serait trompeuse ou incomplète |

## 🧾 Contrat de PR automatique

Une PR générée par la Factory doit être lisible sans ouvrir la trace complète. La trace
reste la preuve détaillée ; la PR est le résumé actionnable.

```markdown
## 🧭 Summary
- Demande initiale et intention reformulée
- Résultat obtenu et limites connues

## 🏗️ Architecture / Design
- Décisions prises
- Alternatives rejetées
- Fichiers ou modules concernés

## 🧩 Changes
- Liste groupée par type : code, tests, docs, config, policy

## ✅ Validation
- Tests/checks exécutés avec leur résultat
- Checks non exécutés avec justification

## 📊 Evaluation
- Suites lancées, baseline, seuils, score actuel, delta
- Décision : pass / needs-human-approval / block

## 💸 Cost and Traceability
- run_id, trace_id, commit, CI run
- profils de modèle utilisés, tokens, latence, coût estimé
- coût par tâche réussie ou raison d'échec

## 🔐 Security and Governance
- sandbox appliqué, permissions utilisées, secrets exposés : oui/non
- findings sécurité, risques résiduels, policy decision

## 👤 Human Review Required
- Cases précises à vérifier par le mainteneur
- Conditions avant merge
```

La PR ne doit jamais masquer une incertitude. Un champ "non exécuté" vaut mieux qu'un
silence : il indique au reviewer ce qui reste à vérifier.

## 📊 Métadonnées d'évaluation et de coût

Les métriques coût/qualité ne sont pas décoratives. Elles décident si l'automatisation a
créé de la valeur ou seulement déplacé du travail vers le reviewer.

| Champ | Pourquoi il est dans la PR |
| ----- | -------------------------- |
| `run_id` / `trace_id` | retrouver la trace complète du chapitre 07 |
| `task_class` | comparer une demande simple, medium ou complexe au bon segment |
| `eval_suite` | savoir quelle qualité a été mesurée |
| `baseline_score` / `current_score` | voir l'amélioration ou la régression |
| `threshold` / `delta` | expliquer pass, block ou exception humaine |
| `input_tokens` / `output_tokens` / `cached_tokens` | auditer la consommation réelle |
| `tool_calls` / `iterations` | détecter une boucle coûteuse ou fragile |
| `latency_ms` | relier expérience reviewer et coût opérationnel |
| `cost_usd` | vérifier le budget du run |
| `cost_per_success` | comparer les stratégies de routing du chapitre 06 |
| `policy_decision` | prouver que la gouvernance du chapitre 09 a été appliquée |

Une bonne PR automatique donne donc deux lectures : le reviewer lit le résumé ; l'opérateur
retrouve les preuves.

## 🛑 Politiques human-stop minimales

La Factory peut ouvrir une PR automatiquement seulement si les risques sont bornés. Elle
s'arrête avant ouverture, ou ouvre en demandant explicitement une validation, dans les cas
suivants.

| Condition | Décision par défaut | Raison |
| --------- | ------------------- | ------ |
| Demande ambiguë ou critères d'acceptation contradictoires | `human` | éviter de coder une mauvaise intention |
| Modification hors fichiers autorisés par le plan | `human` | empêcher la dérive de scope |
| Besoin de secret, token personnel ou privilège admin | `deny` | l'agent ne doit jamais demander plus de droits métier |
| Échec d'un test ou d'une eval critique | `human` ou `deny` | la PR doit porter un risque explicite, pas un faux vert |
| Baisse sous seuil sécurité ou policy `deny` | `deny` | le chapitre 09 reste prioritaire sur la vitesse |
| Coût ou itérations au-dessus du budget | `human` | détecter runaway, retries inutiles ou mauvais routing |
| Changement de policy, workflow critique ou surface d'auth | `human` | les zones sensibles gardent une approbation humaine |
| PR body incomplet ou trace non corrélable | `human` | une PR automatique non auditée n'est pas publiable |

La règle pratique : **l'agent peut proposer, mais il ne peut pas rendre invisible une
incertitude importante**.

## 🧩 Livrable

**PR Factory v1.1** - une spécification complète et vérifiable contenant :

- une chaîne d'agents avec contrats d'entrée/sortie ;
- un format de trace corrélant demande, plan, diff, tests, evals, coût et policy ;
- un template de PR automatique exploitable par un mainteneur ;
- une matrice de décisions `auto` / `human` / `deny` ;
- une liste de métadonnées d'évaluation, coût et sécurité à publier ;
- un scénario de bout en bout démontrant le Gate 5.

## 🔗 Ressources

- [`../06-token-engineering-routing/`](../06-token-engineering-routing/) - budgets,
  routing et coût par succès.
- [`../07-observability-tracing/`](../07-observability-tracing/) - traces corrélées.
- [`../08-evaluation-engineering/`](../08-evaluation-engineering/) - suites d'eval,
  baseline et seuils.
- [`../09-security-governance/`](../09-security-governance/) - policy `auto` / `human` /
  `deny`.
- [`../10-agentic-cicd/`](../10-agentic-cicd/) - gates CI/CD avant PR automatique.
- GitHub Docs - Pull requests, required checks, branch protection rules and CODEOWNERS.

## 📝 Auto-évaluation

Tu peux passer au chapitre 12 quand tu réponds sans hésiter :

1. Pourquoi le Coding Agent ne doit-il pas être le seul juge de la PR qu'il produit ?
1. Quels champs de PR permettent à un humain de reviewer sans relire toute la trace ?
1. Quelle différence fais-tu entre `auto-open PR`, `human-before-open` et `deny` ?
1. Comment prouves-tu qu'une PR automatique respecte le budget et les evals ?
1. Quels signaux doivent arrêter la Factory même si le diff semble correct ?
