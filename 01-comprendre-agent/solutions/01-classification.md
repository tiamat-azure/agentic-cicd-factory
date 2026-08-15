# ✅ Solution - exercice 1 : classification

> Ne lis ceci qu'après avoir écrit tes propres réponses.

| #   | Cas                                | Niveau                  | Justification                                                                                               |
| --- | ---------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1   | Message de commit depuis un diff   | **1 - chain**           | Une étape, entrée connue, sortie contrainte. Aucun besoin de décider.                                       |
| 2   | Traduire toute la doc              | **1 - chain** en boucle | Le flux est fixe ; c'est du batch, pas de la décision.                                                      |
| 3   | Diagnostiquer une CI devenue rouge | **3 - agent**           | Espace ouvert : on ne sait pas où chercher avant de chercher.                                               |
| 4   | Vérifier une convention de nommage | **0 - script**          | Une regex suffit. Un LLM ici est un coût pur et une source d'erreur.                                        |
| 5   | Ticket -> plan -> code -> PR       | **4 - multi-agent**     | Rôles distincts (plan/code/review), budgets et prompts distincts.                                           |
| 6   | Extraire des critères en JSON      | **1 - chain**           | Structured output, une passe. Valide par schéma, pas par agent.                                             |
| 7   | Décider de merger sur `main`       | **0 - humain / policy** | Irréversible. Décision de gouvernance, pas de génération (ch. 09).                                          |
| 8   | Migrer 200 fichiers, cas variés    | **2 ou 3**              | Workflow qui itère sur les fichiers, avec un **agent par fichier** si le cas est vraiment non déterministe. |

## ⚠️ Les deux pièges

- **Cas 4** : le seul vrai piège "pas de LLM". Beaucoup de gens répondent "chain".
- **Cas 7** : "agent" est tentant. Mais une décision irréversible avec règles métier
  explicites n'est pas un problème de génération : c'est un problème de policy.

## 🔎 La lecture d'ensemble

Sur 8 cas réalistes d'une usine CI/CD, **2 seulement** justifient un agent pur. C'est le
ratio à garder en tête pour tout le reste de la formation.

## 🧩 Cas 8 : le pattern important

```text
WORKFLOW (déterministe : itère sur les 200 fichiers, agrège, rapporte)
   └── pour chaque fichier ──> AGENT (borné : budget 5 itérations, 1 fichier)
```

Encapsuler un agent dans un workflow permet de **borner le non-déterminisme** : le coût
total reste prévisible, et un échec est localisé à un fichier. C'est le pattern par défaut
en production, on le reprend au chapitre 03.
