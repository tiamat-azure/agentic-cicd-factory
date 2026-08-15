# ⚖️ LLM-as-judge

## 🎯 Objectif

Utiliser un modèle comme juge seulement pour ce que le code ne sait pas mesurer : clarté,
pertinence, exhaustivité, compromis ou qualité d'un raisonnement.

## 🧾 Rubric obligatoire

Un judge doit recevoir une grille explicite :

| Critère | Score | Evidence attendue |
| ------- | ----- | ----------------- |
| Correctness | 0 à 5 | La réponse satisfait-elle l'expected ? |
| Completeness | 0 à 5 | Les contraintes importantes sont-elles couvertes ? |
| Grounding | 0 à 5 | Le jugement cite-t-il la sortie et la trace ? |
| Safety | pass/block | Y a-t-il un comportement interdit ? |

Le judge doit produire un score **et** une justification liée aux preuves fournies.

## 🔭 Evidence issue des traces

Le judge ne doit pas deviner le run. Il reçoit :

- la demande initiale ;
- l'expected et les constraints ;
- la sortie produite ;
- les extraits utiles de trace ;
- les résultats des checks déterministes ;
- les budgets observés.

## 🧯 Réduire les biais

- Garder la même rubric entre versions.
- Masquer le nom du modèle ou de la version si possible.
- Séparer quality score et blockers.
- Échantillonner des revues humaines sur les cas limites.
- Ne jamais utiliser le même run comme réponse et comme preuve unique de qualité.

## 🚫 Ce que le judge ne doit pas faire

- Valider un format que du code peut parser.
- Ignorer une régression déterministe.
- Compenser un blocker par une bonne note globale.
- Décider seul d'un risque de sécurité critique.
