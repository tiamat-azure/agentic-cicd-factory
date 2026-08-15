# ✏️ Exercices - chapitre 12

Trois exercices de synthèse. Le 3 est le livrable **Factory v2.0**. Travaille dans
`exercices/`, puis compare avec `solutions/` après avoir tenté.

| # | Exercice | Compétence visée | Durée |
| - | -------- | ---------------- | ----- |
| 1 | Dessiner la plateforme | relier composants, contrats et risques | 25 min |
| 2 | Définir SLO, budgets et modes dégradés | exploiter sans dérive | 30 min |
| 3 | Readiness review Factory v2.0 | décider si la plateforme peut produire | 45 min |

______________________________________________________________________

## 🏗️ Exercice 1 - Blueprint de plateforme

Rédige `exercices/01-platform-blueprint.md` avec :

1. un diagramme texte des composants ;
1. les responsabilités de chaque composant ;
1. les contrats échangés (`request_id`, `tenant_id`, `trace_id`, `budget`, `policy_decision`) ;
1. trois frontières de risque et leur protection ;
1. une phrase expliquant pourquoi l'agent ne parle pas directement au fournisseur LLM ni
   aux tools internes.

Critère de réussite : quelqu'un qui n'a pas suivi le chapitre doit pouvoir dire où placer
une nouvelle intégration sans modifier l'agent.

______________________________________________________________________

## 📊 Exercice 2 - SLO, budgets et modes dégradés

Rédige `exercices/02-slo-runbook.md` avec :

1. quatre SLO : qualité, latence, coût, sécurité ;
1. deux budgets par tenant ;
1. une règle de backpressure ;
1. une stratégie de failover modèle ;
1. un mode dégradé quand les evals deviennent instables ;
1. une alerte qui mène à une action claire.

Critère de réussite : chaque métrique doit avoir un seuil et une action associée.

______________________________________________________________________

## 📦 Exercice 3 - Livrable Factory v2.0 : readiness review

Objectif : décider si ta Agentic CI/CD Factory peut être proposée à une première équipe.

Rédige `exercices/03-readiness-review.md` sous forme de checklist argumentée.

### ✅ 3.a - Architecture

- [ ] Gateway, Orchestrator, Runtime, MCP Gateway, Model Gateway, Policy Engine, Eval
  Service, Observability et Cost Control sont séparés.
- [ ] Chaque composant a une responsabilité claire.
- [ ] Les contrats d'entrée/sortie sont nommés.

### 🔐 3.b - Sécurité

- [ ] Les identités utilisateur, agent, service et admin sont séparées.
- [ ] Les secrets ne sont jamais exposés au prompt.
- [ ] Les actions `auto`, `human` et `deny` sont définies.
- [ ] L'audit répond à qui, quoi, où, pourquoi et avec quelle preuve.

### 🔭 3.c - Observabilité et evals

- [ ] Chaque demande a un `trace_id` de bout en bout.
- [ ] Les evals qualité et sécurité bloquent les régressions critiques.
- [ ] Les dashboards montrent succès, latence, coût, failover et escalade humaine.

### 💸 3.d - Coût et exploitation

- [ ] Le coût est attribué par tenant et par workflow.
- [ ] Les budgets ont des seuils et actions.
- [ ] Les retries sont limités aux actions idempotentes.
- [ ] Le runbook incident contient reprise, rollback et communication.

### 🧯 3.e - Disaster recovery

- [ ] RTO et RPO sont définis.
- [ ] Checkpoints, policies, traces, audit logs et résultats d'evals sont sauvegardés.
- [ ] Un drill de reprise est planifié.

Critère de validation : si un item reste rouge, écris la décision correspondante :
`bloquant`, `acceptable pour pilote`, ou `à traiter avant généralisation`.

______________________________________________________________________

## 🎁 Bonus

Choisis une automatisation que tu aurais envie de rendre totalement automatique. Écris ce
qui devrait être mesuré, audité et réversible avant de supprimer la validation humaine.
