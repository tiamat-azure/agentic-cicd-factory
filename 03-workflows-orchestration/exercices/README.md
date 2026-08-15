# ✏️ Exercices - chapitre 03

Trois exercices progressifs. Le 3 est le livrable **Factory v0.3**. Travaille dans
`exercices/`, compare avec `solutions/` **après** avoir tenté.

| #   | Exercice                         | Compétence visée                       | Durée  |
| --- | -------------------------------- | -------------------------------------- | ------ |
| 1   | Cartographier le state           | séparer conversation et données métier | 25 min |
| 2   | Dessiner les edges conditionnels | rendre les décisions auditables        | 30 min |
| 3   | Spécifier Factory v0.3           | produire un workflow publication-ready | 60 min |

______________________________________________________________________

## 🧱 Exercice 1 - Cartographier le state

À partir de la demande suivante :

> "Ajoute une validation qui empêche la Factory d'ouvrir une PR si les tests n'ont pas été
> exécutés."

Crée `exercices/01-state.md` avec trois sections :

1. `request` : ce qui doit rester immuable.
1. `analysis` : contraintes, risques, fichiers ou composants probables.
1. `plan` : étapes et critères d'acceptation.

Contraintes :

- Ne mets pas toute la conversation dans un seul champ `messages`.
- Chaque champ doit pouvoir être relu par un node sans contexte caché.
- Ajoute un champ `status` machine-lisible.

______________________________________________________________________

## 🔀 Exercice 2 - Edges conditionnels

Crée `exercices/02-edges.md` et décris les transitions de `TEST` vers la suite.

Tu dois couvrir au moins ces cas :

1. tests verts ;
1. tests rouges mais erreur probablement corrigeable ;
1. tests rouges qui contredisent le plan validé ;
1. commande de test indisponible ;
1. budget de correction épuisé.

Pour chaque transition, indique :

- condition lue dans le state ;
- prochain node ;
- statut écrit ;
- information nécessaire pour reprendre.

______________________________________________________________________

## 📦 Exercice 3 - Livrable Factory v0.3

Crée `exercices/03-factory-v03.md`. Le document doit spécifier ton workflow complet :

```text
REQUEST -> ANALYZE -> PLAN -> APPROVE_PLAN -> IMPLEMENT -> TEST -> REVIEW -> APPROVE_PR -> PR
```

### 🧾 3.a - Contrat du state

Liste les champs du state et leur rôle. Minimum attendu :

- `request`
- `analysis`
- `plan`
- `human_decisions`
- `changes`
- `test_report`
- `review`
- `pr_draft`
- `status`

### 🧩 3.b - Contrat des nodes

Pour chaque node, indique :

1. champs lus ;
1. champs écrits ;
1. tools autorisés ;
1. statuts d'échec possibles.

### 💾 3.c - Checkpoints

Décris au minimum deux checkpoints :

1. après `PLAN` ;
1. après `TEST`.

Pour chacun, explique ce qui permet de reprendre sans rejouer les nodes précédents.

### 🛂 3.d - Approbations humaines

Décris les deux décisions humaines :

1. validation du plan avant écriture ;
1. validation avant PR.

Chaque décision doit avoir des valeurs structurées, par exemple
`approved | rejected | needs_changes`, et un commentaire obligatoire hors `approved`.

### ✅ Critères de validation du livrable

- [ ] Le workflow est borné : aucune boucle non limitée.
- [ ] Les nodes d'analyse et de planification n'ont pas de permission d'écriture.
- [ ] `IMPLEMENT` ne peut pas démarrer sans plan approuvé.
- [ ] `PR` ne peut pas démarrer sans tests et review acceptés.
- [ ] Les checkpoints suffisent à expliquer la reprise après échec.
- [ ] Le document indique clairement ce qui changera au chapitre 04 avec MCP.

______________________________________________________________________

## 🎁 Bonus (facultatif)

Ajoute une branche `documentation_only` : si `ANALYZE` détecte une demande purement
éditoriale, quels tests sont encore utiles ? Quelles validations humaines gardes-tu ?
