# 🎬 Slides - chapitre 04

Ce chapitre est conceptuel : les slides servent à stabiliser le vocabulaire MCP avant de
brancher des serveurs concrets.

## 🧭 Ordre de lecture

1. Lire l'architecture MCP et le rôle des trois acteurs.
1. Distinguer tools, resources et prompts.
1. Comprendre sessions et capability negotiation.
1. Identifier les frontières de sécurité.
1. Construire la migration native tools -> MCP sans toucher au workflow.

## 📑 Sommaire

| # | Leçon | Idée principale |
| - | ----- | --------------- |
| 1 | [`01-architecture-mcp.md`](01-architecture-mcp.md) | Host / Client / Server |
| 2 | [`02-tools-resources-prompts.md`](02-tools-resources-prompts.md) | Les 3 primitives exposées |
| 3 | [`03-sessions-capabilities.md`](03-sessions-capabilities.md) | Sessions et négociation |
| 4 | [`04-security-boundaries.md`](04-security-boundaries.md) | Sécurité et moindre privilège |
| 5 | [`05-migration-path.md`](05-migration-path.md) | Migration depuis les tools natifs |

## 🎯 Résultat attendu

À la fin des slides, tu dois pouvoir expliquer pourquoi MCP standardise l'accès aux
capacités sans standardiser ton architecture métier.
