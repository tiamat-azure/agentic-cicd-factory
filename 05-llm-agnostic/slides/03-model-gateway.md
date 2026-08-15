# 🚪 03 - Le Model Gateway

## 🎯 Intention

Le Model Gateway est le point d'entrée unique vers les modèles. Il sélectionne un provider,
adapte les entrées, normalise les sorties et expose une surface stable au workflow.

## 🧱 Responsabilités

Le gateway doit :

- lire la configuration du modèle actif ;
- instancier le bon provider ;
- vérifier que les capacités demandées existent ;
- appeler le provider ;
- normaliser la réponse ;
- normaliser les erreurs ;
- journaliser les informations minimales utiles au diagnostic.

Il ne doit pas décider de la stratégie métier du workflow. Cette séparation prépare le
routeur du chapitre 06.

## ⚙️ Sélection par configuration

Exemple de configuration cible :

```yaml
model_gateway:
  default: local-qwen
  providers:
    claude:
      type: anthropic
      model: claude-3-5-sonnet-latest
    local-qwen:
      type: openai_compatible
      base_url: http://localhost:11434/v1
      model: qwen2.5-coder
```

Le workflow ne lit pas `type`, `base_url` ou `model`. Il demande seulement au gateway le
modèle configuré.

## 🧭 Frontière avec MCP

MCP standardise l'accès aux tools et au contexte. Le Model Gateway standardise l'accès aux
LLM.

```text
Workflow
 ├── MCP Client -> tools/resources/prompts
 └── Model Gateway -> génération de texte et tool calls
```

Ces deux frontières sont complémentaires : les tools ne doivent pas connaître le modèle,
et le modèle ne doit pas connaître l'implémentation locale des tools.

## ✅ Critère de réussite

Ajouter un provider revient à créer un nouvel adaptateur et une nouvelle entrée de
configuration, pas à modifier les nodes métier.
