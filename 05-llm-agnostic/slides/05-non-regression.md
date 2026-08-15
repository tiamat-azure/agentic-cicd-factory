# 🧪 05 - Non-régression lors d'un swap de modèle

## 🎯 Intention

Changer de modèle n'est pas une preuve. Il faut rejouer les mêmes scénarios et vérifier que
les invariants importants restent vrais.

## 🧭 Scénario de référence

Un bon scénario de non-régression est petit, stable et représentatif :

1. une demande utilisateur claire ;
1. un état initial connu ;
1. des tools MCP autorisés ;
1. une sortie attendue sous forme d'invariants ;
1. un verdict indépendant du style de rédaction du modèle.

## ✅ Invariants recommandés

Pour la Factory, vérifier au minimum :

- l'analyse produit des tâches vérifiables ;
- le plan suit les étapes du workflow ;
- aucun tool hors périmètre n'est demandé ;
- les sorties structurées sont parseables ;
- les checks existants restent la source de vérité ;
- les erreurs sont explicites quand une capacité manque.

## 🔁 Matrice de swap

| Scénario | Modèle A | Modèle B | Invariants OK ? | Notes |
| -------- | -------- | -------- | --------------- | ----- |
| Analyse simple | cloud | local | oui/non | Écart observé |
| Plan avec tools MCP | cloud | local | oui/non | Écart observé |
| Sortie JSON | cloud | local | oui/non | Écart observé |

Cette matrice n'est pas encore une évaluation complète. Elle prépare les métriques du
chapitre 06 puis les evals structurées des chapitres 07 et 08.

## 🚦 Décision

- Si les invariants passent : le provider peut être ajouté au gateway.
- Si une capacité manque : le gateway doit refuser explicitement le scénario ou choisir une
  autre configuration.
- Si le style varie mais les invariants passent : ce n'est pas une régression métier.
