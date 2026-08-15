# 💰 06 - Token Engineering & Model Routing

> Livrable : **Model Router v0.6** - un routeur de modèles qui mesure chaque run,
> applique des budgets, choisit un modèle via le Model Gateway, puis calcule le coût par
> tâche réussie.

## 🎯 Objectifs pédagogiques

- Instrumenter chaque run : tokens d'entrée, de sortie et de cache, tool calls,
  itérations, latence, coût, résultat et erreur éventuelle.
- Transformer ces métriques en budgets déclaratifs : itérations, tool calls, tokens,
  coût, retries et fallback.
- Classifier une tâche avant exécution : simple, medium ou complex, sans dépendre d'un
  fournisseur de modèle.
- Router vers un modèle local ou cloud via le Model Gateway du chapitre 05.
- Définir une retry policy sûre : retenter seulement les erreurs transitoires et
  idempotentes.
- Optimiser le **coût par tâche réussie**, pas le nombre brut de tokens.

## ✅ Prérequis

- Chapitre 05 (Model Gateway v0.5 : même agent, plusieurs fournisseurs LLM).
- Comprendre le workflow `REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW -> PR`.
- Savoir lire une trace simple : entrée, action, observation, statut.
- Durée estimée : **3 h** (1 h théorie + 45 min conception + 1 h exercices + 15 min
  synthèse).

## 🚪 Gate du chapitre

> **Gate 4 (partie 1/3)** : tu dois pouvoir prouver qu'une stratégie de routing respecte
> ses budgets et réduit le coût par tâche réussie, sans masquer les échecs ni changer le
> code métier de l'agent.

## 🧭 Parcours pas à pas

| Étape | Support                                                                        | Ce que tu fais                                      |
| ----- | ------------------------------------------------------------------------------ | --------------------------------------------------- |
| 1     | [`slides/01-instrumentation-tokens.md`](slides/01-instrumentation-tokens.md)   | Lire : mesurer avant d'optimiser                    |
| 2     | [`slides/02-budgets-et-politiques.md`](slides/02-budgets-et-politiques.md)     | Lire : budgets comme policy gates                   |
| 3     | [`slides/03-classification-et-routing.md`](slides/03-classification-et-routing.md) | Lire : classifier puis router via le gateway        |
| 4     | [`slides/04-fallback-retry-cost.md`](slides/04-fallback-retry-cost.md)         | Lire : fallback, retry et coût par succès           |
| 5     | [`demos/README.md`](demos/README.md)                                           | Parcourir : traces et décisions commentées          |
| 6     | [`exercices/README.md`](exercices/README.md)                                   | Faire les 3 exercices -> **Model Router v0.6**      |
| 7     | [`solutions/README.md`](solutions/README.md)                                   | Comparer après tentative                            |
| 8     | [`../07-observability-tracing/`](../07-observability-tracing/)                 | Enchaîner : transformer ces événements en traces    |

## 📚 Plan théorique

1. Pourquoi l'optimisation commence par l'instrumentation, pas par la réduction de
   contexte.
1. Vocabulaire minimal : `input_tokens`, `output_tokens`, `cached_tokens`, `tool_calls`,
   `iterations`, `latency_ms`, `cost_usd`, `success`, `failure_reason`.
1. Budgets d'agent : limites d'exécution, de contexte, de coût et de retries.
1. Classification de tâche : signaux simples, matrice de décision, override humain.
1. Routing model-agnostic : labels de capacité, pas `if provider == ...` dans le métier.
1. Fallback et retry policy : quand retenter, quand escalader, quand arrêter.
1. Coût par tâche réussie : mesurer sur un lot de tâches, pas sur un run isolé.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : le chapitre décrit des métriques, contrats et policies
  applicables avec ou sans runtime agentique.
- **Model-agnostic** : le routeur choisit des profils (`local-small`, `local-large`,
  `cloud-frontier`) exposés par le Model Gateway, jamais un fournisseur codé en dur.
- **Eval-first** : les métriques produites ici deviennent les traces du chapitre 07 et les
  critères d'évaluation du chapitre 08.

## 🌉 Continuité avec les chapitres 05 et 07

Le chapitre 05 a créé une frontière nette : l'agent parle à un **Model Gateway**, pas à une
API de modèle. Le chapitre 06 ajoute une décision avant l'appel : **quel profil utiliser,
avec quel budget, et quelle stratégie de fallback ?**

Le chapitre 07 ne changera pas ces décisions. Il les rendra observables dans des traces
corrélées : modèle choisi, prompt envoyé, tools appelés, latence, coût, erreur et résultat.

```text
Agent / Workflow
      │
      ▼
Task Classifier
      │
      ▼
Model Router ── budgets / retry / fallback
      │
      ▼
Model Gateway ── local-small / local-large / cloud-frontier
      │
      ▼
Run Metrics ── tokens / latency / cost / success
```

## 📏 Vocabulaire de mesure

| Champ | Sens | Utilisation au chapitre 07 |
| ----- | ---- | -------------------------- |
| `run_id` | identifiant stable d'une exécution | corrélation de trace |
| `task_type` | classe fonctionnelle : analyse, plan, code, review | regroupement dashboard |
| `task_class` | complexité : `simple`, `medium`, `complex` | comparaison par segment |
| `route` | profil choisi : `local-small`, `local-large`, `cloud-frontier` | explication du coût |
| `model` | modèle réellement appelé par le gateway | audit et comparaison |
| `input_tokens` | tokens envoyés au modèle | budget de contexte |
| `output_tokens` | tokens générés par le modèle | budget de sortie |
| `cached_tokens` | tokens facturés ou comptés comme cache | efficacité du cache |
| `tool_calls` | nombre d'actions externes demandées | contrôle de boucle |
| `iterations` | tours agentiques consommés | arrêt et runaway detection |
| `latency_ms` | durée de l'appel ou du run | SLO et debug |
| `cost_usd` | coût estimé du run | budget et reporting |
| `success` | résultat métier vérifié, pas seulement absence d'exception | coût par succès |
| `failure_reason` | `budget_exhausted`, `tool_error`, `model_error`, `quality_gate_failed`, ... | analyse des échecs |
| `retry_count` | retries consommés | détection de fragilité |
| `fallback_count` | escalades vers un autre profil | coût de la robustesse |

## 🧾 Budget minimal

Un budget doit être explicite, versionné avec la Factory et appliqué par le runtime avant
que le modèle ne puisse dériver.

```yaml
agent:
  max_iterations: 8
  max_tool_calls: 20

tokens:
  max_input: 30000
  max_output: 8000

cost:
  max_run_usd: 0.25

retry:
  max_attempts: 2
  retry_on:
    - transient_provider_error
    - rate_limit
    - invalid_structured_output

fallback:
  escalate_on:
    - missing_capability
    - context_window_exceeded
    - quality_gate_failed
```

La règle : **un dépassement de budget est un résultat explicable**, pas une erreur cachée.

## 🔀 Matrice de routing

| Classe | Signaux typiques | Route par défaut | Fallback autorisé |
| ------ | ---------------- | ---------------- | ----------------- |
| `simple` | question courte, résumé, extraction structurée, pas de modification | `local-small` | `local-large` si sortie invalide |
| `medium` | analyse multi-fichiers, plan, refactor borné, review simple | `local-large` | `cloud-frontier` si capacité ou qualité insuffisante |
| `complex` | architecture, forte ambiguïté, sécurité, incident, décision coûteuse | `cloud-frontier` | arrêt ou humain, pas d'escalade infinie |

Le routeur ne remplace pas les evals. Il propose une hypothèse de coût/qualité que les
chapitres 07 et 08 permettront de vérifier.

## 💸 Coût par tâche réussie

Mesurer seulement les tokens pousse à choisir le modèle le moins cher, même s'il échoue et
force des retries. La métrique utile est :

```text
cost_per_success = somme(cost_usd de tous les runs) / nombre de tâches réussies
```

À comparer par classe de tâche : un modèle local peut être excellent sur `simple`, mauvais
sur `complex`, et donc rentable seulement si le routeur sait dire non au bon moment.

## 📦 Livrable

**Model Router v0.6** - une spécification complète contenant :

- un schéma de métriques par run ;
- un budget d'agent et de coût ;
- un classifier `simple` / `medium` / `complex` ;
- une matrice de routing vers `local-small`, `local-large`, `cloud-frontier` ;
- une retry policy limitée aux erreurs transitoires et idempotentes ;
- une fallback policy bornée ;
- un calcul de coût par tâche réussie sur un petit lot de scénarios.

## 🔗 Ressources

- [`../05-llm-agnostic/`](../05-llm-agnostic/) - Model Gateway et profils de modèles.
- [`../07-observability-tracing/`](../07-observability-tracing/) - traces et dashboard à
  partir des métriques de ce chapitre.

## 📝 Auto-évaluation

Tu peux passer au chapitre 07 quand tu réponds sans hésiter :

1. Pourquoi l'optimisation des tokens commence-t-elle par `success` et `failure_reason` ?
1. Quelle différence fais-tu entre retry et fallback ?
1. Quelles erreurs ne dois-tu jamais retenter automatiquement ?
1. Comment éviter qu'un routeur devienne dépendant d'un fournisseur LLM ?
1. Pourquoi un modèle moins cher par token peut-il coûter plus cher par tâche réussie ?
