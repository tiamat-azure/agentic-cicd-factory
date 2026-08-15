# 🧮 Construire une matrice de permissions

## 🎯 Idée clé

Une permission n'est pas un rôle vague comme "agent admin". C'est une capacité précise sur
une cible précise, avec une décision explicite.

## 🧩 Capacités de base

| Capacité | Question de gouvernance |
| -------- | ----------------------- |
| `repo.read` | L'agent peut-il lire ce dépôt ? |
| `repo.write_branch` | Peut-il écrire sur une branche dédiée ? |
| `repo.create_pr` | Peut-il proposer une PR ? |
| `repo.merge_pr` | Peut-il intégrer dans la branche protégée ? |
| `ci.run` | Peut-il déclencher des checks ? |
| `deploy.staging` | Peut-il déployer en environnement non critique ? |
| `deploy.production` | Peut-il toucher la production ? |
| `secrets.read` | Peut-il lire des secrets ? |

## 🧱 Exemple de matrice

| Action | Agent | Mainteneur | CI/CD | Décision par défaut |
| ------ | ----- | ---------- | ----- | ------------------- |
| Lire le code | oui | oui | oui | `auto` |
| Écrire `agent/*` | oui | oui | non | `auto` si sandbox OK |
| Ouvrir une PR | oui | oui | non | `auto` si evals OK |
| Merger une PR | non | oui | oui | `human` puis CI |
| Déployer staging | non | oui | oui | `human` si changement risqué |
| Déployer production | non | oui | oui | `human` obligatoire |
| Lire un secret | non | non sauf break-glass | oui si nécessaire | `deny` pour l'agent |

## ⚠️ Point important

Une matrice de permissions décrit les droits maximaux. La policy finale peut encore réduire
ces droits selon le contexte : fichier touché, score d'eval, type de demande, environnement
ou niveau de risque.
