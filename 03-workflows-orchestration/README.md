# 🕸️ 03 - Workflows & orchestration

> Livrable : **Factory v0.3** - un workflow déterministe, checkpointé, avec approbation
> humaine, qui transforme une demande en changement prêt à ouvrir en PR.

## 🎯 Objectifs pédagogiques

- Passer du Coding Agent du chapitre 02 à une **usine orchestrée** : plusieurs étapes,
  responsabilités explicites, état partagé et sorties vérifiables.
- Comprendre les concepts de graphe : `State`, `Node`, `Edge`, `Conditional Edge`,
  checkpoint, reprise et human approval.
- Savoir quand choisir un workflow plutôt qu'un agent libre : coût, auditabilité,
  sécurité, qualité de debug.
- Concevoir le flux fil rouge `REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW -> PR`.
- Préparer le chapitre 04 : remplacer certaines actions locales par des tools exposés via
  MCP sans changer l'architecture du workflow.

## ✅ Prérequis

- Chapitre 02 (Agent v0.2 - Coding Agent : tools filesystem, git, shell/test, validation,
  permissions).
- Savoir lire une trace d'exécution simple : entrée, action, observation, statut.
- Durée estimée : **3 h** (1 h théorie + 45 min conception + 1 h exercices + 15 min
  synthèse).

## 🚪 Gate du chapitre

> **Gate 2 (partie 1/2)** : tu dois pouvoir dessiner et spécifier un workflow multi-rôles
> borné, avec checkpoints et validation humaine, puis expliquer ce qui est déterministe et
> ce qui reste confié au modèle.

## 🧭 Parcours pas à pas

| Étape | Support                                                                                      | Ce que tu fais                                      |
| ----- | -------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| 1     | [`slides/01-pourquoi-orchestrer.md`](slides/01-pourquoi-orchestrer.md)                       | Lire : pourquoi sortir d'une boucle agent unique    |
| 2     | [`slides/02-graphe-state-node-edge.md`](slides/02-graphe-state-node-edge.md)                 | Lire : vocabulaire de graphe et contrat de state    |
| 3     | [`slides/03-patterns-orchestration.md`](slides/03-patterns-orchestration.md)                 | Lire : sequential, router, parallel, evaluator      |
| 4     | [`slides/04-checkpoints-human-approval.md`](slides/04-checkpoints-human-approval.md)         | Lire : reprise, audit, approbation humaine          |
| 5     | [`slides/05-factory-v03.md`](slides/05-factory-v03.md)                                      | Lire : workflow cible de la Factory v0.3            |
| 6     | [`demos/README.md`](demos/README.md)                                                        | Parcourir : trace commentée d'une exécution         |
| 7     | [`exercices/README.md`](exercices/README.md)                                                | Faire les 3 exercices -> **Factory v0.3**           |
| 8     | [`solutions/README.md`](solutions/README.md)                                                | Comparer après coup : pas avant d'avoir tenté       |

## 📚 Plan théorique

1. Limites d'un agent de codage seul : responsabilités mélangées, reprise difficile,
   décisions non auditables.
1. Graphe d'orchestration : state partagé, nodes typés, edges explicites, branches
   conditionnelles.
1. Patterns utiles : chaîne séquentielle, routeur, parallélisme borné, evaluator-optimizer,
   superviseur.
1. Checkpoints : sauvegarder un état stable, reprendre après erreur, expliquer un run.
1. Human approval : arrêter le graphe au bon endroit, demander une décision minimale,
   reprendre sans rejouer ce qui est déjà validé.
1. Construction du flux `REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW -> PR`.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : LangGraph est cité comme runtime possible, mais le chapitre
  enseigne d'abord le pattern architectural. Le livrable est une spécification de graphe
  portable.
- **Model-agnostic** : les nodes qui appellent un modèle passent par l'abstraction du
  chapitre 01/02. Aucun branchement métier ne dépend d'un fournisseur LLM.
- **Eval-first** : pas encore de framework d'evals, mais chaque node produit une sortie
  structurée et checkpointée. Ces artefacts deviendront traces au ch. 07 et cas d'eval au
  ch. 08.

## 🧩 Workflow cible

```text
REQUEST
  -> ANALYZE
  -> PLAN
  -> APPROVE_PLAN? ── human reject ──> STOP_NEEDS_CLARIFICATION
  -> IMPLEMENT
  -> TEST
  -> REVIEW
  -> APPROVE_PR? ───── human reject ──> STOP_CHANGES_REQUESTED
  -> PR
```

La règle importante : **le graphe décide du prochain node ; le modèle ne décide que du
contenu demandé par son node**. C'est ce qui rend le coût, les permissions et la reprise
maîtrisables.

## 📦 Livrable

**Agentic CI/CD Factory v0.3** - une spécification complète de workflow contenant :

- un état partagé minimal (`request`, `analysis`, `plan`, `changes`, `test_report`,
  `review`, `pr_draft`, `status`) ;
- un contrat d'entrée/sortie pour chaque node ;
- deux checkpoints obligatoires : après `PLAN`, après `TEST` ;
- deux décisions humaines : validation du plan, validation avant PR ;
- une trace textuelle permettant de rejouer mentalement le run sans accéder au modèle.

## 🔗 Ressources

- Anthropic -
  [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)
  (patterns workflow / agent / evaluator).
- Hugging Face -
  [Introduction to LangGraph](https://huggingface.co/learn/agents-course/unit2/langgraph/introduction)
  (vocabulaire StateGraph, nodes, edges, checkpoints).

## 📝 Auto-évaluation

Tu peux passer au chapitre 04 quand tu réponds sans hésiter :

1. Quelle décision appartient au graphe, et quelle décision appartient au modèle ?
1. Que doit contenir un checkpoint pour reprendre sans rejouer tout le workflow ?
1. Où places-tu l'approbation humaine dans le flux, et pourquoi pas plus tard ?
1. Comment empêcher `IMPLEMENT` de modifier le plan validé sans repasser par `PLAN` ?
1. Quelle partie du workflow remplaceras-tu par un serveur MCP au chapitre 04 ?
