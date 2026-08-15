# 📈 07.4 - Du trace au dashboard

## 🧪 Le workflow de diagnostic

Quand un run semble « trop cher » ou « trop lent », on suit toujours le même chemin :

1. retrouver le `trace_id` du run ;
1. ouvrir la trace complète ;
1. identifier le span le plus coûteux ;
1. comparer avec un run similaire ;
1. relier l'écart à un prompt, un modèle, un tool ou une retry policy.

## 📋 Ce qu'un dashboard minimal doit montrer

- coût par run ;
- latence totale ;
- token breakdown ;
- top spans par durée ;
- taux d'erreur par type d'étape ;
- comparaison avec le budget attendu.

## 🧠 Ce qu'il ne doit pas faire

Un dashboard d'observabilité n'est pas un tableau de KPI abstraits. Il doit permettre de
répondre à une question opérationnelle concrète sur un run précis.

## 🔁 Vers le chapitre 08

Le chapitre 08 prendra ces traces et les transformera en dataset d'évaluation :

- entrée = une tâche ;
- sortie = une trace ;
- verdict = conforme ou régression ;
- métriques = correctness, coût, latence, sécurité.
