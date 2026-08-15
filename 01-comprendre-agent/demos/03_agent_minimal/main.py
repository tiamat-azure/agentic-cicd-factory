"""Point d'entrée de l'Agent v0.1.

    python main.py "Pourquoi la suite de tests échoue-t-elle ?"
"""

from __future__ import annotations

import sys

from agent import Agent
from dotenv import load_dotenv

OBJECTIF_PAR_DEFAUT = (
    "La suite de tests de ce dépôt échoue. Identifie le fichier et la ligne fautifs, "
    "explique la cause exacte, et propose la correction (sans l'appliquer)."
)


def main() -> None:
    load_dotenv()
    objectif = " ".join(sys.argv[1:]) or OBJECTIF_PAR_DEFAUT

    print(f"Objectif : {objectif}\n")
    state = Agent(max_iterations=8).run(objectif)

    print("\n" + "=" * 70)
    print(state.resultat or "(pas de résultat)")


if __name__ == "__main__":
    main()
