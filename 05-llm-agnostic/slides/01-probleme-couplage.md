# 🔗 01 - Le problème du couplage au modèle

## 🎯 Intention

Un agent devient fragile quand son code métier connaît trop de détails du fournisseur de
LLM : nom du SDK, format des messages, format des tool calls, erreurs HTTP ou options
spécifiques.

Le but du chapitre n'est pas de cacher que les modèles sont différents. Le but est de
placer ces différences au bon endroit.

## 🧨 Symptômes d'un agent couplé

- `agent.py` importe directement un SDK de provider.
- Les nodes du workflow construisent eux-mêmes des payloads HTTP.
- Les prompts métier contiennent des mentions de modèle ou de fournisseur.
- Le parsing des tool calls est dispersé dans plusieurs fichiers.
- Les erreurs de quota, timeout ou format invalide sont traitées comme des exceptions
  génériques.
- Changer de modèle impose de modifier le code métier.

## 🧭 Règle d'architecture

Le workflow exprime une intention : analyser, planifier, implémenter, tester, reviewer.

Le provider exprime une contrainte technique : comment appeler un modèle précis.

Entre les deux, il faut une frontière stable : le **Model Gateway**.

## 🏭 Application à la Factory

Après le chapitre 04, la Factory sait déjà externaliser des tools via MCP. Le même principe
s'applique ici :

```text
Node métier -> besoin de génération -> Model Gateway -> provider réel
```

Le node ne sait pas si la réponse vient d'un modèle cloud, d'Ollama ou d'un serveur vLLM.
Il sait seulement que le contrat a été respecté.

## ✅ Critère de réussite

Si tu peux changer le modèle actif sans modifier les nodes `ANALYZE`, `PLAN`, `IMPLEMENT`,
`TEST` ou `REVIEW`, le découplage commence à être correct.
