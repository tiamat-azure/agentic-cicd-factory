# ✏️ Exercices - chapitre 07

Deux exercices pour passer du concept de trace à un diagnostic exploitable.

| #   | Exercice                                      | Compétence visée                                | Durée  |
| --- | --------------------------------------------- | ------------------------------------------------ | ------ |
| 1   | Lire une trace et expliquer un run            | relier coût, latence, tokens et décision         | 25 min |
| 2   | Définir un schéma de trace minimal            | instrumenter sans perdre la corrélation          | 25 min |

______________________________________________________________________

## 🪜 Exercice 1 - Pourquoi ce run a-t-il coûté X ?

Lis la trace fictive ci-dessous :

| Étape | Type       | Modèle / tool | Tokens in | Tokens out | Durée | Coût |
| ----- | ---------- | ------------- | --------- | ---------- | ----- | ---- |
| 1     | model call | model A       | 1 200     | 180        | 2.4 s | 0.18 |
| 2     | tool call  | `search_repo` | -         | -          | 0.7 s | -    |
| 3     | model call | model A       | 1 460     | 210        | 3.1 s | 0.22 |
| 4     | tool call  | `write_file`  | -         | -          | 0.4 s | -    |
| 5     | model call | model B       | 1 890     | 260        | 4.8 s | 0.41 |

Réponds en 5 points :

1. Quel span a ajouté le plus de latence ?
1. Pourquoi les tokens d'entrée ont-ils augmenté au fil du run ?
1. Quelle partie du coût vient du choix de modèle ?
1. Quelle étape aurait pu être bornée par un budget ?
1. Que ferais-tu pour réduire le coût sans perdre la qualité ?

______________________________________________________________________

## 🪜 Exercice 2 - Schéma de trace minimal

Pour la factory du fil rouge, définis le schéma minimal d'une trace au format tableau.

Contraintes :

1. il faut pouvoir reconstruire l'arbre des appels ;
1. il faut pouvoir attribuer le coût à une étape ;
1. il faut pouvoir relier un tool call à sa réponse ;
1. il faut pouvoir comparer deux runs similaires ;
1. il faut rester lisible par un humain.

Tu peux structurer ta réponse avec les colonnes :

- identifiant ;
- parent ;
- type ;
- attributs ;
- métriques ;
- statut ;
- commentaire de diagnostic.
