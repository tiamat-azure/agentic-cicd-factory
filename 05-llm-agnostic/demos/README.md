# 🧪 Demos - Swap de modèle sans changer l'agent

## 🎯 Objectif

Cette démonstration est une lecture guidée, volontairement centrée sur l'architecture. Elle
montre ce qui doit changer lors d'un swap de modèle : la configuration et l'adaptateur,
jamais le code métier de l'agent.

## 🧭 Situation de départ

Après le chapitre 04, la Factory possède :

- un workflow stable `REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW -> PR` ;
- des tools ou resources exposés via MCP ;
- des nodes métier qui demandent au modèle d'analyser, planifier ou produire une sortie
  structurée.

Le risque : ces nodes appellent directement un SDK de modèle.

## 🧩 Étape 1 - Identifier la frontière

Cherche dans l'implémentation les endroits qui :

- importent un SDK de provider ;
- construisent un payload spécifique ;
- parsèrent des tool calls spécifiques ;
- traitent des erreurs HTTP provider.

Tout cela doit sortir du code métier et rejoindre un provider ou le gateway.

## 📜 Étape 2 - Stabiliser le contrat

Le workflow doit dépendre uniquement de trois idées :

```text
generate -> produire une réponse
capabilities -> déclarer ce qui est supporté
count_tokens -> estimer la taille avant appel
```

Si une capacité manque, le gateway doit échouer explicitement plutôt que laisser le node
métier bricoler une exception.

## ⚙️ Étape 3 - Changer seulement la configuration

Exemple de swap attendu :

```yaml
model_gateway:
  default: claude
```

puis :

```yaml
model_gateway:
  default: local-qwen
```

La différence se limite à la configuration et aux adaptateurs disponibles.

## 🧪 Étape 4 - Rejouer le même scénario

Utilise le même prompt de demande, les mêmes tools MCP autorisés et les mêmes checks. Le
verdict porte sur les invariants, pas sur le style :

- tâches identifiées ;
- plan exploitable ;
- tools autorisés ;
- sortie structurée parseable ;
- erreur claire si une capacité manque.

## ✅ Résultat attendu

Le swap est réussi si le diff de code métier est vide. Toute modification dans un node du
workflow est un signal que la frontière du gateway fuit encore.
