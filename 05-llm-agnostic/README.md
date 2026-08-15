# 🧠 05 - LLM Agnostic : découpler l'agent du modèle

> Livrable : **Model Gateway v0.5** - la même Agentic CI/CD Factory fonctionne avec un
> modèle cloud et un modèle local, sans modification du code métier de l'agent.

## 🎯 Objectifs pédagogiques

- Comprendre pourquoi une Factory agentique ne doit jamais dépendre directement d'une API
  de modèle.
- Définir un contrat `LLMProvider` commun : génération, comptage approximatif des tokens,
  capacités et erreurs normalisées.
- Placer un **Model Gateway** entre l'agent, le workflow, les tools MCP et les fournisseurs
  réels.
- Comparer les différences utiles entre Anthropic, APIs compatibles OpenAI, Ollama et
  vLLM, sans transformer ces différences en `if provider == ...` dans le code métier.
- Sélectionner un modèle par configuration et vérifier la non-régression quand on le
  remplace.

## ✅ Prérequis

- Chapitre 04 : tools et contexte exposés via MCP, sans modifier le workflow.
- Savoir expliquer le flux `REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW ->
  PR`.
- Disposer d'au moins un modèle cloud **ou** local pour raisonner sur les écarts de
  capacités.
- Durée estimée : **3 h** (1 h théorie + 1 h lecture guidée + 1 h exercices).

## 🚪 Gate du chapitre

> **Gate 3** : tu dois pouvoir changer le modèle actif par configuration, relancer les
> mêmes scénarios de la Factory, et montrer que le code métier de l'agent n'a pas changé.

## 🧭 Parcours pas à pas

| Étape | Support                                                                 | Ce que tu fais                                      |
| ----- | ----------------------------------------------------------------------- | --------------------------------------------------- |
| 1     | [`slides/01-probleme-couplage.md`](slides/01-probleme-couplage.md)     | Lire : où naît le couplage au provider              |
| 2     | [`slides/02-contrat-llm-provider.md`](slides/02-contrat-llm-provider.md) | Lire : le contrat minimal commun                    |
| 3     | [`slides/03-model-gateway.md`](slides/03-model-gateway.md)             | Lire : gateway, registry, config, erreurs           |
| 4     | [`slides/04-differences-provider.md`](slides/04-differences-provider.md) | Lire : différences sans fuite dans l'agent          |
| 5     | [`slides/05-non-regression.md`](slides/05-non-regression.md)           | Lire : même scénario, plusieurs modèles             |
| 6     | [`demos/README.md`](demos/README.md)                                   | Parcourir : démonstration guidée de swap            |
| 7     | [`exercices/README.md`](exercices/README.md)                           | Faire les 3 exercices -> **Model Gateway v0.5**     |
| 8     | [`solutions/README.md`](solutions/README.md)                           | Comparer après coup : pas avant d'avoir tenté       |

## 📚 Plan théorique

1. Le problème : l'agent se fragilise quand il connaît le SDK, le format de tool calling ou
   les erreurs d'un fournisseur précis.
1. Le contrat `LLMProvider` : entrée normalisée, sortie normalisée, capacités déclarées,
   limites connues.
1. Le Model Gateway : point unique de sélection, adaptation, journalisation minimale et
   normalisation des erreurs.
1. Les différences de providers : contexte, streaming, tool calling, JSON strict, latence,
   coût, hébergement et confidentialité.
1. La sélection par configuration : changer le modèle actif sans modifier `agent.py`, les
   nodes du workflow ou les clients MCP.
1. La non-régression : rejouer les mêmes scénarios, comparer les invariants métier, puis
   préparer le routing du chapitre 06.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : le gateway est une frontière d'architecture, pas un SDK imposé.
- **Model-agnostic** : le code métier dépend d'un contrat stable, jamais d'un modèle ou
  d'un fournisseur nommé.
- **Eval-first** : les swaps de modèles se prouvent par des scénarios de non-régression ;
  au chapitre 06, ces mêmes mesures alimenteront le routing.

## 🌉 Continuité avec les chapitres 04 et 06

Le chapitre 04 a rendu les tools interchangeables grâce à MCP. Le chapitre 05 applique la
même idée côté modèle : **l'agent ne parle plus à un fournisseur, il parle à un contrat**.

Le chapitre 06 ajoutera une décision supplémentaire : choisir automatiquement le bon
modèle selon le budget, la complexité et le risque. Pour y arriver proprement, le chapitre
05 doit d'abord rendre le changement de modèle banal, explicite et testable.

## 🧩 Architecture cible

```text
Workflow / Agent nodes
        │
        ▼
  Model Gateway
   ├── Provider Anthropic
   ├── Provider OpenAI-compatible
   ├── Provider Ollama
   └── Provider vLLM
        │
        ▼
  Réponse normalisée + capacités + erreurs normalisées
```

Le point clé : les nodes `ANALYZE`, `PLAN`, `IMPLEMENT`, `TEST` et `REVIEW` demandent une
capacité (`generate`, `tool_calling`, `json_output`) ; ils ne choisissent pas un SDK.

## ⚙️ Contrat minimal attendu

Le contrat peut être implémenté en Python comme une interface ou un protocole. Ce qui
compte ici est la frontière :

```text
LLMProvider.generate(messages, tools, response_format) -> LLMResponse
LLMProvider.count_tokens(messages) -> TokenEstimate
LLMProvider.capabilities() -> ModelCapabilities
```

La réponse normalisée contient au minimum : texte, tool calls éventuels, raison d'arrêt,
usage de tokens si disponible, et métadonnées non métier. Les erreurs normalisées
distinguent au moins : configuration invalide, authentification, quota, timeout, capacité
non supportée et réponse invalide.

## 🧪 Non-régression attendue

Un swap de modèle est acceptable si les invariants métier restent vrais :

- la demande est analysée en tâches vérifiables ;
- le plan respecte les étapes de la Factory ;
- les tools MCP appelés restent autorisés ;
- les tests ou checks existants restent la source de vérité ;
- les sorties structurées restent parseables quand un format structuré est demandé.

On ne cherche pas encore le modèle le moins cher ou le plus rapide : ce sera le sujet du
chapitre 06. Ici, on prouve d'abord que **changer de modèle ne casse pas l'agent**.

## 🔗 Ressources

- Anthropic - [Messages API](https://docs.anthropic.com/en/api/messages)
- OpenAI - [API reference](https://platform.openai.com/docs/api-reference)
- Ollama - [API](https://github.com/ollama/ollama/blob/main/docs/api.md)
- vLLM - [OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html)

## 📝 Auto-évaluation

Tu peux passer au chapitre 06 quand tu réponds sans hésiter :

1. Quelle différence fais-tu entre un provider, un modèle et un gateway ?
1. Quelles informations doivent être dans `ModelCapabilities` ?
1. Pourquoi le code métier ne doit-il jamais tester `provider == "anthropic"` ?
1. Quels invariants prouvent qu'un swap de modèle n'a pas cassé la Factory ?
1. Quelle décision manque encore pour passer d'un gateway à un router ?
