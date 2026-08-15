# 📚 Leçons - Agentic CI/CD

Ce dossier contient les leçons courtes du chapitre 10. Lis-les dans l'ordre : elles
partent du risque de livraison agentique, puis construisent les déclencheurs d'evals, la
pipeline cible, les règles de blocage et le pont vers les PR automatiques.

## 🧭 Ordre conseillé

1. [`01-du-prototype-au-produit.md`](01-du-prototype-au-produit.md) - comprendre pourquoi
   une Factory agentique ne se livre pas comme une API classique.
1. [`02-declencheurs-evals.md`](02-declencheurs-evals.md) - associer chaque type de
   changement à une suite d'evals.
1. [`03-pipeline-cible.md`](03-pipeline-cible.md) - composer checks classiques et gates
   agentiques.
1. [`04-regles-de-blocage.md`](04-regles-de-blocage.md) - rendre les blocages explicables
   et auditables.
1. [`05-pont-vers-pr-factory.md`](05-pont-vers-pr-factory.md) - préparer les PR générées
   au chapitre 11.

## 🎯 Fil directeur

À la fin des leçons, tu dois pouvoir dire :

> Ce commit touche un prompt et une policy. Il lance donc les evals de non-régression, de
> safety et d'allow/deny. La pipeline bloque si le score critique baisse, si le coût par
> succès dépasse le budget ou si l'exception humaine n'est pas tracée.
