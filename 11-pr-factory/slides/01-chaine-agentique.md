# 🔗 Chaîne agentique de la PR Factory

## 🎯 Objectif

Construire une PR automatique ne consiste pas à laisser un agent coder puis cliquer sur
"ouvrir une PR". Le chapitre assemble des agents qui se contrôlent mutuellement et
transmettent des preuves.

## 🧱 Rôles de la chaîne

| Agent | Responsabilité | Ne doit pas faire |
| ----- | -------------- | ----------------- |
| Requirement Agent | reformuler la demande, détecter ambiguïtés, écrire les critères | modifier le code |
| Architecture Agent | proposer le plan, les fichiers probables et les risques | contourner la policy |
| Coding Agent | produire un diff borné par le plan | valider seul son diff |
| Test Agent | choisir et lancer les validations adaptées | inventer un résultat de test |
| Review Agent | détecter bugs, dette et incohérences | remplacer une review humaine sensible |
| Security Agent | vérifier secrets, permissions, injection et sandbox | élargir les droits |
| Evaluation runner | comparer à la baseline et aux seuils | changer les seuils pour passer |
| PR Composer | résumer preuves et décisions dans la PR | cacher les incertitudes |

## 🔁 Handoff vérifiable

Chaque handoff répond à quatre questions :

1. Quelle décision vient d'être prise ?
1. Sur quelles preuves ?
1. Quel budget a été consommé ?
1. Quel arrêt humain reste possible ?

Si une étape ne peut pas répondre, elle ne passe pas le relais en `auto`.

## 🚦 Exemple de flux

```text
Demande : "Ajoute un budget coût au routeur de modèle"
Requirement -> critères : budget visible, dépassement bloquant, message explicite
Architecture -> plan : modifier budget policy + tests de dépassement
Policy -> auto : fichiers autorisés, pas de secret, risque faible
Coding -> diff : policy + tests
Test -> pass : tests ciblés exécutés
Review -> pass : pas de régression évidente
Security -> pass : aucun secret, permissions inchangées
Evaluation -> pass : score stable, coût sous budget
PR Composer -> auto-open PR avec reviewer mainteneur
```

## 🛑 Points d'arrêt

- Ambiguïté de la demande : arrêt avant architecture.
- Plan qui touche auth, secrets, policy ou workflow critique : humain avant codage.
- Diff hors scope : humain avant tests.
- Test ou eval critique en échec : humain ou refus.
- PR body incomplet : humain avant ouverture.
