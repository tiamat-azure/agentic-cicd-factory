# 🧰 Tools, resources et prompts

## 🎯 Idée clé

MCP n'expose pas qu'une liste de tools. Il peut exposer trois familles de capacités.

## 🛠️ Tools

Un **tool** réalise une action.

Exemples dans la Factory :

- lire un fichier ;
- lancer une validation ;
- créer une PR ;
- récupérer un diff.

Un tool doit être explicite, borné et testable.

## 📚 Resources

Une **resource** fournit du contexte.

Exemples :

- un README de chapitre ;
- une politique de merge ;
- un état checkpointé ;
- un log d'exécution.

Une resource n'est pas une action : c'est une source de vérité consultable.

## 💬 Prompts

Un **prompt** fournit une intention pré-packagée.

Exemples :

- "résume le changement demandé" ;
- "prépare la revue" ;
- "liste les risques de sécurité".

Le prompt aide à standardiser les usages sans figer le contenu métier.

## 🧠 Pourquoi séparer ces trois notions

- un tool agit ;
- une resource informe ;
- un prompt guide.

Les confondre produit vite des agents opaques et difficiles à sécuriser.
