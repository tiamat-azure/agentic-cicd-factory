# 🛤️ Migrer des tools natifs vers MCP

## 🎯 Idée clé

La bonne migration est progressive : on remplace une capacité à la fois, pas le workflow
entier.

## 🪜 Stratégie

1. Identifier les tools les plus stables et les plus réutilisables.
1. Les encapsuler derrière un serveur MCP dédié.
1. Garder le même contrat métier côté workflow.
1. Vérifier que les traces restent lisibles et que les permissions sont inchangées.
1. Étendre ensuite à d'autres capacités.

## 🧩 Cibles naturelles dans la Factory

- filesystem ;
- Git ;
- CI ;
- GitHub ou backend de PR.

## 🔁 Ce qui ne doit pas changer

- le graphe ;
- les checkpoints ;
- les approbations humaines ;
- les critères de sortie.

## 🌉 Pont vers le chapitre 05

Le chapitre 05 appliquera la même logique de séparation : le modèle pourra changer sans
réécrire le métier. MCP prépare déjà cette discipline de découplage.
