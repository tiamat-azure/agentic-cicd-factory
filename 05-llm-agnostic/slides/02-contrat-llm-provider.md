# 📜 02 - Le contrat LLMProvider

## 🎯 Intention

`LLMProvider` est le contrat minimal que le reste de l'agent a le droit de connaître. Il ne
représente pas un fournisseur précis ; il représente une capacité de génération.

## 🧩 Méthodes minimales

```text
generate(messages, tools, response_format) -> LLMResponse
count_tokens(messages) -> TokenEstimate
capabilities() -> ModelCapabilities
```

Ce contrat peut être codé comme une classe abstraite, un protocole Python ou une interface
équivalente. Le choix technique importe moins que la stabilité de la frontière.

## 📥 Entrée normalisée

L'entrée doit éviter les détails de provider :

- messages avec rôles et contenu ;
- tools décrits par un schéma commun ;
- format de réponse attendu quand il existe ;
- paramètres métier stables : température, limite de sortie, timeout.

## 📤 Sortie normalisée

La sortie doit rendre comparables les providers :

- texte produit ;
- tool calls éventuels ;
- raison d'arrêt ;
- usage de tokens si le provider le fournit ;
- métadonnées techniques isolées du code métier.

## 🧰 Capacités déclarées

`ModelCapabilities` évite les suppositions :

| Capacité | Question à poser |
| -------- | ---------------- |
| Contexte | Quelle taille maximale d'entrée ? |
| Tool calling | Le modèle sait-il demander des tools de façon structurée ? |
| JSON strict | Peut-on exiger une sortie parseable ? |
| Streaming | La réponse peut-elle arriver progressivement ? |
| Vision | Le modèle accepte-t-il des images ? |
| Localité | Les données sortent-elles de la machine ? |

## ⚠️ Erreurs normalisées

Le gateway doit transformer les erreurs provider en catégories actionnables :

- configuration invalide ;
- authentification impossible ;
- quota ou rate limit ;
- timeout ;
- capacité non supportée ;
- réponse invalide ou non parseable.

## ✅ Critère de réussite

Un node métier doit pouvoir appeler `generate` et traiter `LLMResponse` sans savoir quel SDK
a réellement été utilisé.
