# ✅ Solutions - Model Gateway v0.5

## 🎯 Intention

Ces solutions donnent une cible de conception. Elles ne remplacent pas ton implémentation :
compare-les après avoir tenté les exercices.

## 🧩 Solution 1 - Contrat provider

Un contrat acceptable expose au minimum :

```text
generate(messages, tools, response_format) -> LLMResponse
count_tokens(messages) -> TokenEstimate
capabilities() -> ModelCapabilities
```

`LLMResponse` contient :

- le texte produit ;
- les tool calls éventuels ;
- la raison d'arrêt ;
- l'usage de tokens si disponible ;
- des métadonnées techniques qui ne pilotent pas le métier.

`ModelCapabilities` contient : contexte maximal, support du tool calling, support du JSON
strict, streaming, vision éventuelle, localité des données et limites connues.

## 🚪 Solution 2 - Placement du gateway

Dépendances souhaitées :

```text
Workflow nodes -> Model Gateway -> LLMProvider concret -> SDK/API provider
```

Dépendances à éviter :

```text
Workflow nodes -> SDK/API provider
Workflow nodes -> if provider == "..."
Tools MCP -> choix du modèle
```

Le gateway lit la configuration, choisit l'adaptateur, vérifie les capacités demandées et
retourne une réponse normalisée. Les providers concrets sont les seuls endroits qui
connaissent les formats spécifiques.

## 🔁 Solution 3 - Matrice de non-régression

| Scénario | Invariant | Cloud | Local | Verdict |
| -------- | --------- | ----- | ----- | ------- |
| Analyse simple | Les tâches sont actionnables et vérifiables. | OK | OK | Pass |
| Plan avec MCP | Aucun tool hors périmètre n'est demandé. | OK | OK | Pass |
| Sortie structurée | Le JSON attendu est parseable. | OK | À corriger | Fail |

Dans cet exemple, le troisième scénario échoue pour le modèle local. La bonne correction
n'est pas de modifier le node métier : il faut soit renforcer l'adaptateur, soit déclarer
que le modèle ne supporte pas cette capacité, soit choisir une autre configuration.

## ✅ Checklist finale

- Le workflow ne contient aucun import de SDK provider.
- Le modèle actif est choisi par configuration.
- Les capacités sont déclarées et vérifiées avant usage.
- Les erreurs provider sont normalisées.
- Le swap de modèle est validé par des invariants métier.
- Les métriques collectées sont suffisantes pour préparer le routing du chapitre 06.
