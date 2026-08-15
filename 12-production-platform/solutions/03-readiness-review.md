# 📦 Solution 3 - Readiness review Factory v2.0

## ✅ Décision synthétique

Statut recommandé pour un premier pilote : **acceptable pour pilote**, pas encore pour
généralisation multi-organisation.

Raison : l'architecture, les gates et les runbooks sont définis, mais les seuils réels de
qualité et de coût doivent être calibrés sur les premières traces de production.

## 🏗️ Architecture

| Item | Statut | Commentaire |
| ---- | ------ | ----------- |
| Composants séparés | vert | gateways, runtime, policy, evals et observability ont des rôles distincts |
| Contrats nommés | vert | `request_id`, `tenant_id`, `workflow_id`, `trace_id`, `budget` |
| Reprise workflow | jaune | checkpoints définis, drill à exécuter avant généralisation |

## 🔐 Sécurité

| Item | Statut | Commentaire |
| ---- | ------ | ----------- |
| Identités séparées | vert | agent, utilisateur, service et admin distincts |
| Secrets hors prompt | vert | capacités déléguées uniquement |
| Actions `auto/human/deny` | vert | merge et déploiement restent humains en pilote |
| Audit exploitable | jaune | vérifier rétention et accès par tenant |

## 🔭 Observabilité et evals

| Item | Statut | Commentaire |
| ---- | ------ | ----------- |
| Trace de bout en bout | vert | obligatoire dès l'intake |
| Evals qualité/sécurité | jaune | seuils initiaux prudents, à recalibrer |
| Dashboards | vert | succès, latence, coût, failover, escalation |

## 💸 Coût et exploitation

| Item | Statut | Commentaire |
| ---- | ------ | ----------- |
| Attribution du coût | vert | tenant + workflow + route modèle |
| Budgets avec action | vert | backpressure et validation humaine |
| Retries idempotents | jaune | auditer chaque action durable avant activation large |
| Runbook incident | jaune | prêt sur papier, drill nécessaire |

## 🧯 Disaster recovery

| Item | Statut | Commentaire |
| ---- | ------ | ----------- |
| RTO/RPO | jaune | objectifs définis, non encore prouvés |
| Sauvegardes critiques | vert | checkpoints, policies, traces, evals |
| Drill planifié | jaune | bloquant avant généralisation |

## 🚦 Conditions de passage en généralisation

1. Un drill de reprise réussi avec preuve de non-doublon.
1. 30 jours de métriques coût par PR utile et taux de rollback.
1. Aucun incident critique sans scénario d'eval ajouté.
1. Revue d'audit confirmant séparation des tenants et masquage des secrets.
1. Validation explicite des actions qui peuvent rester automatiques.
