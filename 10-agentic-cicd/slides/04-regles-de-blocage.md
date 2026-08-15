# 🚦 10.4 - Règles de blocage explicables

## 🎯 Pourquoi bloquer

Bloquer n'est pas punir l'équipe. C'est empêcher une version dont le risque est connu mais
non accepté de devenir la nouvelle baseline.

## 🧱 Blocages minimaux

| Condition | Décision | Justification |
| --------- | -------- | ------------- |
| Score critique sous seuil | `block` | qualité insuffisante sur un cas obligatoire |
| Régression au-delà de la tolérance | `block` | nouvelle version pire que la baseline |
| Coût par succès hors budget | `block` | optimisation locale trop chère globalement |
| Policy `deny` devenue `allow` | `block` ou approbation humaine | risque de permission élargie |
| Trace incomplète | `block` | décision impossible à auditer |
| Dataset modifié sans justification | `needs-human-approval` | baseline potentiellement manipulée |

## 🪪 Exceptions humaines

Une exception doit être plus stricte qu'un passage automatique. Elle contient :

- un propriétaire ;
- une raison ;
- une portée limitée ;
- une date d'expiration ;
- un lien vers les runs et les evals qui échouent ;
- une action de suivi.

## 🧠 Règle simple

Si tu ne peux pas expliquer pourquoi la pipeline a bloqué, la règle est trop opaque. Si tu
peux la contourner sans trace, la règle n'est pas une policy.
