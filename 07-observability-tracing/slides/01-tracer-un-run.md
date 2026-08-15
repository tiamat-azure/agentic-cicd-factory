# 🧭 07.1 - Tracer un run, pas juste écrire des logs

## ❓ Logging ou tracing ?

- Un log dit : « quelque chose s'est produit ».
- Une trace dit : « voici tout le chemin suivi par un run ».

Pour ce chapitre, le bon niveau de détail est celui qui permet de reconstruire un
diagnostic sans relancer le système.

## 🎯 La question à laquelle on veut répondre

> Pourquoi cette exécution a coûté X et pris Y secondes ?

Pour répondre, il faut voir :

1. quel modèle a été appelé ;
1. combien d'itérations ont eu lieu ;
1. quels tools ont été invoqués ;
1. où la latence s'est accumulée ;
1. combien de tokens ont été consommés ;
1. quelle décision a mené au résultat final.

## 🧱 Ce qu'une trace de run doit contenir

| Donnée             | Pourquoi elle est utile                         |
| ------------------ | ------------------------------------------------ |
| `trace_id`         | regrouper toutes les étapes d'un run             |
| `span_id`          | identifier une étape précise                     |
| `parent_span_id`    | reconstruire l'arbre des appels                 |
| modèle / provider  | comprendre le coût et la latence du LLM          |
| prompt / version   | relier une variation de comportement au contexte |
| tokens in / out    | expliquer la facture LLM                         |
| tool / args / stat | expliquer l'effet de bord et les retries         |
| durée / coût / err | détecter les hotspots et les échecs              |

## 🧠 Règle simple

Si tu ne peux pas expliquer un run avec une seule trace, ton instrumentation est trop
faible.

## 🔁 Pont depuis le chapitre 06

Le routeur de modèles décidait déjà quel modèle appeler. Ici, on ajoute la mémoire du
pourquoi : quel choix, combien ça a coûté, et combien de temps il a pris.
