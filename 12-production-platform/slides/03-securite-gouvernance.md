# 🔐 12.3 - Sécurité et gouvernance à l'échelle

## 🧨 Le nouveau risque

Au chapitre 09, tu as gouverné une action. En production, tu gouvernes des milliers
d'actions, plusieurs équipes et des intégrations qui changent. Le risque principal n'est
pas seulement l'agent malveillant : c'est le **droit implicite** qui apparaît parce qu'une
frontière est floue.

## 🪪 Identités séparées

| Identité | Exemple | Droits attendus |
| -------- | ------- | --------------- |
| Utilisateur | personne qui demande le changement | demander, suivre, approuver selon rôle |
| Agent | `agent:code-writer` | agir dans un sandbox borné |
| Service | compte technique CI/CD | appeler APIs nécessaires, jamais humain |
| Reviewer | mainteneur humain | approuver PR ou déploiement |
| Admin plateforme | équipe d'exploitation | configurer quotas, policies, tenants |

Un agent ne doit jamais emprunter l'identité complète d'un humain. Il agit pour un humain,
avec une identité dédiée et des droits limités.

## 🏢 Multi-tenancy

Le tenant peut être une équipe, une organisation, un produit ou un environnement. Il sert à
isoler :

- quotas de coût et de concurrence ;
- repositories et outils autorisés ;
- jeux d'evals et seuils ;
- secrets et environnements ;
- dashboards et audit logs ;
- règles human-in-the-loop.

Sans `tenant_id`, tu ne peux ni facturer, ni auditer, ni limiter proprement.

## 🔑 Secrets

Règle simple : **l'agent ne lit pas les secrets bruts**.

Il reçoit des capacités déléguées :

- token court-vivant limité à une action ;
- accès à un tool qui signe ou déploie sans révéler la clé ;
- environnement sandbox sans export de secrets ;
- masquage dans traces et logs ;
- rotation et révocation indépendantes du prompt.

## 🧾 Audit

Une entrée d'audit doit répondre à six questions :

| Question | Exemple |
| -------- | ------- |
| Qui a demandé ? | `user:alice` |
| Qui a agi ? | `agent:code-writer` |
| Quelle action ? | `repo.create_pull_request` |
| Sur quelle cible ? | `repo:factory`, branche `agent/123` |
| Pourquoi autorisé ? | policy `pr-open:auto`, evals vertes |
| Où est la preuve ? | `trace_id`, artefacts, commit, PR |

Un audit log n'est pas un log applicatif verbeux. C'est une preuve structurée.

## ⚖️ RBAC et policy

La matrice RBAC donne les capacités maximales. La policy décide ensuite selon le contexte.

```text
RBAC dit : cet agent peut ouvrir une PR.
Policy dit : cette PR précise peut être ouverte automatiquement car les evals sont vertes,
le coût est sous budget, la branche est isolée et aucun secret n'a été touché.
```

Les deux niveaux sont nécessaires : RBAC sans policy est trop large ; policy sans RBAC est
fragile.

## 💡 À retenir

1. Les droits d'un agent dépendent de l'action, du contexte et du tenant, pas du modèle.
1. Les secrets doivent être transformés en capacités, jamais exposés au prompt.
1. L'audit est une fonctionnalité de production, pas une option de debug.

-> Slide suivante : [`04-observabilite-evals-cout.md`](04-observabilite-evals-cout.md)
