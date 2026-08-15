# 🛤️ 10.3 - Pipeline cible d'une Factory agentique

## 🧩 Ordre recommandé

```text
1. Detect changes
2. Run classical checks
3. Select eval suites
4. Run evals with traces
5. Check cost and latency budgets
6. Apply policy gates
7. Publish decision artifacts
8. Release or block
```

## ✅ Checks classiques

Ils restent indispensables : format, tests, sécurité de dépendances, build du site ou de
l'artefact applicatif. Ils répondent à : « le système est-il techniquement livrable ? ».

## 🤖 Gates agentiques

Ils répondent à : « le comportement agentique est-il encore acceptable ? ».

| Gate | Entrée | Sortie |
| ---- | ------ | ------ |
| Eval quality | suite + baseline | score, régression, exemples échoués |
| Cost budget | traces d'eval | coût total, coût par succès |
| Policy gate | décision simulée ou réelle | `allow`, `deny`, `escalate` |
| Audit gate | artefacts de run | lien commit -> eval -> décision |

## 📦 Artefacts à publier

Une pipeline utile laisse des preuves :

- résumé des changements détectés ;
- suites d'evals exécutées et raisons ;
- scores et écarts à la baseline ;
- budget consommé ;
- décisions de policy ;
- exceptions humaines éventuelles.

## ⚠️ Erreur fréquente

Ne mets pas les evals après le déploiement « pour observer ». Les evals de non-régression
sont un gate de livraison, pas seulement un dashboard.
