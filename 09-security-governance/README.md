# 🔐 09 - Agent Security & Governance

> Livrable : **Policy Engine v0.9** - une politique déclarative qui décide, pour chaque
> action de la Factory, si l'agent peut continuer seul, doit demander une validation
> humaine, ou doit s'arrêter.

## 🎯 Objectifs pédagogiques

- Séparer clairement identité agent, identité utilisateur, identité service et identité
  admin.
- Construire une matrice de permissions par action : lire, écrire, ouvrir une PR, merger,
  déployer, accéder aux secrets.
- Définir un sandbox qui limite fichiers, réseau, secrets, commandes et durée d'exécution.
- Placer des validations humaines aux bons endroits, sans transformer tout le workflow en
  validation manuelle.
- Relier les décisions de gouvernance aux traces et evals des chapitres 07 et 08.

## ✅ Prérequis

- Chapitre 08 (Evaluation Framework v0.8).
- Savoir lire une trace de run et un résultat d'eval.
- Durée estimée : **2 h 30** (1 h théorie + 45 min atelier policy + 45 min exercices).

## 🚪 Gate du chapitre

> Tu dois pouvoir prendre une action demandée par l'agent et justifier la décision
> `auto`, `human` ou `deny` à partir de son identité, de ses permissions, du sandbox, des
> résultats d'eval et du risque métier.

## 🧭 Parcours pas à pas

| Étape | Support | Ce que tu fais |
| ----- | ------- | --------------- |
| 1 | [`slides/01-identites-separees.md`](slides/01-identites-separees.md) | Lire : pourquoi un agent n'est jamais un admin |
| 2 | [`slides/02-matrice-permissions.md`](slides/02-matrice-permissions.md) | Lire : traduire les rôles en actions autorisées |
| 3 | [`slides/03-sandboxing.md`](slides/03-sandboxing.md) | Lire : isoler fichiers, réseau, secrets et commandes |
| 4 | [`slides/04-human-in-the-loop.md`](slides/04-human-in-the-loop.md) | Lire : décider où l'humain est obligatoire |
| 5 | [`slides/05-security-evals-et-cicd.md`](slides/05-security-evals-et-cicd.md) | Lire : transformer la policy en gate CI/CD |
| 6 | [`demos/`](demos/) | Examiner : policy déclarative et scénarios d'eval sécurité |
| 7 | [`exercices/`](exercices/) | Faire les exercices -> **Policy Engine v0.9** |
| 8 | [`solutions/`](solutions/) | Comparer et corriger |

## 📚 Plan théorique

1. Identités séparées : agent, utilisateur, mainteneur, service account, runner CI.
1. Permissions minimales : capacité explicite par action et par cible.
1. Sandboxing : ce que l'agent peut voir, modifier, appeler et combien de temps il peut
   tourner.
1. Human-in-the-loop : validations humaines proportionnées au risque.
1. Evals sécurité : vérifier que la policy bloque aussi les régressions de gouvernance.
1. Préparation du chapitre 10 : brancher ces décisions comme gates de CI/CD.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : la policy décrit des décisions (`auto`, `human`, `deny`) sans
  dépendre d'un orchestrateur particulier.
- **Model-agnostic** : aucun modèle n'obtient plus de droits parce qu'il est supposé
  meilleur. Les droits dépendent de l'action, du contexte et des evals.
- **Eval-first** : une permission automatique n'est acceptable que si elle reste mesurable
  par des tests de policy et des scénarios de régression sécurité.

## 🛡️ Modèle de décision minimal

Une action n'est automatique que si toutes les questions suivantes reçoivent une réponse
explicite :

| Question | Exemple de réponse attendue |
| -------- | --------------------------- |
| Qui agit ? | `agent:code-writer` via un compte de service dédié |
| Sur quoi ? | branche `agent/*`, jamais `main` directement |
| Quelle capacité ? | `repo.write_branch`, pas `repo.merge_pr` |
| Dans quel sandbox ? | pas de secrets, réseau restreint, timeout borné |
| Quel signal d'eval ? | score sécurité au-dessus du seuil, aucune régression critique |
| Quel risque métier ? | faible -> `auto`, élevé -> `human`, interdit -> `deny` |

## 🔁 Pont avec les chapitres voisins

- Le chapitre 08 a appris à bloquer une régression mesurable. Ici, on ajoute les
  régressions de sécurité et de gouvernance.
- Le chapitre 10 branchera ces décisions dans la CI/CD : un changement de policy, de tool,
  de prompt ou de workflow devra déclencher les checks associés.

## ⚙️ Installation

Aucune installation supplémentaire. Ce chapitre manipule des fichiers déclaratifs et des
matrices de décision ; il ne demande ni nouveau package, ni commande d'exécution.

## 🔗 Ressources

- OWASP - LLM Top 10 : risques propres aux applications LLM.
- NIST AI Risk Management Framework : vocabulaire de gouvernance et de risque.
- GitHub Actions - Environments and deployment protection rules : exemple de validation
  humaine avant déploiement.

## 📝 Auto-évaluation

Tu peux passer au chapitre 10 quand tu réponds sans hésiter :

1. Pourquoi l'agent ne doit-il pas utiliser l'identité GitHub d'un humain ?
1. Quelle différence fais-tu entre `write branch`, `create PR`, `merge PR` et `deploy` ?
1. Quelles ressources doivent rester hors sandbox pour un coding agent ?
1. Quelle action doit être `deny` même si tous les tests passent ?
1. Comment transformer une règle human-in-the-loop en gate CI/CD vérifiable ?
