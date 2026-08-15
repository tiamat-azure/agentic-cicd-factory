"""DEMO 1 - Un LLM seul (niveau 0). Constater ce qui manque.

    python demos/01_llm_brut.py

On pose au modèle une question dont la réponse est DANS le dépôt.
Il n'a aucun tool : il ne peut que deviner.

Ce que tu dois observer :
  - le modèle répond quand même, avec assurance ;
  - sa réponse est plausible et invérifiable ;
  - relance : la réponse change. Aucun ancrage dans le réel.

Conclusion : le problème d'un LLM seul n'est pas qu'il raisonne mal,
c'est qu'il n'a **aucun accès au monde**. Un agent, c'est d'abord cet accès.
"""

from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent / "03_agent_minimal"))
from model import get_client  # noqa: E402

QUESTION = (
    "Dans le module Python `facturation.py` d'un dépôt que je ne te montre pas, "
    "la fonction `appliquer_remise(montant, pourcentage)` a un bug. "
    "Quel est ce bug, précisément, et à quelle ligne ?"
)


def main() -> None:
    load_dotenv()
    client = get_client()

    for essai in (1, 2):
        reponse = client.complete(
            system="Tu es un assistant d'analyse de code.",
            messages=[{"role": "user", "content": QUESTION}],
            tools=None,
        )
        print(f"\n───── essai {essai} ─────")
        print(reponse.text.strip())

    print("\n" + "=" * 70)
    print("Deux réponses, aucune vérifiable. Aucun tool = aucun ancrage dans le réel.")
    print("-> demo suivante : 02_boucle_manuelle.py")


if __name__ == "__main__":
    main()
