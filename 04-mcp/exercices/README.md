# ✏️ Exercices - chapitre 04

Trois exercices progressifs. Le 3 est le livrable **Tools via MCP**. Travaille dans
`exercices/`, compare avec `solutions/` **après** avoir tenté.

| # | Exercice | Compétence visée | Durée |
| - | -------- | ---------------- | ----- |
| 1 | Cartographier les capacités | distinguer tool, resource, prompt | 25 min |
| 2 | Décrire une session | comprendre discovery et négociation | 30 min |
| 3 | Planifier la migration MCP | remplacer 3 tools natifs sans casser le workflow | 60 min |

______________________________________________________________________

## 🧭 Exercice 1 - Cartographier les capacités

À partir de la Factory v0.3, prends 5 capacités et classe-les en :

1. **tool** ;
1. **resource** ;
1. **prompt**.

Pour chaque choix, écris une phrase de justification.

______________________________________________________________________

## 🔄 Exercice 2 - Décrire une session

Écris `exercices/02-session.md` et décris le cycle suivant :

1. découverte des capacités ;
1. sélection d'un serveur ;
1. exécution d'un tool ;
1. continuation dans la même session.

Tu dois indiquer :

- ce que le host doit connaître avant d'appeler ;
- ce qui peut être découvert dynamiquement ;
- ce qui ne doit pas être stocké dans la session.

______________________________________________________________________

## 🛤️ Exercice 3 - Planifier la migration MCP

Crée `exercices/03-migration.md`.

Le document doit contenir :

1. les 3 tools natifs que tu remplaces en premier ;
1. le serveur MCP cible pour chacun ;
1. les permissions qui changent ;
1. les risques de sécurité introduits ou réduits ;
1. ce qui reste strictement identique dans le workflow.

### ✅ Critères de validation du livrable

- [ ] Les 3 choix sont cohérents avec la Factory.
- [ ] Le workflow n'est pas réécrit pour la migration.
- [ ] Les frontières de sécurité sont explicites.
- [ ] Les différences entre tool, resource et prompt sont correctes.
- [ ] Le document indique clairement ce qui changera au chapitre 05.

______________________________________________________________________

## 🎁 Bonus (facultatif)

Décris une stratégie de migration en deux temps :

1. d'abord un serveur MCP "lecture seule" ;
1. ensuite les actions à effet de bord.
