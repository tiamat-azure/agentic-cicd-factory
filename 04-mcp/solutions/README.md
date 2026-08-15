# ✅ Solutions - chapitre 04

Ces solutions donnent une cible raisonnable, pas un corrigé unique. Compare-les à ton
travail après avoir tenté les exercices.

## 🧱 Solution 1 - Cartographier les capacités

- **tool** : `filesystem.read`, `ci.run_tests`, `github.create_pr`.
- **resource** : `plan_validé`, `trace_checkpoint`, `policy_merge`.
- **prompt** : `résume le risque`, `prépare la revue`, `explique l'échec`.

Le point important est la fonction :

- un tool agit ;
- une resource éclaire ;
- un prompt oriente.

## 🔄 Solution 2 - Session MCP

Une bonne description de session doit dire :

- le host découvre les capacités disponibles ;
- le client choisit le serveur adapté ;
- la session relie plusieurs appels cohérents ;
- les secrets et politiques sensibles ne doivent pas être persistés comme du contexte banal.

Le protocole permet de continuer un échange sans réinventer le contrat à chaque appel.

## 🛤️ Solution 3 - Migration MCP

### 🧩 Cibles raisonnables

1. **Filesystem** : lecture/écriture de fichiers.
1. **Git** : diff, status, branche, préparation de patch.
1. **CI** : lancement et lecture des validations.

### 🔐 Sécurité

- droits plus explicites ;
- surface d'exposition réduite ;
- séparation entre accès et décision ;
- meilleure lisibilité des opérations à effet de bord.

### 🌉 Ce qui reste identique

- le workflow ;
- les checkpoints ;
- les approbations humaines ;
- les critères d'acceptation.

Le chapitre 05 pourra ensuite remplacer le provider de modèle sans rouvrir cette partie.
