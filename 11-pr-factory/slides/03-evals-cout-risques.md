# 📊 Evals, coût et risques dans la PR

## 🎯 Objectif

Une PR automatique est acceptable seulement si elle expose la qualité mesurée, le coût et
les risques résiduels au même endroit.

## 📏 Métadonnées minimales

| Catégorie | Champs |
| --------- | ------ |
| Trace | `run_id`, `trace_id`, commit, CI run |
| Evals | suite, baseline, seuil, score actuel, delta, décision |
| Coût | route, modèles, tokens, tool calls, itérations, latence, coût estimé |
| Risque | fichiers sensibles, secrets, permissions, findings, policy decision |

## 🧮 Lecture coût / qualité

Une PR peu coûteuse mais fausse n'est pas une réussite. Une PR correcte mais dix fois trop
chère n'est pas scalable. La métrique utile reste :

```text
valeur = résultat validé / coût total du run
```

La PR doit donc montrer le résultat validé et le coût, pas seulement l'un des deux.

## 🚦 Décisions possibles

| Signal | Décision |
| ------ | -------- |
| Tous les seuils passent, coût sous budget, risques faibles | `auto-open` |
| Qualité acceptable mais changement sensible ou validation partielle | `human-before-open` ou PR avec review obligatoire |
| Seuil critique en échec, policy deny, secret exposé | `deny` |

## 🧭 Bon usage des deltas

Comparer uniquement le score courant peut tromper. La PR doit montrer :

- la baseline utilisée ;
- le score courant ;
- le seuil absolu ;
- la tolérance de régression ;
- l'explication si le résultat demande une exception.
