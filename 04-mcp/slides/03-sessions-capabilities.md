# 🔄 Sessions et capability negotiation

## 🎯 Idée clé

Une session MCP permet de garder un échange cohérent dans le temps, tandis que la
capability negotiation permet au host de découvrir ce que le serveur sait faire.

## 🧵 Sessions

Une session sert à :

- relier plusieurs appels au même échange ;
- conserver un contexte minimal ;
- distinguer une interaction en cours d'un simple appel ponctuel.

## 🤝 Capability negotiation

Avant d'appeler un serveur, le client apprend :

- quels tools sont disponibles ;
- quelles resources sont lisibles ;
- quels prompts sont publiés ;
- quelles limites ou options sont supportées.

## 🧭 Conséquence pratique

Le host peut adapter son comportement :

- s'il manque une capacité, il évite de l'utiliser ;
- s'il existe plusieurs serveurs, il choisit celui qui convient ;
- s'il y a plusieurs niveaux de permission, il n'active que le minimum utile.

## 🌉 Pour la Factory

La Factory ne doit jamais supposer qu'un serveur expose exactement la même surface qu'un
tool local. Elle doit d'abord découvrir, puis décider.
