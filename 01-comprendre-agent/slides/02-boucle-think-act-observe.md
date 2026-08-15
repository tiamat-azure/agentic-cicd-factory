# 01.2 - La boucle Think -> Act -> Observe

## L'intuition

Un LLM est une fonction pure : `texte -> texte`. Il ne peut rien faire du monde. Un agent,
c'est cette fonction **placée dans une boucle qui a accès au monde**.

```text
   ┌─────────────────────────────────────────────┐
   │                                             │
   ▼                                             │
┌──────┐   pense    ┌────────┐   agit   ┌──────────────┐
│ LLM  │ ─────────> │ Action │ ───────> │ Environnement│
└──────┘            └────────┘          └──────┬───────┘
   ▲                                           │
   │              observe (résultat)           │
   └───────────────────────────────────────────┘
```

## Les 3 temps

### 1. Think

Le modèle reçoit : `system prompt + historique + observations` et produit soit :

- une **action** (appel de tool, avec des arguments), soit
- une **réponse finale** (fin de boucle).

C'est le seul endroit où il y a du raisonnement. Tout le reste est de la plomberie
déterministe - et c'est une bonne nouvelle : la plomberie, ça se teste.

### 2. Act

Ton code - pas le modèle - exécute l'action. Le modèle **demande**, le runtime
**exécute**.

> Point critique de sécurité : le modèle n'exécute jamais rien. Il émet une intention
> structurée. C'est ta boucle qui décide de l'honorer, de la refuser ou de demander une
> validation humaine (-> ch. 09).

### 3. Observe

Le résultat de l'exécution est **réinjecté dans l'historique**, dans un message
identifiable comme "résultat d'outil".

> Erreur n°1 des débutants : exécuter le tool et ne pas remettre le résultat dans
> l'historique. Le modèle re-demande alors le même tool en boucle. Si ton agent répète la
> même action, vérifie ça en premier.

## Pseudo-code de référence

```python
def run(objectif: str) -> str:
    historique = [system_prompt, user(objectif)]

    while True:                       # <- le "N inconnu"
        decision = llm(historique)    # THINK
        historique.append(decision)

        if decision.est_finale:
            return decision.texte     # TERMINAISON décidée par le modèle

        for appel in decision.appels_tools:
            resultat = TOOLS[appel.nom](**appel.args)   # ACT
            historique.append(tool_result(appel.id, resultat))  # OBSERVE
```

Tout le chapitre 01 tient dans ces 12 lignes. Le reste de la formation consiste à rendre
ces 12 lignes **observables, évaluables, gouvernées et scalables**.

## ReAct : pourquoi "Reasoning + Acting"

Le pattern porte le nom de l'article _ReAct_ (2022). Son idée : entrelacer le raisonnement
en langage naturel et les actions, plutôt que de planifier d'abord puis exécuter ensuite.

Avantage : après chaque observation, le modèle peut **corriger sa trajectoire**. C'est
exactement ce qu'il faut pour du CI/CD, où un test qui échoue change le plan.

Deux variantes de mise en œuvre :

| Variante               | Comment                                                        | Quand                                 |
| ---------------------- | -------------------------------------------------------------- | ------------------------------------- |
| ReAct textuel          | le modèle écrit `Thought: ... Action: ...` en texte, tu parses | modèles sans tool calling natif       |
| **Tool calling natif** | l'API renvoie des appels structurés (JSON)                     | par défaut aujourd'hui - plus robuste |

Nous utilisons le **tool calling natif** dès la demo 3, et nous gardons le mode textuel en
tête car il reste nécessaire pour certains modèles locaux (-> ch. 05).

## Le format d'un tool

Un tool, c'est 3 choses, et seulement 3 :

1. **un nom** stable ;
1. **une description** en langage naturel - c'est le vrai "prompt" du tool, le modèle ne
   voit que ça pour décider ;
1. **un schéma d'arguments** (JSON Schema) - le contrat.

```json
{
  "name": "lire_fichier",
  "description": "Lit le contenu texte d'un fichier du dépôt. Utilise-le avant toute modification.",
  "input_schema": {
    "type": "object",
    "properties": { "chemin": { "type": "string", "description": "Chemin relatif au dépôt" } },
    "required": ["chemin"]
  }
}
```

> Une mauvaise description de tool coûte plus cher qu'un mauvais modèle. On y revient au
> chapitre 02.

## À retenir

1. Think = le modèle décide ; Act = ton code exécute ; Observe = le résultat retourne dans
   l'historique.
1. Le modèle n'exécute jamais rien lui-même : c'est le point d'ancrage de toute la
   sécurité.
1. Oublier de réinjecter l'observation = boucle infinie.

-> Demo suivante : [`demos/02_boucle_manuelle.py`](../demos/02_boucle_manuelle.py)
