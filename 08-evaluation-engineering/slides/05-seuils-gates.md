# 🚦 Seuils, gates et décision de blocage

## 🎯 Objectif

Transformer les scores d'eval en décision opérationnelle : `pass`, `block` ou
`needs_human_review`.

## 🧮 Score global

Un score global aide à suivre la tendance, mais il ne suffit jamais.

```text
global_score = 0.50 * correctness
             + 0.20 * completeness
             + 0.15 * cost_efficiency
             + 0.10 * latency
             + 0.05 * trace_quality
```

Les poids doivent être versionnés avec le dataset. Changer les poids sans l'annoncer
revient à changer la définition de la qualité.

## 🛑 Blockers

Un blocker arrête la promotion même si le score global est bon :

- test rouge ;
- fichier interdit modifié ;
- régression sur un cas protégé ;
- budget critique dépassé ;
- trace incomplète pour une décision auditée ;
- judge sans evidence suffisante ;
- signal de risque qui relève du chapitre 09.

## 🧭 Décision

| Condition | Décision |
| --------- | -------- |
| Aucun blocker et score au-dessus du seuil | `pass` |
| Blocker déterministe | `block` |
| Score limite ou judge incertain | `needs_human_review` |
| Budget dépassé mais fallback prévu | `needs_human_review` ou `block` selon policy |

## 🌉 Passage vers la gouvernance

Le chapitre 09 ne réinventera pas les seuils. Il leur donnera un cadre : qui peut les
modifier, quels seuils sont obligatoires, quand escalader, comment auditer une exception.
