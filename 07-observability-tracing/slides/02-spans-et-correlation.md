# 🔗 07.2 - Spans et corrélation

## 📎 Les identifiants à ne jamais perdre

- `trace_id` : le run complet.
- `span_id` : une étape mesurable.
- `parent_span_id` : la relation entre étapes.
- `step_id` ou `turn` : l'ordre logique dans l'agent.
- `tool_call_id` : la corrélation entre action et observation.

## 🌳 Le schéma mental

```text
run
└── model call
    ├── tool call
    └── model call
        └── tool call
```

Chaque span doit répondre à une seule question :

- quelle action a démarré ;
- quelle entrée elle a reçue ;
- combien de temps elle a pris ;
- quel résultat ou erreur elle a produit.

## ⚠️ Anti-patterns fréquents

- des logs sans `run_id` ;
- un span qui mélange modèle, tool et I/O ;
- une observation sans lien avec le tool call précédent ;
- des métriques agrégées sans possibilité de descendre au cas individuel.

## ✅ Bonne habitude

Instrumenter chaque transition importante :

1. début du span ;
1. fin du span ;
1. attributs stables ;
1. événements utiles ;
1. statut final.

## 🧭 Ce qu'on doit pouvoir reconstruire

À partir d'une trace, on doit retrouver :

- quel passage a été décidé par le modèle ;
- quel passage a été imposé par le runtime ;
- quel tool a été relancé ;
- pourquoi le même run a bifurqué ou a ralenti.
