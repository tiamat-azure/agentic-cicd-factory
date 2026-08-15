# 🧬 04 - Les différences de providers à isoler

## 🎯 Intention

Être LLM-agnostic ne signifie pas prétendre que tous les modèles sont identiques. Cela
signifie que leurs différences sont déclarées, testées et confinées dans le gateway.

## 🧾 Différences fréquentes

| Sujet | Pourquoi ça compte |
| ----- | ------------------ |
| Format des messages | Chaque API encode les rôles et contenus différemment. |
| Tool calling | Certains modèles supportent des appels structurés, d'autres nécessitent un format texte. |
| JSON strict | Les garanties de sortie structurée varient fortement. |
| Taille de contexte | Le même prompt peut passer chez un provider et échouer chez un autre. |
| Comptage de tokens | Les compteurs exacts ne sont pas toujours disponibles localement. |
| Latence | Un modèle local peut être plus lent mais plus confidentiel. |
| Coût | Un modèle cloud facture, un modèle local consomme surtout de l'infrastructure. |
| Sécurité | Les données peuvent quitter ou non l'environnement local. |

## 🧱 Où placer l'adaptation

À faire dans le provider :

- transformer les messages normalisés vers le format du SDK ;
- adapter les schémas de tools ;
- convertir les réponses en `LLMResponse` ;
- convertir les erreurs techniques.

À éviter dans l'agent :

- choisir un prompt différent par provider ;
- parser plusieurs formats de tool calls ;
- supposer qu'un modèle supporte une capacité non déclarée ;
- masquer un échec de parsing par une réussite métier.

## 🧪 Différence acceptable ou régression ?

Une formulation différente est acceptable. Une tâche métier oubliée, un tool non autorisé
ou une sortie structurée non parseable est une régression.

Le chapitre 05 se concentre sur ces invariants métier. Le chapitre 06 optimisera ensuite
le choix du modèle selon budget, coût et complexité.
