"""Solution - exercice 2 : tool `chercher_dans_fichiers`.

À fusionner dans `tools.py` : la fonction, une entrée dans TOOL_SPECS, une dans REGISTRE.
"""

from __future__ import annotations

MAX_RESULTATS = 50


def chercher_dans_fichiers(motif: str, extension: str = ".py") -> str:
    """Recherche littérale, ligne par ligne, dans le bac à sable.

    Pourquoi tronquer à MAX_RESULTATS : la sortie d'un tool entre intégralement dans la
    fenêtre de contexte, à chaque tour de boucle suivant. Un tool qui renvoie 2000 lignes
    sature le contexte, fait exploser le coût, et noie l'objectif -> pathologie de dérive
    (voir slides/03). Un tool doit toujours borner sa sortie.
    """
    from tools import SANDBOX, _tronquer  # noqa: PLC0415

    resultats: list[str] = []
    tronque = False

    for fichier in sorted(SANDBOX.rglob(f"*{extension}")):
        try:
            lignes = fichier.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for numero, ligne in enumerate(lignes, start=1):
            if motif in ligne:
                if len(resultats) >= MAX_RESULTATS:
                    tronque = True
                    break
                chemin = fichier.relative_to(SANDBOX).as_posix()
                resultats.append(f"{chemin}:{numero}: {ligne.strip()}")
        if tronque:
            break

    if not resultats:
        return f"Aucune occurrence de {motif!r} dans les fichiers {extension}."

    entete = f"{len(resultats)} occurrence(s)" + (" (tronqué)" if tronque else "")
    return _tronquer(entete + "\n" + "\n".join(resultats))


# --------------------------------------------------------------------------- #
# Spec à ajouter dans TOOL_SPECS
# --------------------------------------------------------------------------- #

SPEC = {
    "name": "chercher_dans_fichiers",
    "description": (
        "Recherche une chaîne de caractères dans tous les fichiers du dépôt et renvoie "
        "les lignes correspondantes avec leur chemin et leur numéro de ligne. "
        "Utilise-le AVANT `lire_fichier` pour localiser un symbole, une constante ou un "
        "message d'erreur : c'est beaucoup moins coûteux que de lire des fichiers entiers."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "motif": {"type": "string", "description": "Chaîne littérale à rechercher."},
            "extension": {
                "type": "string",
                "description": "Extension des fichiers à inspecter, ex. '.py'. Défaut : '.py'.",
            },
        },
        "required": ["motif"],
    },
}

# --------------------------------------------------------------------------- #
# Ce que l'expérience de dégradation doit t'apprendre
# --------------------------------------------------------------------------- #
#
# Avec la description ci-dessus, le modèle cherche puis lit ciblé.
# Avec "Cherche du texte.", il lit des fichiers entiers d'abord, ou n'utilise pas le tool.
#
# Le comportement d'un agent se pilote autant par les DESCRIPTIONS DE TOOLS que par le
# system prompt. Une description doit dire QUOI, QUAND, et POURQUOI plutôt qu'un autre.
# Approfondi au chapitre 02.
