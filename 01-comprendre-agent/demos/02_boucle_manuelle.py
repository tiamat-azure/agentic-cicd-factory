"""DEMO 2 - La boucle jouée à la main.

    python demos/02_boucle_manuelle.py

Ici le modèle a des tools, mais **c'est toi qui joues la boucle** : à chaque tour,
le script s'arrête et te demande d'appuyer sur Entrée pour exécuter l'action
demandée, puis pour réinjecter l'observation.

But : sentir physiquement les 3 temps, et voir qu'un agent n'est rien d'autre que
ce script avec `input()` remplacé par `while True`.

Expérience obligatoire (option `--sans-observation`) :

    python demos/02_boucle_manuelle.py --sans-observation

On n'ajoute PAS le résultat du tool à l'historique. Observe le ping-pong :
le modèle redemande indéfiniment la même action. C'est l'erreur n°1 des débutants.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent / "03_agent_minimal"))
from model import get_client  # noqa: E402
from tools import TOOL_SPECS, executer  # noqa: E402

SYSTEM = (
    "Tu es un agent d'analyse de dépôt. Découvre la structure, lis les fichiers "
    "pertinents, puis vérifie tes hypothèses en exécutant les tests."
)
OBJECTIF = "Trouve pourquoi la suite de tests de ce dépôt échoue."

MAX_TOURS = 6


def main() -> None:
    load_dotenv()
    sans_observation = "--sans-observation" in sys.argv
    client = get_client()

    messages: list[dict] = [{"role": "user", "content": OBJECTIF}]

    for tour in range(1, MAX_TOURS + 1):
        print(f"\n{'=' * 70}\nTOUR {tour}")

        input("  [Entrée] -> THINK : envoyer l'historique au modèle...")
        reponse = client.complete(system=SYSTEM, messages=messages, tools=TOOL_SPECS)
        messages.append(
            {"role": "assistant", "content": reponse.text, "tool_calls": reponse.tool_calls}
        )

        if reponse.text:
            print(f"  think    : {reponse.text.strip()[:400]}")

        if reponse.is_final:
            print("\n  Le modèle n'appelle plus de tool -> TERMINAISON naturelle.")
            print(f"\nRéponse finale :\n{reponse.text}")
            return

        for appel in reponse.tool_calls:
            print(f"  décision : {appel.name}({json.dumps(appel.arguments, ensure_ascii=False)})")
            input("  [Entrée] -> ACT : exécuter l'action (c'est TON code qui exécute)...")
            observation = executer(appel.name, appel.arguments)
            print(f"  résultat : {observation.strip()[:300]}")

            if sans_observation:
                print("  /!\\ OBSERVE volontairement omis - le modèle ne saura rien du résultat.")
                continue

            input("  [Entrée] -> OBSERVE : réinjecter le résultat dans l'historique...")
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": appel.id,
                    "name": appel.name,
                    "content": observation,
                }
            )

    print(f"\nMax {MAX_TOURS} tours atteint sans terminaison -> c'est un garde-fou, pas un succès.")


if __name__ == "__main__":
    main()
