# 🛂 03.4 - Checkpoints et human approval

## 💾 Pourquoi checkpointé ?

Un checkpoint est une photographie stable du state. Il permet de répondre à trois
questions :

1. Qu'est-ce qui était vrai à ce moment du run ?
1. Peut-on reprendre sans rejouer les étapes précédentes ?
1. Quelle décision humaine ou automatique a autorisé la suite ?

Sans checkpoint, un workflow long redevient une conversation opaque.

## 🧱 Bons emplacements de checkpoint

Dans la Factory v0.3, deux checkpoints sont obligatoires :

| Checkpoint       | Pourquoi ici ?                                      |
| ---------------- | --------------------------------------------------- |
| Après `PLAN`     | le plan devient le contrat d'implémentation         |
| Après `TEST`     | le résultat qualité justifie review ou correction   |

On pourrait aussi sauvegarder après `REQUEST`, mais la demande originale doit déjà être
immuable dans le state.

## 🧑‍⚖️ Human approval n'est pas un bouton magique

Une approbation humaine doit être petite et décidable. Ne demande pas :

> "Est-ce que tout te semble bon ?"

Demande plutôt :

```text
Plan proposé : ...
Risques : ...
Fichiers probablement touchés : ...
Budget : ...
Décision attendue : approved | rejected | needs_changes
Commentaire obligatoire si rejected ou needs_changes.
```

Le workflow reprend ensuite à un node précis, avec la décision écrite dans le state.

## 🚧 Où bloquer le graphe ?

Deux blocages sont utiles dès v0.3 :

1. **Avant `IMPLEMENT`** : éviter qu'un modèle modifie le code sur un plan non validé.
1. **Avant `PR`** : éviter de publier une proposition dont tests ou review ne sont pas
   acceptables.

La validation du merge arrivera plus tard, avec les policies du chapitre 09 et la PR
Factory du chapitre 11.

## 🔁 Reprise après rejet

Un rejet ne doit pas effacer le run. Il ajoute une information :

```text
human_decision:
  node: APPROVE_PLAN
  decision: needs_changes
  comment: "Réduire le scope au parser, pas au renderer."
```

Le conditional edge peut alors revenir vers `PLAN` avec une contrainte supplémentaire, ou
arrêter proprement si le budget est dépassé.

## 💡 À retenir

1. Un checkpoint est une frontière de reprise et d'audit.
1. Une approbation humaine doit produire une donnée structurée.
1. On ne rejoue jamais gratuitement une étape déjà validée.

-> Slide suivante : [`05-factory-v03.md`](05-factory-v03.md)
