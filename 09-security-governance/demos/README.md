# 🧪 Demos - Lire une policy de gouvernance

Ces demos sont déclaratives : pas de commande à exécuter. L'objectif est de lire une policy
comme un contrat de sécurité, puis de vérifier qu'elle couvre les scénarios d'eval.

## 📄 Fichiers

- [`policy-engine-v09.toml`](policy-engine-v09.toml) : exemple minimal de Policy Engine.
- [`security-eval-cases.toml`](security-eval-cases.toml) : scénarios que le chapitre 10
  pourra transformer en checks CI/CD.

## 🔎 Questions de lecture

1. Quelle identité exécute chaque action ?
1. Quelles actions sont `auto`, `human` ou `deny` ?
1. Quelle règle empêche l'agent de lire un secret ?
1. Quel seuil d'eval peut transformer une action automatique en validation humaine ?
1. Quel cas deviendra un gate CI/CD au chapitre 10 ?
