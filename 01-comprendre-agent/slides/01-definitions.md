# 📐 01.1 - Définitions : le spectre de l'autonomie

## ❓ Le problème avec le mot "agent"

> "Un agent, c'est un LLM qui utilise des outils."

Cette définition est fausse par insuffisance. Un LLM qui utilise un outil **une fois**,
dans un ordre décidé par toi, n'est pas un agent : c'est un appel de fonction.

La bonne question n'est pas _"est-ce qu'il y a des tools ?"_ mais :

> **Qui décide de la prochaine action, et qui décide qu'on s'arrête ?**

Si la réponse est "moi, le développeur, dans mon code" -> ce n'est pas un agent. Si la
réponse est "le modèle, à l'exécution" -> c'est un agent.

## 🪜 Les 5 niveaux

| Niveau | Nom             | Qui décide du flux                 | Nb d'appels LLM | Terminaison      |
| ------ | --------------- | ---------------------------------- | --------------- | ---------------- |
| 0      | LLM application | personne (1 aller-retour)          | 1               | immédiate        |
| 1      | Chain           | le développeur (fixe)              | N fixe          | fin de la chaîne |
| 2      | Workflow        | le développeur (avec branchements) | N borné         | fin du graphe    |
| 3      | **Agent**       | **le modèle**                      | **N inconnu**   | **le modèle**    |
| 4      | Multi-agent     | un orchestrateur + les modèles     | N inconnu       | négociée         |

### 🔹 Niveau 0 - LLM application

```text
prompt ──> LLM ──> réponse
```

Exemple : "résume ce texte". Aucun état, aucune décision.

### 🔗 Niveau 1 - Chain

```text
prompt ──> LLM ──> transform ──> LLM ──> réponse
```

Le chemin est **écrit à l'avance**. Reproductible, testable, pas cher. Exemple : extraire
les specs d'un ticket, puis générer un plan de test.

### 🔀 Niveau 2 - Workflow

```text
              ┌── branche A ──┐
prompt ─> routeur              ├─> résultat
              └── branche B ──┘
```

Il y a des `if`, des boucles bornées, du parallélisme - mais **le graphe est écrit par
toi**. Le LLM remplit des cases, il ne dessine pas le plan.

> C'est le niveau le plus sous-estimé. La majorité des "agents" en production sont des
> workflows, et c'est très bien : ils sont prévisibles et évaluables.

### 🤖 Niveau 3 - Agent

```text
        ┌──────────────────────────────┐
        │                              │
prompt ─┴─> LLM ──> action ──> observation ──> (LLM décide) ──> STOP
```

Le modèle choisit **à chaque tour** quoi faire, et déclare lui-même la fin. Le nombre
d'itérations n'est pas connu à l'écriture du code. C'est ça, et uniquement ça, qui fait
l'agent.

### 👥 Niveau 4 - Multi-agent

Plusieurs agents, chacun avec son propre prompt, ses propres tools, son propre budget, qui
se passent du travail (handoff) ou sont coordonnés par un superviseur. -> Chapitre 03.

## 🔍 Ce qui change vraiment entre niveau 2 et niveau 3

| Dimension    | Workflow             | Agent                                             |
| ------------ | -------------------- | ------------------------------------------------- |
| Coût         | prévisible           | variable, potentiellement non borné               |
| Latence      | prévisible           | variable                                          |
| Debug        | on relit le graphe   | on relit une **trace** (-> ch. 07)                |
| Tests        | unitaires classiques | evals statistiques (-> ch. 08)                    |
| Mode d'échec | exception            | **boucle infinie, dérive, hallucination d'outil** |
| Sécurité     | surface connue       | surface ouverte (-> ch. 09)                       |

> Retiens : **passer en agentique, c'est échanger de la prévisibilité contre de
> l'adaptabilité.** Tout le reste de cette formation (observabilité, evals, policies)
> existe pour racheter la prévisibilité que tu viens de perdre.

## 🧵 Notre fil rouge

La Agentic CI/CD Factory contiendra **les 5 niveaux à la fois** :

- niveau 1 pour formater un message de commit,
- niveau 2 pour router une demande vers le bon sous-système,
- niveau 3 pour l'agent de codage qui explore un repo,
- niveau 4 pour la chaîne plan -> code -> test -> review.

L'art n'est pas de tout rendre agentique. C'est de **choisir le niveau minimum qui résout
le problème**.

## 💡 À retenir

1. Un agent se définit par **qui décide**, pas par la présence de tools.
1. Le nombre d'itérations inconnu à l'écriture = signature de l'agent.
1. Le niveau le plus bas qui marche est toujours le bon choix.

-> Demo suivante : [`demos/01_llm_brut.py`](../demos/01_llm_brut.py)
