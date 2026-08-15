# 🧠 03.3 - Patterns d'orchestration utiles

## 🧵 Sequential workflow

```text
A -> B -> C -> D
```

À utiliser quand chaque étape dépend clairement de la précédente. C'est le cœur du flux
`REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW -> PR`.

Avantage : simple à debugger. Risque : trop linéaire si certaines tâches peuvent être
faites en parallèle.

## 🔀 Router

```text
request -> classify -> bugfix | feature | documentation
```

Le routeur choisit une branche parmi des options écrites à l'avance. Le modèle peut aider
à classer, mais il ne crée pas de branche nouvelle à l'exécution.

Dans la Factory, le routeur arrivera progressivement : petite correction, ajout de feature,
refactor, documentation, investigation.

## 🧬 Parallel fan-out / fan-in

```text
          -> review_code ----
changes --|                 |-> synthèse
          -> review_tests ---
```

Utile quand plusieurs vérifications indépendantes lisent le même artefact. Le fan-in doit
réconcilier les résultats dans une sortie unique, par exemple `review.status`.

## 🧪 Evaluator-optimizer

```text
generate -> evaluate -> improve -> evaluate -> stop
```

Le générateur produit une proposition. L'évaluateur la juge avec des critères explicites.
L'optimiseur corrige si le budget le permet.

Dans ce chapitre, on l'applique modestement : `IMPLEMENT -> TEST -> IMPLEMENT` au maximum
une ou deux fois, pas une boucle infinie.

## 🕹️ Orchestrator-workers

```text
orchestrator -> worker_plan
             -> worker_code
             -> worker_review
```

L'orchestrateur découpe et coordonne. Les workers ont un rôle étroit, un budget et des
permissions différentes. C'est la base du workflow multi-agents annoncé par le Gate 2.

## ⚖️ Choisir le pattern minimal

| Besoin                                  | Pattern recommandé        |
| --------------------------------------- | ------------------------- |
| Étapes connues et dépendantes           | sequential                |
| Demandes de types différents            | router                    |
| Vérifications indépendantes             | parallel fan-out/fan-in   |
| Amélioration bornée par critères        | evaluator-optimizer       |
| Plusieurs rôles avec permissions fortes | orchestrator-workers      |

## 💡 À retenir

1. Un pattern est un compromis coût / robustesse / observabilité.
1. Les boucles doivent être bornées par budget, pas par optimisme.
1. Le meilleur workflow est celui qu'un humain peut relire sans exécuter le modèle.

-> Slide suivante : [`04-checkpoints-human-approval.md`](04-checkpoints-human-approval.md)
