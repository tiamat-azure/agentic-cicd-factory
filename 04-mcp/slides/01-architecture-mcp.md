# 🧱 Architecture MCP

## 🎯 Idée clé

MCP sépare le **client qui demande** d'une **capacité** et le **serveur qui l'expose**.
Le host orchestre la relation, le client parle le protocole, le serveur publie ses
capacités.

## 🧩 Les 3 acteurs

- **Host** : l'application qui pilote l'expérience agentique.
- **Client** : l'adaptateur qui dialogue avec un serveur MCP.
- **Server** : le fournisseur de capacités, de contexte ou de prompts.

## 🗺️ Pourquoi c'est utile

Avant MCP, chaque tool était souvent codé comme un cas particulier dans l'agent.

Avec MCP, les capacités deviennent :

- découvrables ;
- versionnables ;
- isolables ;
- remplaçables sans casser le reste du système.

## 🌉 Lecture pour la Factory

Dans la Factory, le host reste le workflow orchestrateur.

Le serveur MCP, lui, peut porter :

- l'accès au filesystem ;
- l'accès à Git ;
- l'accès à la CI ;
- l'accès à GitHub ou à un autre backend.

Le graphe ne change pas : il appelle seulement des capacités mieux encapsulées.
