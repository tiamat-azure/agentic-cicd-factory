# 🔀 Classification et routing

## 🎯 Idée clé

Le routeur ne choisit pas "le meilleur modèle" dans l'absolu. Il choisit le profil le
moins coûteux qui a une chance raisonnable de réussir une classe de tâche donnée.

## 🧭 Classifier avant d'appeler

Le classifier peut commencer simple et déterministe. Il observe des signaux déjà connus :

- longueur et ambiguïté de la demande ;
- nombre de fichiers ou domaines concernés ;
- besoin de raisonnement architectural ;
- risque sécurité ou production ;
- sortie attendue : résumé, plan, patch, review ;
- budget restant dans le workflow.

Le classifier doit produire une décision explicable, pas seulement un score opaque.

## 🗂️ Trois classes utiles

| Classe | Exemple | Profil initial |
| ------ | ------- | -------------- |
| `simple` | reformuler une demande, extraire un JSON, résumer une trace courte | `local-small` |
| `medium` | analyser plusieurs fichiers, proposer un plan, reviewer un patch borné | `local-large` |
| `complex` | arbitrer une architecture, traiter une ambiguïté forte, raisonner sécurité | `cloud-frontier` |

Ces classes sont volontairement grossières. Les evals du chapitre 08 permettront de les
affiner.

## 🧱 Routing via le Model Gateway

Le routeur parle en profils de capacité :

```text
simple  -> local-small
medium  -> local-large
complex -> cloud-frontier
```

Le Model Gateway traduit ensuite ces profils vers les fournisseurs disponibles. Ainsi, le
code métier ne contient pas de branchement du type `if model == "..."`.

## 🧪 Décision traçable

Chaque décision de routing doit laisser une trace courte :

```json
{
  "task_class": "medium",
  "route": "local-large",
  "reason": "analyse multi-fichiers bornée, pas de risque sécurité, budget cloud conservé"
}
```

Cette raison sera affichée au chapitre 07 dans la trace du run. Elle évite les systèmes où
le coût augmente sans explication.

## ⚖️ Override humain

Certaines décisions doivent rester modifiables : incident production, sécurité, forte
incertitude métier. L'override doit être tracé comme une décision explicite, pas comme une
exception silencieuse au routeur.
