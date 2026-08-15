# ⚖️ 12.2 - Scalabilité et résilience

## 📈 Ce qui change à l'échelle

Un run isolé échoue bruyamment. Une plateforme échoue parfois silencieusement : backlog qui
gonfle, retries qui multiplient le coût, modèle indisponible, tool lent, PR dupliquées,
quota d'une équipe qui bloque les autres.

La production exige donc des mécanismes simples : files, workers, quotas, idempotence,
checkpoints et backpressure.

## 🧺 Files de travail

| File | Exemple de contenu | Priorité typique | Risque principal |
| ---- | ------------------ | ---------------- | ---------------- |
| `intake` | demande utilisateur validée | haute | spam ou abus |
| `analysis` | classification, plan, estimation | normale | coût caché |
| `implementation` | modification de code | normale | conflit de branche |
| `verification` | tests, sécurité, evals | haute | fausse confiance |
| `human_review` | décision humaine requise | dépend du risque | blocage organisationnel |
| `incident_recovery` | reprise après crash | haute | doublon ou état incohérent |

Séparer les files évite qu'un type de tâche sature toute la plateforme.

## 🔁 Retries sûrs

Un retry est acceptable seulement si l'action est **idempotente** ou compensable.

| Action | Retry automatique ? | Condition |
| ------ | ------------------- | --------- |
| Appel modèle échoué sur timeout | oui | même prompt, même budget, trace du retry |
| Lecture de fichier | oui | lecture seule |
| Écriture sur branche agent | oui avec garde | même `request_id`, même base, pas de doublon |
| Création de PR | non par défaut | vérifier qu'une PR n'existe pas déjà |
| Merge | non | décision humaine et état externe trop critique |
| Déploiement | non | passer par procédure dédiée de release/rollback |

## 🧷 Idempotence et checkpoints

Chaque étape durable doit enregistrer :

- `request_id` et `workflow_id` ;
- entrée canonique de l'étape ;
- sortie validée ;
- statut machine-lisible ;
- version du prompt, de la policy et de l'eval ;
- pointeur vers les artefacts produits.

La règle : **reprendre depuis le dernier checkpoint validé**, jamais depuis une intuition.

## 🚦 Backpressure

Quand la charge dépasse la capacité, la plateforme doit ralentir proprement.

| Signal | Réponse saine |
| ------ | ------------- |
| backlog par tenant trop élevé | réduire le débit du tenant, pas de toute la plateforme |
| coût horaire supérieur au budget | refuser les tâches non urgentes ou demander validation |
| taux de failover modèle élevé | passer en mode dégradé et alerter |
| latence tools élevée | réduire la concurrence sur ce tool |
| evals instables | suspendre l'automatisation concernée |

## 🧯 Modes dégradés

La résilience n'est pas seulement « retenter ». C'est choisir une version plus sûre du
service :

- lecture et analyse autorisées, écriture suspendue ;
- PR autorisée, merge interdit ;
- modèle local pour tâches simples, humain pour tâches complexes ;
- nouveaux workflows refusés, workflows critiques terminés ;
- evals obligatoires élargies pendant incident.

## 💡 À retenir

1. Les retries sans idempotence créent des incidents.
1. Le backpressure est une fonctionnalité produit, pas un détail d'infrastructure.
1. Un mode dégradé explicite vaut mieux qu'une automatisation opaque qui continue.

-> Slide suivante : [`03-securite-gouvernance.md`](03-securite-gouvernance.md)
