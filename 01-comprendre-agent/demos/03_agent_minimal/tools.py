"""Les tools de l'Agent v0.1.

Un tool = (nom, description, schéma d'arguments, fonction Python).
La *description* est le vrai prompt du tool : c'est tout ce que le modèle voit
pour décider de l'utiliser.

Périmètre volontairement restreint : lecture seule, dans un bac à sable.
L'écriture arrive au chapitre 02, la gouvernance au chapitre 09.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

# Bac à sable : aucun accès en dehors de ce dossier.
SANDBOX = (Path(__file__).parent / "sandbox").resolve()

MAX_SORTIE = 4000  # caractères - un tool bavard sature la fenêtre de contexte


def _resoudre(chemin: str) -> Path:
    cible = (SANDBOX / chemin).resolve()
    if not cible.is_relative_to(SANDBOX):
        raise ValueError(f"Accès refusé hors du bac à sable : {chemin}")
    return cible


def _tronquer(texte: str) -> str:
    if len(texte) <= MAX_SORTIE:
        return texte
    return texte[:MAX_SORTIE] + f"\n... [tronqué, {len(texte) - MAX_SORTIE} caractères omis]"


# --------------------------------------------------------------------------- #
# Implémentations
# --------------------------------------------------------------------------- #


def lister_fichiers(sous_dossier: str = ".") -> str:
    base = _resoudre(sous_dossier)
    if not base.is_dir():
        return f"Erreur : {sous_dossier} n'est pas un dossier."
    entrees = sorted(p.relative_to(SANDBOX).as_posix() for p in base.rglob("*") if p.is_file())
    return "\n".join(entrees) if entrees else "(aucun fichier)"


def lire_fichier(chemin: str) -> str:
    cible = _resoudre(chemin)
    if not cible.is_file():
        return f"Erreur : fichier introuvable : {chemin}"
    return _tronquer(cible.read_text(encoding="utf-8"))


def executer_tests() -> str:
    """Lance pytest dans le bac à sable et renvoie le verdict brut."""
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=SANDBOX,
        capture_output=True,
        text=True,
        timeout=120,
    )
    return _tronquer(f"code_retour={proc.returncode}\n{proc.stdout}\n{proc.stderr}")


# --------------------------------------------------------------------------- #
# Déclaration : schémas exposés au modèle
# --------------------------------------------------------------------------- #

TOOL_SPECS: list[dict[str, Any]] = [
    {
        "name": "lister_fichiers",
        "description": (
            "Liste récursivement les fichiers du dépôt. "
            "Utilise-le en premier pour découvrir la structure avant de lire quoi que ce soit."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "sous_dossier": {
                    "type": "string",
                    "description": "Sous-dossier relatif à explorer. Par défaut la racine.",
                }
            },
            "required": [],
        },
    },
    {
        "name": "lire_fichier",
        "description": (
            "Lit le contenu texte d'un fichier du dépôt. "
            "Ne devine jamais le contenu d'un fichier : lis-le."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "chemin": {
                    "type": "string",
                    "description": "Chemin du fichier, relatif à la racine du dépôt.",
                }
            },
            "required": ["chemin"],
        },
    },
    {
        "name": "executer_tests",
        "description": (
            "Exécute la suite de tests (pytest) du dépôt et renvoie le code de retour "
            "et la sortie. Utilise-le pour vérifier un diagnostic par les faits."
        ),
        "parameters": {"type": "object", "properties": {}, "required": []},
    },
]

REGISTRE: dict[str, Callable[..., str]] = {
    "lister_fichiers": lister_fichiers,
    "lire_fichier": lire_fichier,
    "executer_tests": executer_tests,
}


def executer(nom: str, arguments: dict[str, Any]) -> str:
    """ACT : c'est le runtime qui exécute, jamais le modèle."""
    if nom not in REGISTRE:
        return f"Erreur : tool inconnu {nom!r}. Tools disponibles : {list(REGISTRE)}"
    try:
        return REGISTRE[nom](**arguments)
    except TypeError as exc:
        return f"Erreur d'arguments pour {nom} : {exc}"
    except Exception as exc:  # renvoyer l'erreur AU MODÈLE plutôt que crasher
        return f"Erreur lors de l'exécution de {nom} : {type(exc).__name__}: {exc}"
