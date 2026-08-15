# 🏗️ 10.1 - Du prototype agentique au produit livrable

## ❓ Pourquoi la CI classique ne suffit pas

Une CI classique vérifie surtout que le code compile, que les tests passent et que les
artefacts se construisent. Pour une Factory agentique, ce n'est pas assez : le comportement
peut changer sans changer beaucoup de code.

Exemples :

- une phrase de prompt rend l'agent plus agressif ;
- un tool accepte un argument plus large ;
- un modèle différent respecte moins bien les consignes ;
- une policy autorise une action qui était bloquée ;
- un workflow déplace l'approbation humaine après l'action.

## 🧱 Ce qui devient livrable

La Factory livre plus que du Python ou du YAML. Elle livre un comportement :

| Élément | Question CI/CD |
| ------- | -------------- |
| Prompt | Le comportement attendu tient-il toujours ? |
| Tool | L'action externe est-elle validée et bornée ? |
| Modèle | La qualité et le coût restent-ils acceptables ? |
| Workflow | Les gates sont-ils encore dans le bon ordre ? |
| Policy | Les permissions sont-elles toujours justifiées ? |
| Eval | Le thermomètre mesure-t-il encore le bon risque ? |

## 🎯 Objectif du chapitre

Transformer ces éléments en artefacts versionnés, évalués et bloquants. La règle est
simple : si un changement peut modifier une décision de l'agent, il doit être visible dans
la CI/CD.

## 🔁 Pont depuis le chapitre 09

Le Policy Engine dit : « cette action est autorisée ou refusée ». La CI/CD dit : « cette
nouvelle version du Policy Engine peut-elle être livrée ? ».
