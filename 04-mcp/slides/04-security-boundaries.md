# 🔐 Sécurité et frontières

## 🎯 Idée clé

MCP ne supprime pas la sécurité : il la rend plus visible.

## 🛡️ Ce qu'un serveur doit limiter

- lecture seulement quand l'écriture n'est pas nécessaire ;
- accès borné à un périmètre connu ;
- exposition minimale des secrets ;
- permissions explicites pour les actions risquées.

## 🚫 Ce qu'il ne faut pas faire

- exposer tout le repository "par confort" ;
- mélanger contexte métier et secrets ;
- laisser un serveur décider seul d'une action sensible ;
- faire passer un transport standard pour une confiance automatique.

## 🧪 Règle simple

Si une capacité peut modifier l'état du système, elle doit être :

- nommée clairement ;
- bornée ;
- traçable ;
- réversible quand c'est possible.

## 🌉 Lecture pour la Factory

Le serveur Git ne doit pas pouvoir faire n'importe quelle mutation.
Le serveur CI ne doit pas pouvoir lancer n'importe quel job.
Le serveur GitHub ne doit pas pouvoir ouvrir n'importe quelle PR sans garde-fous.
