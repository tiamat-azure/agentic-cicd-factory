# 📚 Leçons - Token Engineering & Model Routing

Ce dossier contient les leçons courtes du chapitre 06. Lis-les dans l'ordre : elles
partent de la mesure brute, puis construisent les budgets, le routing et la métrique de
coût utile.

## 🧭 Ordre conseillé

1. [`01-instrumentation-tokens.md`](01-instrumentation-tokens.md) - mesurer avant
   d'optimiser.
1. [`02-budgets-et-politiques.md`](02-budgets-et-politiques.md) - transformer les limites
   en policy gates.
1. [`03-classification-et-routing.md`](03-classification-et-routing.md) - choisir un
   profil via le Model Gateway.
1. [`04-fallback-retry-cost.md`](04-fallback-retry-cost.md) - retenter, escalader et
   calculer le coût par succès.

## 🎯 Fil directeur

À la fin des leçons, tu dois pouvoir expliquer une décision de routing avec une phrase du
type :

> Cette tâche est `medium`, elle part sur `local-large`, avec un budget de 8 itérations,
> 30k tokens d'entrée et 0,25 USD. Si la sortie structurée est invalide une fois, on retry ;
> si le quality gate échoue deux fois, on fallback vers `cloud-frontier` ou on arrête.
