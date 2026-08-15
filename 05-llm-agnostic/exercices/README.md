# 🏋️ Exercices - Construire le Model Gateway v0.5

## 🎯 Objectif

Transformer la Factory en système LLM-agnostic : le workflow reste stable, les providers
sont interchangeables, et le swap de modèle se valide par non-régression.

## 🧩 Exercice 1 - Dessiner le contrat provider

Décris le contrat `LLMProvider` de ta Factory avec :

- les entrées de `generate` ;
- la forme de `LLMResponse` ;
- les champs de `ModelCapabilities` ;
- les erreurs normalisées.

Critère de réussite : un node métier peut utiliser ce contrat sans connaître le provider.

## 🚪 Exercice 2 - Placer le Model Gateway

À partir de l'architecture du chapitre 04, indique :

- quels fichiers ou modules devraient dépendre du gateway ;
- quels fichiers ou modules ne doivent jamais importer un SDK de provider ;
- où lire la configuration du modèle actif ;
- où convertir les erreurs provider en erreurs normalisées.

Critère de réussite : ajouter un provider ne modifie pas les nodes `ANALYZE`, `PLAN`,
`IMPLEMENT`, `TEST` ou `REVIEW`.

## 🔁 Exercice 3 - Préparer une matrice de non-régression

Construis une matrice avec au moins trois scénarios :

1. analyse d'une demande simple ;
1. planification avec tools MCP ;
1. sortie structurée attendue.

Pour chaque scénario, note les invariants à vérifier avec un modèle cloud et un modèle
local.

Critère de réussite : le verdict ne dépend pas de la beauté de la prose, mais d'invariants
métier observables.

## ✅ Livrable attendu

À la fin des exercices, tu dois pouvoir expliquer et montrer :

- où se trouve la frontière `LLMProvider` ;
- comment le gateway sélectionne un provider par configuration ;
- pourquoi le workflow reste inchangé ;
- quels invariants prouvent qu'un swap de modèle est acceptable.
