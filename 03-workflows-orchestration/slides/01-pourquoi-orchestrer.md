# 🧭 03.1 - Pourquoi orchestrer ?

## 🧱 Ce que le chapitre 02 nous a donné

À la fin du chapitre 02, le Coding Agent sait utiliser des tools : lire, écrire, lancer des
commandes, inspecter un diff. C'est puissant, mais tout arrive dans une même boucle :
comprendre la demande, décider quoi faire, coder, tester, se corriger, conclure.

Cette boucle est utile pour explorer. Elle devient fragile quand on veut produire une usine
CI/CD reproductible.

## ⚠️ Les limites d'une boucle unique

| Symptôme                 | Ce qui se passe                                              |
| ------------------------ | ------------------------------------------------------------ |
| Responsabilités floues   | le même prompt analyse, planifie, code et review             |
| Reprise difficile        | après un échec test, on ne sait pas où reprendre             |
| Coût variable            | le modèle peut refaire de l'analyse au lieu de tester        |
| Audit incomplet          | impossible de dire quelle décision a été validée par humain  |
| Permissions trop larges  | l'agent qui analyse possède parfois déjà les droits d'écrire |

Le problème n'est pas que l'agent est mauvais. Le problème est qu'on lui demande de porter
un processus qui devrait être explicite.

## 🔀 Workflow vs agent

Un **agent** décide à l'exécution de la prochaine action. Un **workflow** encode le flux à
l'avance : étapes, branches, conditions d'arrêt, reprise.

```text
Agent libre :
request -> LLM -> tool -> LLM -> tool -> ... -> stop

Workflow :
request -> analyze -> plan -> implement -> test -> review -> pr
```

Le workflow peut contenir des appels LLM. Il peut même contenir un agent dans un node. Mais
le chemin général reste gouverné par le graphe.

## 🏭 Pourquoi c'est mieux pour une CI/CD Factory

Une usine CI/CD doit être :

1. **prévisible** : on connaît les étapes et les budgets ;
1. **auditable** : chaque décision importante laisse une trace ;
1. **reprenable** : un test rouge ne force pas à recommencer depuis la demande ;
1. **gouvernable** : certaines actions attendent un humain ;
1. **composable** : demain, un node pourra appeler MCP au lieu d'un tool local.

## 💡 À retenir

1. On orchestre pour borner le non-déterminisme, pas pour supprimer les modèles.
1. Le workflow décrit le processus ; les modèles remplissent des tâches locales.
1. Plus l'action est risquée, plus elle doit être explicite dans le graphe.

-> Slide suivante : [`02-graphe-state-node-edge.md`](02-graphe-state-node-edge.md)
