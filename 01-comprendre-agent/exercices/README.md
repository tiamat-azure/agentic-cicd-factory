# Exercices - chapitre 01

Trois exercices progressifs. Le 3 est le livrable **Agent v0.1**. Travaille dans
`exercices/`, compare avec `solutions/` **après** avoir tenté.

| #   | Exercice                       | Compétence visée                      | Durée  |
| --- | ------------------------------ | ------------------------------------- | ------ |
| 1   | Classer 8 cas                  | choisir le bon niveau d'autonomie     | 15 min |
| 2   | Ajouter un tool                | décrire un tool, boucler correctement | 25 min |
| 3   | Terminaison explicite + budget | rendre un agent gouvernable           | 40 min |

______________________________________________________________________

## Exercice 1 - Quel niveau d'autonomie ? (papier)

Pour chacun des 8 cas, choisis un niveau (0 script / 1 chain / 2 workflow / 3 agent / 4
multi-agent) et **justifie en une phrase**. Écris tes réponses dans
`exercices/01-classification.md`.

1. Générer un message de commit conventionnel à partir d'un `git diff`.
1. Traduire tous les fichiers de doc du dépôt en anglais.
1. Diagnostiquer pourquoi un job CI est passé de vert à rouge entre deux commits.
1. Vérifier qu'une PR respecte la convention de nommage des branches.
1. À partir d'un ticket, produire un plan d'implémentation, coder, tester, ouvrir la PR.
1. Extraire les critères d'acceptation d'un ticket en JSON structuré.
1. Décider si une PR peut être mergée automatiquement sur `main`.
1. Migrer 200 fichiers d'une API dépréciée vers la nouvelle, chaque cas étant différent.

> Piège : au moins deux de ces cas **ne nécessitent aucun LLM**.

______________________________________________________________________

## Exercice 2 - Ajouter un tool `chercher_dans_fichiers`

Dans une copie de `demos/03_agent_minimal/`, ajoute un tool qui cherche une chaîne dans
les fichiers du bac à sable et renvoie les lignes correspondantes avec leur numéro.

Contraintes :

1. Signature : `chercher_dans_fichiers(motif: str, extension: str = ".py") -> str`.
1. Ne jamais sortir du bac à sable (réutilise `_resoudre`).
1. Tronquer à 50 résultats maximum - explique en commentaire pourquoi c'est nécessaire.
1. Rédiger la description du tool de sorte que le modèle l'utilise **avant** de lire des
   fichiers entiers.

Validation :

```sh
python main.py "Où la constante TAUX_TVA est-elle utilisée ?"
```

Réussi si le modèle appelle `chercher_dans_fichiers` sans que tu le lui demandes
explicitement.

**Puis dégrade volontairement la description** en `"Cherche du texte."` et relance. Note
ce qui change : c'est ta première leçon de tool design (approfondie au ch. 02).

______________________________________________________________________

## Exercice 3 - Livrable Agent v0.1 : terminaison explicite et budget

Objectif : rendre l'agent **gouvernable**, prérequis de tout le reste de la formation.

### 3.a - Tool `terminer`

Ajoute un tool :

```python
{
  "name": "terminer",
  "description": "Déclare la fin de la tâche. À appeler dès que l'objectif est atteint "
                 "ou que tu es certain de ne pas pouvoir l'atteindre.",
  "parameters": {
    "type": "object",
    "properties": {
      "statut": {"type": "string", "enum": ["succes", "echec"]},
      "resume": {"type": "string", "description": "Conclusion en 3 lignes maximum."},
      "confiance": {"type": "number", "description": "Entre 0 et 1."}
    },
    "required": ["statut", "resume", "confiance"]
  }
}
```

Il n'exécute rien : la boucle l'intercepte et remplit `state.statut`, `state.resultat`.
Ajoute la mention correspondante dans le `SYSTEM_PROMPT`.

### 3.b - Budget en tokens

Ajoute `max_tokens_total` au state et une condition d'arrêt `budget_tokens_epuise()`.
L'agent doit sortir proprement avec `statut="budget_epuise"`.

### 3.c - Anti ping-pong

Si la **même** action (nom + arguments) est demandée 2 fois d'affilée, ne la ré-exécute
pas : renvoie comme observation un message explicite du type
`"Tu viens d'exécuter cette action à l'identique. Voici le résultat précédent : ... "`.

### 3.d - Journal exploitable

À la fin du run, écris `run.json` :

```json
{
  "objectif": "...",
  "statut": "succes",
  "iterations": 4,
  "tokens": { "in": 1234, "out": 567 },
  "actions": [{ "tour": 1, "tool": "lister_fichiers", "args": {} }],
  "resultat": "..."
}
```

> Ce fichier est ton premier artefact d'observabilité. Au chapitre 07, il deviendra une
> trace OpenTelemetry ; au chapitre 08, l'entrée d'un jeu d'evals. Soigne-le.

### Critères de validation du livrable

- [ ] L'agent termine via le tool `terminer` avec un statut machine-lisible.
- [ ] Il s'arrête proprement sur budget itérations **et** sur budget tokens.
- [ ] Le ping-pong est détecté et neutralisé.
- [ ] `run.json` est produit à chaque exécution.
- [ ] `LLM_PROVIDER=anthropic` et `LLM_PROVIDER=ollama` fonctionnent sans modifier
  `agent.py`, `tools.py` ni `state.py`.
- [ ] Aucune dépendance à un framework agentique.

______________________________________________________________________

## Bonus (facultatif)

- Fais tourner l'agent 5 fois de suite sur le même objectif. Le résultat est-il stable ?
  Note les écarts : tu viens de découvrir pourquoi les evals sont statistiques (ch. 08).
- Ajoute un tool `supprimer_fichier` **sans l'exposer au modèle**, puis demande-toi ce
  qu'il faudrait exiger avant de l'exposer un jour. Réponse au chapitre 09.
