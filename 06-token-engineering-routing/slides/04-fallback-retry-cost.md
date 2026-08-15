# 🔁 Fallback, retry et coût par succès

## 🎯 Idée clé

Retry et fallback améliorent la robustesse, mais ils peuvent aussi détruire le budget. Ils
doivent être rares, bornés et mesurés.

## 🔄 Retry

Un retry relance la même route pour corriger un problème probablement transitoire.

Retry possible :

- erreur fournisseur temporaire ;
- rate limit avec attente autorisée ;
- sortie structurée invalide mais corrigeable ;
- timeout court sur une action idempotente.

Retry interdit :

- budget déjà dépassé ;
- permission refusée ;
- erreur de test déterministe ;
- tool non idempotent déjà exécuté ;
- demande ambiguë qui nécessite un humain.

## 🚀 Fallback

Un fallback change de profil, souvent vers plus capable ou plus coûteux.

Fallback possible :

- fenêtre de contexte insuffisante ;
- capacité absente du profil initial ;
- quality gate échoué malgré une sortie valide ;
- tâche reclassifiée après analyse.

Fallback interdit :

- escalade infinie ;
- contournement d'un budget validé ;
- contournement d'une policy de sécurité ;
- remplacement systématique des evals par "essayons plus gros".

## 💰 Coût par tâche réussie

La métrique centrale est :

```text
cost_per_success = somme(cost_usd de tous les runs) / nombre de tâches réussies
```

Elle inclut les échecs, retries et fallback. C'est volontaire : un modèle bon marché qui
échoue souvent coûte cher en pratique.

## 📊 Comparaison correcte

Compare par classe de tâche :

| Classe | Route A | Route B | À regarder |
| ------ | ------- | ------- | ---------- |
| `simple` | local | cloud | coût par succès et latence |
| `medium` | local-large | cloud | taux de fallback et qualité |
| `complex` | cloud | local puis cloud | coût des échecs avant escalade |

Une seule moyenne globale peut cacher un routeur mauvais sur les tâches critiques.

## 🔭 Préparation du chapitre 07

À partir de maintenant, chaque run doit être explicable :

- pourquoi cette route ?
- quel budget était actif ?
- combien de retries ?
- quel fallback ?
- quel coût final ?
- succès métier ou échec qualifié ?

Le chapitre 07 transformera ces réponses en traces consultables et dashboards.
