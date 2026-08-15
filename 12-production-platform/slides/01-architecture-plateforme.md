# 🏗️ 12.1 - Architecture d'une Agent Platform

## ❓ Le problème à résoudre

La PR Factory v1.1 sait produire une PR. La production demande autre chose : plusieurs
équipes, plusieurs dépôts, des quotas, des incidents, des secrets, des coûts attribuables,
des audits et des décisions humaines au bon endroit.

La question n'est plus :

> « Est-ce que l'agent peut faire la tâche ? »

mais :

> **« Est-ce que la plateforme peut laisser l'agent faire la tâche de façon sûre,
> mesurable, réversible et économiquement acceptable ? »**

## 🧱 Les composants minimaux

| Composant | Responsabilité | Ce qu'il ne doit pas faire |
| --------- | -------------- | -------------------------- |
| Agent Gateway | authentifier, identifier le tenant, limiter les quotas, créer `request_id` | décider du plan technique |
| Orchestrator | tenir l'état du workflow, reprendre, ordonnancer, éviter les doublons | exécuter les tools directement |
| Agent Runtime | lancer l'agent dans un sandbox avec budgets et terminaison | choisir les droits métier |
| MCP Gateway | exposer les tools autorisés avec audit et schémas stables | donner accès brut au réseau interne |
| Model Gateway | fournir des capacités modèle, router et failover | laisser le métier dépendre d'un fournisseur |
| Policy Engine | rendre `auto`, `human` ou `deny` explicable | cacher une décision dans un prompt |
| Eval Service | mesurer qualité, sécurité et régression | remplacer les tests ou l'audit |
| Observability | corréler traces, logs, métriques et coûts | stocker des secrets dans les traces |
| Cost Control | attribuer, plafonner, prévoir | optimiser au détriment du succès mesuré |

## 🧭 Flux de bout en bout

```text
1. demande entrante
2. authentification + tenant + quota
3. création du workflow et du checkpoint initial
4. analyse et plan sous budget
5. décision policy : continuer / humain / refuser
6. exécution agent dans sandbox
7. appels tools via MCP Gateway
8. appels modèles via Model Gateway
9. tests, sécurité, evals et cost check
10. PR, approbation humaine si nécessaire, déploiement contrôlé
11. monitoring, postmortem et apprentissage par evals
```

Chaque étape produit une trace et une décision exploitable. Si tu ne peux pas expliquer une
étape après coup, elle n'est pas prête pour la production.

## 🔌 Contrats plutôt que dépendances directes

Un agent de production ne connaît pas :

- le nom du fournisseur LLM ;
- le token GitHub brut ;
- l'URL interne d'un outil ;
- la règle exacte qui autorise un merge ;
- le backend d'observabilité.

Il connaît des **contrats** : `ModelGateway.generate`, `Tool.call`, `Policy.evaluate`,
`Trace.emit`, `Eval.run`. Cela rend le système remplaçable, testable et gouvernable.

## 🧵 End-state du parcours

| Chapitre | Brique accumulée | Rôle en production |
| -------- | ---------------- | ------------------ |
| 01-02 | boucle agentique + tools | Runtime borné |
| 03-04 | workflows + MCP | Orchestration et intégrations |
| 05-06 | Model Gateway + routing | modèle interchangeable et budgeté |
| 07-08 | tracing + evals | preuve de qualité et diagnostic |
| 09-10 | policy + CI/CD | gouvernance et gates automatisés |
| 11 | PR Factory | production de changement contrôlé |
| 12 | Agent Platform | exploitation multi-équipes |

## 💡 À retenir

1. Une plateforme agentique orchestre des responsabilités, pas seulement des prompts.
1. Les frontières de composants sont des frontières de risque.
1. Le bon design permet de remplacer modèle, tool, policy ou backend sans réécrire l'agent.

-> Slide suivante : [`02-scalabilite-resilience.md`](02-scalabilite-resilience.md)
