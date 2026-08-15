# 🚀 10 - Agentic CI/CD

> Livrable : **Factory v1.0** - une Factory dont chaque changement de prompt, tool,
> modèle, workflow ou policy déclenche les checks adaptés et peut bloquer la livraison.

## 🎯 Objectifs pédagogiques

- Faire passer la Factory du prototype gouverné manuellement à un système livré par CI/CD.
- Relier les acquis des chapitres 07 à 09 : traces, evals, budgets et policies deviennent
  des gates automatisés.
- Déclencher les evals dès qu'un changement peut modifier le comportement agentique :
  prompt, tool, modèle, workflow, policy, dataset ou seuil.
- Définir des règles de blocage lisibles : qualité sous le seuil, coût hors budget,
  régression de sécurité, changement non traçable ou approbation humaine manquante.
- Préparer le chapitre 11 : une PR générée automatiquement ne sera acceptable que si cette
  chaîne CI/CD sait l'arrêter.

## ✅ Prérequis

- Chapitre 09 (Policy Engine v0.9 : décisions, permissions, garde-fous et escalades).
- Comprendre les traces du chapitre 07 et les suites d'evals du chapitre 08.
- Savoir lire un workflow CI existant sans le confondre avec le runtime de l'agent.
- Durée estimée : **3 h** (1 h 15 théorie + 45 min étude de cas + 1 h exercices).

## 🚪 Gate du chapitre

> **Factory v1.0** : tu dois pouvoir expliquer, avant merge, quels changements déclenchent
> quelles evals, quels seuils bloquent la pipeline, qui peut approuver une exception et
> quelle trace prouve la décision.

## 🧭 Parcours pas à pas

| Étape | Support | Ce que tu fais |
| ----- | ------- | -------------- |
| 1 | [`slides/01-du-prototype-au-produit.md`](slides/01-du-prototype-au-produit.md) | Lire : pourquoi un agent a besoin de CI/CD spécifique |
| 2 | [`slides/02-declencheurs-evals.md`](slides/02-declencheurs-evals.md) | Lire : mapper changements -> suites d'evals |
| 3 | [`slides/03-pipeline-cible.md`](slides/03-pipeline-cible.md) | Lire : composer checks classiques et gates agentiques |
| 4 | [`slides/04-regles-de-blocage.md`](slides/04-regles-de-blocage.md) | Lire : bloquer sans rendre la livraison arbitraire |
| 5 | [`slides/05-pont-vers-pr-factory.md`](slides/05-pont-vers-pr-factory.md) | Lire : préparer les PR automatiques du chapitre 11 |
| 6 | [`demos/README.md`](demos/README.md) | Parcourir : étude de cas commentée d'une pipeline |
| 7 | [`exercices/README.md`](exercices/README.md) | Faire les exercices -> contrat CI/CD de **Factory v1.0** |
| 8 | [`solutions/README.md`](solutions/README.md) | Comparer après tentative |

## 📚 Plan théorique

1. Pourquoi les checks classiques ne suffisent pas pour un système agentique.
1. Artefacts versionnés : prompts, tools, modèles, workflows, policies, datasets,
   seuils, budgets et manifests de capabilities.
1. Déclencheurs d'evals : sélectionner la bonne suite sans tout relancer inutilement.
1. Pipeline cible : lint/tests, build, security, evals, budget, policy, audit et release.
1. Règles de blocage : seuils absolus, régressions, dérive de coût, sécurité et
   approbation humaine.
1. Traçabilité : relier commit, run CI, suite d'eval, policy decision et artefact livré.
1. Préparation du chapitre 11 : accepter ou refuser une PR produite par agent.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : le chapitre décrit des contrats CI/CD et des gates ; ils peuvent
  être portés dans GitHub Actions, GitLab CI, Azure Pipelines ou un orchestrateur interne.
- **Model-agnostic** : un changement de modèle passe par le Model Gateway et déclenche des
  evals de comportement, pas des conditions métier sur un fournisseur.
- **Eval-first** : aucune amélioration agentique n'est livrable sans comparaison mesurée
  avec la baseline et sans trace de décision.

## 🌉 Continuité avec les chapitres 09 et 11

Le chapitre 09 a défini ce que l'agent a le droit de faire. Le chapitre 10 décide quand ce
comportement peut être livré. Le chapitre 11 demandera à la Factory de créer elle-même des
PR : sans la chaîne de blocage construite ici, une PR automatique serait seulement une
accélération du risque.

```text
Policy Engine v0.9
      │
      ▼
Agentic CI/CD v1.0 ── checks classiques + evals + budgets + policies
      │
      ▼
PR Factory v1.1 ── PR générée, vérifiée, expliquée, puis bloquée ou proposée
```

## 🧾 Artefacts à traiter comme du code

| Artefact | Risque si non testé | Check minimal |
| -------- | ------------------- | ------------- |
| Prompt système | changement de comportement silencieux | evals de non-régression + review humaine si critique |
| Tool contract | action externe mal appelée | tests de validation + evals de tool use |
| Modèle ou route | qualité/coût différents | evals par segment + budget de coût |
| Workflow | ordre des décisions modifié | tests de graphe + evals end-to-end |
| Policy | permission trop large ou blocage excessif | tests de cas autorisés/refusés |
| Dataset d'eval | seuils trompeurs | validation de couverture + changelog |
| Seuil d'eval | gate trop permissif | justification + approbation |

## 🔁 Déclencheurs d'evals

La CI/CD ne doit pas relancer tout le système à chaque commit. Elle doit sélectionner les
suites proportionnées au risque.

| Changement détecté | Suite d'evals à lancer | Pourquoi |
| ------------------ | ---------------------- | -------- |
| `prompts/**` ou texte de prompt embarqué | intent, instruction following, safety, regression | le modèle peut décider autrement |
| `tools/**` ou schéma d'arguments | tool selection, validation, idempotence, erreurs | l'agent peut agir autrement |
| route ou profil modèle | quality by segment, cost, latency, fallback | le compromis qualité/coût change |
| graphe de workflow | end-to-end, rollback, human approval | l'ordre des gates change |
| policy ou permission | allow/deny matrix, escalation, audit | le périmètre d'action change |
| dataset ou seuil | meta-eval, couverture, stabilité | le thermomètre change |

## 🚦 Règles de blocage minimales

Une pipeline agentique doit bloquer au moins dans ces cas :

- une eval critique passe sous son seuil absolu ;
- une métrique régresse au-delà de la tolérance déclarée par rapport à la baseline ;
- le coût par tâche réussie dépasse le budget du segment ;
- une policy attendue `deny` devient `allow`, ou l'inverse sans approbation ;
- une trace d'eval ne permet pas de relier résultat, prompt, modèle, tools et commit ;
- une exception est demandée sans propriétaire, justification et date d'expiration.

## 🧩 Contrat de pipeline cible

Le livrable du chapitre n'est pas un outil magique, mais un contrat clair :

```text
change detection
  -> checks classiques du repo
  -> sélection des suites d'evals
  -> exécution avec traces et budgets
  -> comparaison à la baseline
  -> policy decision : pass / block / needs-human-approval
  -> publication des artefacts de décision
```

Dans ce dépôt, les checks existants du site et des liens restent la base. La Factory ajoute
ses gates agentiques sans remplacer les garde-fous déjà présents.

## 📦 Livrable

**Factory v1.0** - une spécification complète de CI/CD agentique contenant :

- une matrice `changement -> evals déclenchées` ;
- un ordre de pipeline qui combine checks classiques, evals, sécurité, budget et policies ;
- des seuils de blocage et de régression ;
- un format de décision `pass` / `block` / `needs-human-approval` ;
- une stratégie d'exception limitée, auditée et expirante ;
- les artefacts nécessaires pour qu'une future PR automatique soit vérifiable.

## 🔗 Ressources

- [`../07-observability-tracing/`](../07-observability-tracing/) - traces nécessaires aux
  décisions de CI.
- [`../08-evaluation-engineering/`](../08-evaluation-engineering/) - suites d'evals et
  baselines.
- [`../09-security-governance/`](../09-security-governance/) - policies, permissions et
  escalades.
- GitHub Actions - workflows, checks requis et artefacts de run.

## 📝 Auto-évaluation

Tu peux passer au chapitre 11 quand tu réponds sans hésiter :

1. Quel changement doit déclencher une eval de prompt, de tool, de modèle ou de policy ?
1. Quelle différence fais-tu entre un test classique et une eval agentique ?
1. Quand faut-il bloquer même si les tests unitaires sont verts ?
1. Quelle trace prouve qu'une exception humaine était légitime ?
1. Pourquoi une PR automatique sans gate d'eval est-elle dangereuse ?
