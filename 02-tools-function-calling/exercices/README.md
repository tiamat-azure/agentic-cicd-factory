# ✏️ Exercices - chapitre 02

Trois exercices progressifs. Le 3 est le livrable **Agent v0.2**. Travaille d'abord seul,
compare ensuite avec `solutions/`.

| # | Exercice | Compétence visée | Durée |
| - | -------- | ---------------- | ----- |
| 1 | Choisir les bons tools | concevoir l'environnement | 20 min |
| 2 | Écrire des contrats robustes | schéma, validation, erreurs | 30 min |
| 3 | Assembler un Coding Agent v0.2 | permissions, tests, résumé | 45 min |

______________________________________________________________________

## 🪜 Exercice 1 - Quels tools donnerais-tu à l'agent ?

Pour chacun des 10 cas ci-dessous, choisis les tools minimaux à exposer, puis note au
moins **une permission à refuser**.

1. Lister les fichiers d'un dépôt inconnu.
1. Lire un README et en extraire les sections.
1. Modifier une fonction Python sans casser le reste du code.
1. Lancer la suite de tests.
1. Vérifier le diff avant de proposer un patch.
1. Interroger une page HTTP publique de documentation.
1. Ouvrir une issue GitHub en écriture.
1. Supprimer un fichier temporaire.
1. Renommer un dossier entier.
1. Publier une release.

> Piège : tous ces cas ne doivent pas forcément devenir des tools exposés au modèle.

______________________________________________________________________

## 🧾 Exercice 2 - Écrire de meilleurs contrats

Choisis 3 tools parmi `read_file`, `write_file`, `run_tests`, `git_diff`, puis rédige pour
chacun :

1. un nom stable ;
1. une description courte et non ambiguë ;
1. un schéma d'entrée strict ;
1. une erreur attendue si l'argument est invalide ;
1. une règle de permission.

### ✅ Critères

- pas de propriété inutile ;
- pas de champ libre si un enum suffit ;
- pas de commande destructive ;
- pas de comportement implicite.

______________________________________________________________________

## 📦 Exercice 3 - Livrable Agent v0.2 : coding agent borné

Objectif : décrire un agent qui peut recevoir une consigne du type :

> "Ajoute une petite fonction au projet, mets à jour le code, puis prouve que ça marche."

### 🛠️ Contraintes

- l'agent doit commencer par lire ;
- il doit écrire uniquement dans un périmètre autorisé ;
- il doit lancer les tests après la modification ;
- il doit produire un résumé final lisible ;
- il doit refuser toute action hors permissions.

### 📓 À rendre

Un court document ou pseudo-code qui contient :

- la liste des tools ;
- les permissions associées ;
- le flux d'exécution ;
- le message d'erreur en cas de refus ;
- la condition de sortie.

### ✅ Critères de validation

- [ ] L'environnement est minimal et explicitement borné.
- [ ] Chaque tool a un contrat lisible.
- [ ] Le runtime valide avant d'exécuter.
- [ ] L'agent teste après écriture.
- [ ] Le résumé final explique le patch et le résultat.

______________________________________________________________________

## 🎁 Bonus (facultatif)

- Retire un tool de lecture, puis observe ce qui devient impossible.
- Ajoute un tool trop puissant, puis liste les garde-fous qu'il faudrait exiger avant de
  l'exposer.
