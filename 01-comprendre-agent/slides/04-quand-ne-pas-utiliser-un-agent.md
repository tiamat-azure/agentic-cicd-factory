# 01.4 - Quand NE PAS utiliser un agent

## L'arbre de décision

```text
Le problème est-il résoluble sans LLM (regex, parser, script) ?
│
├── OUI ──> ÉCRIS UN SCRIPT. Fin.
└── NON
    │
    Connais-tu à l'avance la suite d'étapes ?
    │
    ├── OUI, toujours la même ─────────> CHAIN (niveau 1)
    ├── OUI, avec des branchements ────> WORKFLOW (niveau 2)
    └── NON, ça dépend de ce qu'on découvre en route
        │
        Peux-tu supporter un coût et une latence variables ?
        │
        ├── NON ──> WORKFLOW + fallback humain
        └── OUI
            │
            As-tu des evals et de l'observabilité ?
            │
            ├── NON ──> AGENT en interne / bac à sable uniquement
            └── OUI ──> AGENT (niveau 3)
```

> Règle : **"ça dépend de ce qu'on découvre en route"** est la seule justification valable
> d'un agent. Tout le reste est du workflow déguisé.

## Les 6 signaux "n'utilise pas d'agent"

1. **Le flux est déterministe.** Si tu peux dessiner le diagramme complet, code le
   diagramme. Un agent qui redécouvre à chaque exécution un chemin que tu connais est une
   taxe payée en tokens et en latence.
1. **La latence est contrainte.** Un agent = N appels LLM séquentiels. Sous 2 secondes de
   budget, oublie.
1. **Le coût doit être prévisible.** Facturation à l'acte, volume élevé -> workflow.
1. **L'erreur est irréversible.** Suppression de données, paiement, `git push --force` sur
   `main`. Soit un workflow, soit un agent avec human-in-the-loop obligatoire (ch. 09).
1. **Tu ne peux pas évaluer le résultat.** Sans critère de succès, tu ne sauras jamais si
   ton agent se dégrade. C'est le principe **eval-first** de cette formation.
1. **Le domaine ne tolère aucune variance.** Conformité, comptabilité, sécurité : le
   non-déterminisme est un défaut, pas une feature.

## Les 4 signaux "un agent est justifié"

1. **L'espace d'états est ouvert** : explorer un repo inconnu, chercher pourquoi un test
   échoue.
1. **Le nombre d'étapes dépend des observations** : corriger jusqu'à ce que la CI passe.
1. **Le coût de l'échec est faible et rattrapable** : une PR, ça se ferme ; un commit sur
   une branche, ça s'annule.
1. **La vérification est plus facile que la génération** : tu ne sais pas écrire le patch,
   mais tu sais lancer les tests. C'est le terrain idéal de l'agentique - et exactement
   pourquoi le CI/CD est un si bon fil rouge.

## Application à notre Factory

| Sous-système                      | Niveau retenu | Pourquoi                                       |
| --------------------------------- | ------------- | ---------------------------------------------- |
| Formater un message de commit     | 1 - chain     | déterministe, une seule étape                  |
| Router une demande (bug/feat/doc) | 2 - workflow  | branchements connus à l'avance                 |
| Explorer le repo et coder         | 3 - agent     | dépend de ce qu'on trouve dans le code         |
| Boucle corriger-jusqu'à-CI-verte  | 3 - agent     | nombre d'itérations inconnu, vérif automatique |
| Décider de merger sur `main`      | 0 - humain    | irréversible, politique métier (ch. 09)        |

> Une usine agentic réussie contient **moins d'agents** qu'on ne le croit. La compétence
> recherchée, c'est le placement du curseur, pas la maximisation de l'autonomie.

## Le coût caché de l'agentique

Passer un composant en agentique t'oblige à financer, en plus :

```text
Agent  =  boucle
        + observabilité (ch. 07)
        + evals + jeu de non-régression (ch. 08)
        + policies + sandboxing (ch. 09)
        + gestion de coût (ch. 06)
```

Si tu ne peux pas financer les quatre derniers, tu ne peux pas financer le premier. C'est
le message central de cette formation, et la raison de l'ordre des chapitres.

## À retenir

1. "Ça dépend de ce qu'on découvre en route" = seule justification d'un agent.
1. Vérification facile + génération difficile = terrain idéal.
1. Un agent sans evals ni observabilité n'est pas déployable.

-> Passe aux [exercices](../exercices/).
