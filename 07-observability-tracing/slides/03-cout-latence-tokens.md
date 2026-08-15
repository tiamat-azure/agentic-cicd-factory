# 💸 07.3 - Coût, latence, tokens

## 📊 Trois mesures, trois questions

- **Tokens** : combien de texte a été consommé ?
- **Latence** : où le temps s'est-il perdu ?
- **Coût** : quelle partie de la facture vient du modèle, et quelle partie du runtime ?

## 🧮 Ce qu'il faut attribuer

Pour chaque run, sépare au minimum :

1. les tokens d'entrée ;
1. les tokens de sortie ;
1. les tokens mis en cache, si le fournisseur les expose ;
1. la durée des appels modèle ;
1. la durée des tools ;
1. le nombre de retries ;
1. le coût total estimé.

## 🔍 Pourquoi un run coûte plus cher qu'un autre ?

Les causes les plus fréquentes sont simples :

- le prompt a grossi ;
- l'agent a tourné plus longtemps ;
- un tool a échoué puis a été rejoué ;
- le routeur a choisi un modèle plus cher ;
- une boucle a ajouté des itérations inutiles.

## 🧭 Le bon réflexe

Ne demande pas seulement « combien ça a coûté ? ».
Demande aussi :

- quelle étape a créé ce coût ;
- si ce coût était attendu ;
- si le coût a apporté de la valeur ;
- si un budget aurait dû arrêter le run plus tôt.

## 🔁 Pont vers le chapitre 08

Une fois que les métriques sont corrélées à la trace, elles deviennent filtrables,
comparables et donc évaluables.
