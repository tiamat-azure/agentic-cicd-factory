# ✅ Evals déterministes et code-based

## 🎯 Objectif

Vérifier automatiquement tout ce qui n'a pas besoin d'un LLM. C'est moins coûteux, plus
rapide et plus fiable qu'un jugement sémantique.

## 🧮 Evals déterministes

À utiliser quand le résultat attendu est observable sans ambiguïté :

- fichier créé, modifié ou non modifié ;
- sortie JSON conforme à un schéma ;
- valeur exacte ou expression régulière ;
- absence d'un chemin interdit ;
- budget respecté : coût, tokens, latence, tool calls, itérations.

## 🧑‍💻 Evals code-based

Une eval code-based exécute une vérification existante ou un calcul simple :

- tests unitaires ou d'intégration déjà présents ;
- parseur de markdown, YAML ou JSON ;
- comparaison structurée d'un plan ;
- calcul `cost_per_success` ;
- lecture de trace pour vérifier un span obligatoire.

## 🛑 Ordre d'exécution

Toujours exécuter les checks déterministes avant les judges LLM :

1. ils bloquent vite les erreurs évidentes ;
1. ils évitent de payer un judge pour une sortie invalide ;
1. ils réduisent les faux positifs ;
1. ils produisent des blockers auditables.

## ⚠️ Piège courant

Ne pas transformer un check déterministe en prompt de judge.

Mauvais réflexe : demander à un LLM si le JSON est valide.

Bon réflexe : parser le JSON, puis réserver le judge à la qualité du contenu si le format
est valide.
