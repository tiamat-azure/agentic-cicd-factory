# 🌉 10.5 - Préparer la PR Factory

## 🔜 Ce que le chapitre 11 ajoutera

Le chapitre 11 demandera à la Factory de créer une PR à partir d'une demande. Cela ajoute
un risque : l'agent ne se contente plus d'analyser, il propose un changement intégrable.

## 🧩 Ce que le chapitre 10 doit fournir avant

Avant de générer des PR automatiquement, il faut déjà savoir :

- quels checks sont requis ;
- quelles evals sont obligatoires selon le changement ;
- quels seuils bloquent ;
- quelle policy décide `pass`, `block` ou `needs-human-approval` ;
- quels artefacts seront joints à la PR.

## 📝 Contrat pour une future PR automatique

Une PR générée par agent devra expliquer :

| Question | Preuve attendue |
| -------- | --------------- |
| Pourquoi ce changement ? | demande source + plan |
| Quels fichiers ont changé ? | diff et classification |
| Quels risques sont touchés ? | matrice de déclenchement |
| Quelles evals ont tourné ? | résultats + baseline |
| Pourquoi merger ou bloquer ? | décision de policy |

## 🚦 Gate final en préparation

Le gate final du parcours arrivera au chapitre 11 : une PR générée automatiquement à
partir d'une demande. Le chapitre 10 en construit le prérequis : aucune PR automatique ne
passe sans preuve mesurée.
