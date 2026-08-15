# 🔭 07 - Observability & Tracing

> Livrable : **Observability v0.7** - un socle de tracing qui permet d'expliquer
> n'importe quel run : qui a décidé quoi, dans quel ordre, avec quelle latence, combien
> de tokens et pourquoi le coût final a été ce qu'il est.

## 🎯 Objectifs pédagogiques

- Distinguer logging, métriques et tracing.
- Faire produire à chaque run une trace corrélée : agent, modèle, prompt, tool calls,
  spans, tokens, latence, erreurs, coût et résultat.
- Répondre sans relancer l'agent à la question : « pourquoi cette exécution a coûté X et
  pris Y secondes ? ».
- Préparer le passage au chapitre 08 : transformer les traces en matière première
  d'évaluation.

## ✅ Prérequis

- Chapitre 06 (Model Router v0.6).
- Savoir lire un journal d'exécution et relier une décision à une mesure.
- Durée estimée : **2 h 30** (1 h 15 théorie + 45 min lecture de traces + 30 min
  exercices).

## 🚪 Gate du chapitre

> Tu dois pouvoir prendre une trace de run et reconstruire le chemin complet :
> modèle choisi, itérations, tool calls, points de latence, consommation de tokens et
> raisons du coût total.

## 🗺️ Parcours pas à pas

| Étape | Support                                                        | Ce que tu fais                                    |
| ----- | -------------------------------------------------------------- | ------------------------------------------------- |
| 1     | [`slides/01-tracer-un-run.md`](slides/01-tracer-un-run.md)    | Lire : pourquoi logging ≠ tracing                 |
| 2     | [`slides/02-spans-et-correlation.md`](slides/02-spans-et-correlation.md) | Lire : relier run, span et tool call              |
| 3     | [`slides/03-cout-latence-tokens.md`](slides/03-cout-latence-tokens.md) | Lire : attribuer coût, latence et tokens          |
| 4     | [`slides/04-du-trace-au-dashboard.md`](slides/04-du-trace-au-dashboard.md) | Lire : passer de la trace au diagnostic           |
| 5     | [`exercices/`](exercices/)                                    | Faire les exercices -> base de l'eval du ch. 08   |
| 6     | [`solutions/`](solutions/)                                    | Comparer et corriger                              |

## 📚 Plan théorique

1. Pourquoi le logging seul ne suffit pas.
1. Anatomie d'une trace agentique : `trace_id`, `span_id`, `parent_span_id`, step,
   tool, modèle, tokens, latence, coût.
1. Corrélation entre décision du modèle et effets observés dans le runtime.
1. Attribution du coût : modèle, retries, tool calls, prompt growth, cache.
1. Du diagnostic ponctuel au dashboard minimal.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : on parle de traces, spans et attributs, pas d'un backend
  d'observabilité particulier.
- **Model-agnostic** : on mesure les appels modèle, pas un fournisseur en dur.
- **Eval-first** : la trace est la source de vérité qui alimentera les datasets du
  chapitre 08.

## 🔁 Pont avec les chapitres voisins

- Le chapitre 06 a introduit les budgets ; ici on les rend explicables.
- Le chapitre 08 transformera ces traces en critères mesurables et en régressions.

## 🔗 Ressources

- OpenTelemetry - notions de trace, span et attributs.
- LangChain Academy - Agent Observability & Evaluation (partie tracing).

## 📝 Auto-évaluation

Tu peux passer au chapitre 08 quand tu sais répondre, à partir d'une seule trace :

1. Quel modèle a été appelé, combien de fois, et avec quels tokens ?
1. Quel tool call a ajouté le plus de latence ?
1. Pourquoi le coût a-t-il augmenté entre deux runs comparables ?
1. Quelle métrique faut-il surveiller pour éviter la dérive d'une trace ?
1. Quelle donnée de trace deviendra un critère d'eval au chapitre suivant ?
