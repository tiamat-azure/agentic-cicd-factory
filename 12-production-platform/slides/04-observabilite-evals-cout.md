# 🔭 12.4 - Observabilité, evals et coût en continu

## 🧭 Trois boucles, une seule décision

En production, tu ne peux pas piloter séparément qualité, fiabilité et coût. Une stratégie
moins chère qui dégrade les PR n'est pas une optimisation. Une stratégie très fiable mais
hors budget n'est pas durable.

La plateforme doit donc corréler :

- **observabilité** : ce qui s'est passé ;
- **evals** : si le résultat est acceptable ;
- **coût** : ce que le résultat a consommé.

## 📊 SLO agentiques

| SLO | Exemple de mesure | Pourquoi il compte |
| --- | ----------------- | ------------------ |
| Taux de PR utiles | PR acceptées ou demandant peu de corrections | mesure métier |
| Taux de réussite par workflow | `success / total` par type de tâche | fiabilité |
| Latence p95 | durée demande -> PR prête | expérience utilisateur |
| Coût par PR utile | coût total / PR acceptées | pilotage économique |
| Taux de rollback | changements annulés après merge/déploiement | qualité réelle |
| Taux de human escalation | part des décisions non automatiques | calibration du risque |
| Taux de failover modèle | appels basculés vers autre profil | santé du Model Gateway |
| Taux de régression eval | scénarios rouges par version | sécurité du changement |

## 🧪 Evals en production

Les evals ne sont pas un examen final ponctuel. Elles forment une boucle :

```text
trace réelle -> cas d'eval -> seuil -> canary -> production -> nouvelle trace
```

Quand un incident survient, transforme-le en scénario de régression. Sinon, la plateforme
peut répéter la même erreur avec plus de confiance.

## 🐤 Canary et shadow runs

| Technique | Utilisation | Décision saine |
| --------- | ----------- | -------------- |
| Canary | exposer une petite part du trafic à une nouvelle policy/prompt/route | élargir si qualité et coût restent verts |
| Shadow run | exécuter une variante sans agir sur le monde réel | comparer avant d'autoriser l'automatisation |
| Replay de traces | rejouer des demandes historiques | détecter les régressions avant release |
| A/B contrôlé | comparer deux stratégies sur segments équivalents | choisir sur coût par succès, pas intuition |

## 💸 Attribution du coût

Le coût doit être attribué au bon niveau :

- tenant ;
- repository ou produit ;
- type de workflow ;
- modèle ou route ;
- retry/fallback ;
- échec vs succès ;
- étape du workflow.

Sans cette attribution, tu optimiseras au mauvais endroit.

## 🚨 Alertes utiles

Une alerte doit mener à une action claire.

| Alerte | Action attendue |
| ------ | --------------- |
| coût par PR utile augmente de 50 % | inspecter retries, routage et failovers |
| p95 demande -> PR double | vérifier backlog, tools lents et quotas |
| eval sécurité rouge | bloquer automatisation concernée |
| failover modèle massif | activer mode dégradé et contacter fournisseur |
| taux d'escalade humaine chute brusquement | vérifier que la policy ne devient pas trop permissive |

## 💡 À retenir

1. L'observabilité explique le passé ; les evals protègent le futur.
1. Le coût utile se mesure par résultat acceptable, pas par appel modèle isolé.
1. Une automatisation non mesurée doit redevenir manuelle.

-> Slide suivante : [`05-disaster-recovery-exploitation.md`](05-disaster-recovery-exploitation.md)
