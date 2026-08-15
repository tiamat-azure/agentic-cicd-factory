# 🔑 Solutions - chapitre 07

Ces réponses servent de guide de correction.

## ✅ Exercice 1 - Lecture de trace

Attendus principaux :

- le plus gros incrément de latence vient du modèle B ;
- la hausse des tokens d'entrée vient de l'historique qui s'allonge ;
- le changement de modèle explique la hausse de coût ;
- le budget aurait dû porter au minimum sur les itérations ou le coût ;
- la première optimisation possible est de réduire le contexte envoyé au modèle.

## ✅ Exercice 2 - Schéma minimal

Le schéma doit au moins permettre :

- `trace_id` pour grouper un run ;
- `span_id` et `parent_span_id` pour reconstruire l'arbre ;
- `type` pour distinguer modèle, tool, observation, erreur ;
- attributs pour le modèle, le prompt et les arguments ;
- métriques pour durée, tokens et coût ;
- statut pour savoir si l'étape a réussi ;
- commentaire pour relier la donnée brute à un diagnostic.

## 🧭 Point clé

La bonne trace n'est pas la plus bavarde : c'est celle qui rend un run explicable et
comparables aux autres.
