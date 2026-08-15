# 🏁 01.3 - State et terminaison

## ❓ Pourquoi un state explicite

Naïvement, le state d'un agent = la liste des messages. C'est vrai au début, et faux dès
que tu vises la production, pour trois raisons :

1. **La fenêtre de contexte est finie.** L'historique brut grossit sans limite (-> ch. 06,
   token engineering).
1. **Tout n'est pas à envoyer au modèle.** Un compteur d'itérations, un budget, un
   identifiant de trace : c'est du state, mais pas du contexte.
1. **Il faut pouvoir reprendre.** Un agent CI/CD qui tourne 20 minutes doit être
   interruptible et reprenable.

D'où la distinction fondamentale :

```text
        STATE (ce que ton runtime sait)
        ├── messages        ──> envoyés au modèle = CONTEXTE
        ├── iteration       ──> jamais envoyé
        ├── tokens_consommes──> jamais envoyé
        ├── trace_id        ──> jamais envoyé
        └── objectif        ──> envoyé une fois
```

> **Contexte ⊂ State.** Confondre les deux est la cause n°1 des agents qui explosent en
> coût. Retiens cette phrase, on la réutilisera au chapitre 06.

## 🧬 Anatomie minimale

```python
@dataclass
class AgentState:
    objectif: str
    messages: list[dict] = field(default_factory=list)
    iteration: int = 0
    max_iterations: int = 10
    termine: bool = False
    resultat: str | None = None
```

C'est volontairement pauvre. Chaque chapitre suivant y ajoutera un champ :

| Chapitre | Champ ajouté au state     |
| -------- | ------------------------- |
| 03       | `plan`, `sous_taches`     |
| 06       | `budget_tokens`, `resume` |
| 07       | `trace_id`, `spans`       |
| 09       | `approbations_requises`   |

## 🚦 Les conditions de terminaison

Un agent doit avoir **au moins trois** conditions d'arrêt. Une seule ne suffit jamais.

| Condition              | Type      | Signification                           | Sortie         |
| ---------------------- | --------- | --------------------------------------- | -------------- |
| Réponse finale         | naturelle | le modèle n'appelle plus de tool        | succès         |
| Tool `terminer`        | explicite | le modèle déclare la fin avec un statut | succès / échec |
| `max_iterations`       | garde-fou | la boucle n'aboutit pas                 | échec          |
| Budget tokens/€        | garde-fou | coût dépassé (-> ch. 06)                | échec          |
| Timeout                | garde-fou | latence dépassée                        | échec          |
| Erreur non rattrapable | garde-fou | ex. auth invalide                       | échec          |

### ⚖️ Naturelle vs explicite

- **Naturelle** : simple, mais ambiguë - le modèle a-t-il fini, ou abandonné ?
- **Explicite** (`terminer(statut, resume)`) : le modèle doit déclarer son statut. Bien
  plus évaluable, parce que tu obtiens un signal machine-lisible sur le succès.

> Pour une usine CI/CD, la terminaison explicite est **obligatoire** : une PR ne se merge
> pas sur un "il a l'air d'avoir fini".

Nous implémentons les deux dans la demo 3, et l'exercice 3 te fait basculer sur
l'explicite.

## ⚠️ Les 3 pathologies de boucle

```text
1. PING-PONG      : le modèle rappelle le même tool avec les mêmes args
   cause          : observation non réinjectée, ou résultat vide/illisible
   détection      : hash (nom + args) déjà vu à l'itération précédente

2. DÉRIVE         : le modèle travaille, mais plus sur l'objectif
   cause          : objectif noyé dans un historique trop long
   détection      : re-rappeler l'objectif ; borner l'historique (ch. 06)

3. FUITE EN AVANT : le modèle déclare "terminé" sans avoir rien fait
   cause          : objectif mal défini, ou tools inadaptés
   détection      : evals (ch. 08) - c'est indétectable à l'œil nu à l'échelle
```

Dans la demo 3, la boucle logue nom + args à chaque tour : c'est déjà un détecteur de
ping-pong à l'œil nu, et l'ancêtre direct des traces du chapitre 07.

## 💡 À retenir

1. `contexte ⊂ state`.
1. Trois conditions d'arrêt minimum, dont au moins un garde-fou dur.
1. La terminaison explicite est ce qui rend un agent évaluable.

-> Demo suivante : [`demos/03_agent_minimal/`](../demos/03_agent_minimal/)
