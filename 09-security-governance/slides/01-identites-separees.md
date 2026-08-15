# 🪪 Séparer les identités

## 🎯 Idée clé

Un agent ne doit jamais agir comme "la personne qui l'a lancé". Il doit agir avec une
identité dédiée, traçable, limitée et révocable.

## 👥 Quatre identités à distinguer

| Identité | Rôle | Exemple de droits |
| -------- | ---- | ----------------- |
| Utilisateur | formule la demande | créer une demande, lire le résultat |
| Agent | exécute le workflow | lire le repo, écrire une branche dédiée |
| Mainteneur humain | approuve le risque | valider une PR, autoriser un déploiement |
| Service CI/CD | applique le pipeline | lancer tests, publier artefacts, déployer si gate validé |

Ces identités peuvent appartenir à la même organisation, mais elles ne doivent pas partager
le même jeton, le même niveau de droits, ni le même journal d'audit.

## 🚫 Anti-patterns

- Donner à l'agent le token personnel d'un mainteneur.
- Laisser l'agent pousser directement sur `main`.
- Confondre "l'utilisateur a demandé" avec "l'utilisateur a approuvé".
- Masquer les actions de l'agent derrière un compte générique non traçable.

## ✅ Règle pratique

Chaque action sensible doit répondre à deux questions séparées :

1. Qui a demandé cette action ?
1. Quelle identité technique l'exécute réellement ?

Si la réponse est la même par confort, la gouvernance est probablement trop faible.
