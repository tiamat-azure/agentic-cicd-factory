# 🎬 Demos - chapitre 04

La demo de ce chapitre est une **trace de migration** : elle montre qu'un workflow peut
rester identique alors que ses capacités passent de tools locaux à MCP.

## 🧭 Ordre de lecture

1. Lire la demande de départ.
1. Repérer l'ancien tool natif.
1. Repérer le serveur MCP de remplacement.
1. Vérifier que le node du workflow ne change pas.
1. Vérifier que les permissions deviennent plus explicites.

## 🧵 Trace avant / après

```text
[REQUEST]
input: "Valide le diff, lance les tests et prépare la PR."

[AVANT]
node: IMPLEMENT / TEST / PR
tools natifs:
  - read_file
  - run_tests
  - create_pr
problème: capacités dispersées dans l'agent

[APRÈS]
node: IMPLEMENT / TEST / PR
tools MCP:
  - filesystem.read
  - ci.run_tests
  - github.create_pr
problème résolu: capacités standardisées et négociées

[OBSERVATION]
workflow inchangé, adaptateurs remplacés
```

## 🔍 Ce qu'il faut observer

- le host garde la responsabilité d'orchestration ;
- le serveur expose une capacité, pas une politique métier ;
- le chemin de migration peut être progressif ;
- la sécurité est plus lisible car la frontière est explicite.
