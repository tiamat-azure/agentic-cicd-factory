# 🎬 Demos - chapitre 03

Ce chapitre ne fournit pas encore de runtime imposé. La demo est une **trace commentée** :
elle montre ce que le workflow doit rendre visible avant de l'implémenter dans un framework
comme LangGraph.

## 🧭 Ordre de lecture

1. Lis la trace ci-dessous comme si elle provenait d'un orchestrateur.
1. Repère les champs du state écrits à chaque étape.
1. Vérifie où le graphe s'arrête pour attendre un humain.
1. Note ce qui pourra devenir un tool MCP au chapitre 04.

## 🧵 Trace commentée

```text
[REQUEST]
input: "Ajoute une validation de nom de branche avant création de PR."
state.request = { text, author, created_at }

[ANALYZE]
reads: request
writes: analysis = {
  intent: "add branch-name validation",
  likely_files: ["tools/git.py", "agent.py"],
  risks: ["bloquer des branches valides", "message d'erreur peu exploitable"]
}

[PLAN]
reads: request, analysis
writes: plan = {
  steps: [
    "ajouter une fonction de validation",
    "appeler la validation avant PR",
    "ajouter un test nominal et un test rejet"
  ],
  acceptance: ["branche feat/... acceptée", "branche main rejetée"]
}
checkpoint: plan_created

[APPROVE_PLAN]
status: waiting_human
human_decision: approved

[IMPLEMENT]
reads: plan
writes: changes = { files_changed, diff_summary }

[TEST]
reads: changes, plan
writes: test_report = { command: "test suite du chapitre", status: "green" }
checkpoint: tests_green

[REVIEW]
reads: plan, changes, test_report
writes: review = { status: "approved", notes: [] }

[APPROVE_PR]
status: waiting_human
human_decision: approved

[PR]
writes: pr_draft = { title, body, checklist }
status: ready_for_pr
```

## 🔍 Ce qu'il faut observer

- `IMPLEMENT` ne commence qu'après approbation du plan.
- `TEST` écrit un rapport, pas seulement du texte libre.
- `REVIEW` relit le plan validé : il ne juge pas une solution hors scope.
- `PR` prépare une proposition ; le merge n'appartient pas encore à ce chapitre.

## 🧪 Variante à simuler

Change mentalement `TEST.status` en `red`. Le conditional edge doit choisir une des trois
issues :

1. retour vers `IMPLEMENT` si le budget de correction reste disponible ;
1. arrêt `tests_failed` si l'erreur est bloquante ;
1. demande humaine si le plan validé ne couvre pas la correction nécessaire.
