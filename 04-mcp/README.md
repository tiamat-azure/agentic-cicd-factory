# 🔌 04 - MCP : transformer les Tools en plateforme

> Livrable : **Agentic CI/CD Factory v0.4** - au moins 3 tools natifs remplacés par des
> serveurs MCP, sans changer l'architecture du workflow.

## 🎯 Objectifs pédagogiques

- Comprendre MCP comme un contrat standard Host / Client / Server, pas comme un
  framework d'agent.
- Distinguer clairement tools, resources, prompts, sessions et capability negotiation.
- Savoir ce que MCP standardise, ce qu'il isole, et ce qu'il ne doit surtout pas exposer.
- Migrer progressivement des tools natifs vers des serveurs MCP sans réécrire le graphe.
- Préparer le chapitre 05 : la couche tool/context change, pas la logique métier.

## ✅ Prérequis

- Chapitre 03 (Workflows & orchestration).
- Savoir expliquer le flux `REQUEST -> ANALYZE -> PLAN -> IMPLEMENT -> TEST -> REVIEW ->
  PR`.
- Avoir identifié au moins 3 actions de la Factory candidates pour une externalisation.
- Durée estimée : **3 h** (1 h théorie + 1 h lecture guidée + 1 h exercices).

## 🚪 Gate du chapitre

> **Gate 2 (partie 2/2)** : tu sais remplacer au moins 3 tools natifs par des serveurs
> MCP, expliquer les frontières de sécurité, et montrer que le graphe ne change pas.

## 🧭 Parcours pas à pas

| Étape | Support                                                      | Ce que tu fais                                   |
| ----- | ------------------------------------------------------------ | ------------------------------------------------ |
| 1     | [`slides/01-architecture-mcp.md`](slides/01-architecture-mcp.md) | Lire : Host / Client / Server                    |
| 2     | [`slides/02-tools-resources-prompts.md`](slides/02-tools-resources-prompts.md) | Lire : les 3 primitives exposées                 |
| 3     | [`slides/03-sessions-capabilities.md`](slides/03-sessions-capabilities.md) | Lire : sessions et capability negotiation        |
| 4     | [`slides/04-security-boundaries.md`](slides/04-security-boundaries.md) | Lire : sécurité, permissions, surfaces d'attaque |
| 5     | [`slides/05-migration-path.md`](slides/05-migration-path.md) | Lire : migration native tools -> MCP             |
| 6     | [`demos/README.md`](demos/README.md)                        | Parcourir : trace avant / après                  |
| 7     | [`exercices/README.md`](exercices/README.md)                | Faire les 3 exercices -> **Tools via MCP**       |
| 8     | [`solutions/README.md`](solutions/README.md)                | Comparer après coup : pas avant d'avoir tenté    |

## 📚 Plan théorique

1. Pourquoi MCP existe : standardiser l'accès aux tools et au contexte.
1. Architecture MCP : Host, Client, Server, transport, cycle de vie.
1. Tools, resources et prompts : trois façons différentes d'exposer des capacités.
1. Sessions et capability negotiation : découvrir ce qu'un serveur sait faire.
1. Sécurité : moindre privilège, frontières explicites, secrets hors du scope.
1. Migration : remplacer des tools natifs sans casser le workflow ni le modèle mental.

## 🧱 Principes directeurs appliqués ici

- **Framework-agnostic** : on enseigne le protocole et l'architecture, pas un SDK.
- **Model-agnostic** : le modèle consomme des capacités décrites, pas des outils codés en
  dur.
- **Eval-first** : chaque migration se vérifie par les mêmes traces, les mêmes tests et
  les mêmes checkpoints que le reste de la Factory.

## 🌉 Continuité avec les chapitres 03 et 05

Le chapitre 03 a figé la forme du workflow : le graphe décide, le modèle exécute le
contenu demandé.

Le chapitre 04 ne change pas cette règle. Il remplace seulement la couche d'accès aux
capacités :

- avant : outils locaux codés dans l'agent ;
- maintenant : capacités standardisées exposées par des serveurs MCP ;
- après : le chapitre 05 ajoutera un Model Gateway, sans toucher au workflow ni aux
  contrats métier.

Autrement dit : **MCP change les adaptateurs, pas la responsabilité des nodes**.

## 🧩 Architecture cible

```text
User / Workflow
      │
      ▼
   MCP Host
      │
      ▼
   MCP Client
   ├── Filesystem Server
   ├── Git Server
   ├── CI Server
   └── GitHub Server
```

Le point clé : chaque serveur expose une surface plus petite et plus lisible qu'un set de
tools maison dispersés dans le code.

## 📦 Livrable

**Agentic CI/CD Factory v0.4** - une Factory qui remplace au moins 3 actions natives par
des serveurs MCP, par exemple :

- lecture/écriture de fichiers ;
- opérations Git locales ;
- exécution de validations CI ;
- ou ouverture de PR via une interface distante.

Le workflow reste le même ; seule la provenance des capacités change.

## 🔗 Ressources

- Model Context Protocol - [Architecture](https://modelcontextprotocol.io/specification/2025-06-18/architecture)
- Model Context Protocol - [Overview](https://modelcontextprotocol.io/)

## 📝 Auto-évaluation

Tu peux passer au chapitre 05 quand tu réponds sans hésiter :

1. Quelle différence fais-tu entre un tool, une resource et un prompt MCP ?
1. Qui négocie les capacités, et à quel moment ?
1. Qu'est-ce qui doit rester hors d'un serveur MCP pour des raisons de sécurité ?
1. Pourquoi un workflow peut rester identique alors que les tools changent ?
1. Quelles 3 capacités de la Factory remplacerais-tu en premier, et pourquoi ?
