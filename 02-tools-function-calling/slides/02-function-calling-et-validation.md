# 🧾 02.2 - Function calling, schémas et validation

## 🎯 Ce qu'il faut comprendre

Le modèle ne doit jamais "inventer" l'interface d'un tool. Il doit choisir parmi des
contrats explicites :

- un **nom** stable ;
- une **description** utile ;
- un **schéma d'entrée** strict ;
- une **sortie** lisible par machine ;
- une **erreur** prévisible.

## 🧩 Le contrat d'un tool

```json
{
  "name": "read_file",
  "description": "Lit un fichier du dépôt. N'utilise ce tool que si tu connais déjà le chemin.",
  "input_schema": {
    "type": "object",
    "properties": {
      "path": { "type": "string", "description": "Chemin relatif au dépôt" }
    },
    "required": ["path"],
    "additionalProperties": false
  }
}
```

La description n'est pas du décor : c'est souvent ce que le modèle lit le plus vite pour
choisir son action.

## 🧪 Validation en 3 couches

1. **Validation de forme** : le JSON est-il conforme au schéma ?
1. **Validation métier** : le chemin est-il dans la sandbox ? la commande est-elle
   autorisée ?
1. **Validation post-exécution** : le résultat correspond-il à ce qu'on attendait ?

> Si une couche échoue, le runtime renvoie une observation claire. Le modèle peut alors
> corriger son action au tour suivant.

## 🧠 Structured output

Quand le modèle doit produire une réponse finale, la même logique s'applique :

- statut ;
- résumé ;
- artefacts produits ;
- confiance / limites ;
- prochaine action conseillée.

Plus la sortie est structurée, plus elle est exploitable par un orchestrateur ou un
workflow au chapitre 03.

## 💡 À retenir

1. Un tool sans schéma est une promesse floue.
1. Une bonne description guide le modèle mieux qu'un long prompt.
1. La validation n'est pas un détail d'implémentation : c'est l'interface de sécurité.
