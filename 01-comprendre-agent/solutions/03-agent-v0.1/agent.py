"""Solution - exercice 3 : Agent v0.1 gouvernable.

Différences avec `demos/03_agent_minimal/agent.py` :
  a. tool `terminer` -> terminaison EXPLICITE avec statut machine-lisible
  b. budget en tokens en plus du budget en itérations
  c. neutralisation du ping-pong
  d. journal `run.json` -> premier artefact d'observabilité

Copie ce fichier par-dessus l'agent de la demo, avec `state.py` de ce dossier.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from model import ModelClient, get_client
from state import AgentState
from tools import TOOL_SPECS, executer

SYSTEM_PROMPT = """\
Tu es un agent d'analyse de dépôt logiciel, composant de la Agentic CI/CD Factory.

Ta méthode :
1. Découvre la structure du dépôt avant toute chose.
2. Localise avant de lire ; ne devine jamais le contenu d'un fichier.
3. Vérifie tes hypothèses par les faits (exécute les tests).
4. Appelle le tool `terminer` dès que l'objectif est atteint, ou dès que tu es certain
   de ne pas pouvoir l'atteindre. Ne termine jamais autrement.

Contraintes :
- Si un outil renvoie une erreur, corrige ton appel ; ne le répète pas à l'identique.
- Sois concis. Ne conclus rien que tu n'aies vérifié.
"""

TERMINER_SPEC = {
    "name": "terminer",
    "description": (
        "Déclare la fin de la tâche. À appeler dès que l'objectif est atteint ou que tu "
        "es certain de ne pas pouvoir l'atteindre. N'appelle aucun autre outil après."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "statut": {"type": "string", "enum": ["succes", "echec"]},
            "resume": {"type": "string", "description": "Conclusion en 3 lignes maximum."},
            "confiance": {"type": "number", "description": "Entre 0 et 1."},
        },
        "required": ["statut", "resume", "confiance"],
    },
}

SPECS = TOOL_SPECS + [TERMINER_SPEC]


class Agent:
    def __init__(
        self,
        client: ModelClient | None = None,
        max_iterations: int = 8,
        max_tokens_total: int = 100_000,
        verbose: bool = True,
    ):
        self.client = client or get_client()
        self.max_iterations = max_iterations
        self.max_tokens_total = max_tokens_total
        self.verbose = verbose

    # ------------------------------------------------------------------ #

    def run(self, objectif: str, journal: str | Path = "run.json") -> AgentState:
        state = AgentState(
            objectif=objectif,
            max_iterations=self.max_iterations,
            max_tokens_total=self.max_tokens_total,
        )
        state.ajouter_utilisateur(objectif)

        while not state.termine:
            # (b) garde-fous durs, évalués AVANT tout appel payant
            if state.budget_epuise():
                self._arreter(state, "budget_epuise", f"Budget épuisé ({state.resume_couts()}).")
                break

            state.iteration += 1
            self._log(f"\n─── itération {state.iteration}/{state.max_iterations} ───")

            # ------------------------------------------------------- THINK
            reponse = self.client.complete(system=SYSTEM_PROMPT, messages=state.messages, tools=SPECS)
            state.tokens_in += reponse.usage.get("input_tokens", 0)
            state.tokens_out += reponse.usage.get("output_tokens", 0)
            state.ajouter_assistant(reponse.text, reponse.tool_calls)
            if reponse.text:
                self._log(f"[think] {reponse.text.strip()[:400]}")

            # Filet de sécurité : le modèle a oublié `terminer`.
            if reponse.is_final:
                self._arreter(state, "succes_implicite", reponse.text)
                break

            for appel in reponse.tool_calls:
                # (a) terminaison explicite
                if appel.name == "terminer":
                    args = appel.arguments
                    state.confiance = args.get("confiance")
                    self._arreter(state, args.get("statut", "succes"), args.get("resume", ""))
                    state.journaliser_action(appel.name, appel.arguments)
                    break

                # (c) anti ping-pong : on ne ré-exécute pas, on informe le modèle
                if state.action_repetee(appel.name, appel.arguments):
                    self._log(f"[!] ping-pong neutralisé sur {appel.name}")
                    observation = (
                        "Tu viens d'exécuter cette action à l'identique. "
                        "Le résultat est inchangé :\n"
                        f"{state.derniere_observation(appel.name)}\n"
                        "Change d'approche ou appelle `terminer`."
                    )
                else:
                    self._log(f"[act] {appel.name}({json.dumps(appel.arguments, ensure_ascii=False)})")
                    observation = executer(appel.name, appel.arguments)  # ACT
                    state.memoriser_observation(appel.name, observation)

                self._log(f"[observe] {observation.strip()[:300]}")
                state.journaliser_action(appel.name, appel.arguments)
                state.ajouter_observation(appel.id, appel.name, observation)  # OBSERVE

        self._log(f"\n=== statut={state.statut} | {state.resume_couts()} ===")
        self._ecrire_journal(state, Path(journal))  # (d)
        return state

    # ------------------------------------------------------------------ #

    @staticmethod
    def _arreter(state: AgentState, statut: str, resultat: str) -> None:
        state.termine = True
        state.statut = statut
        state.resultat = resultat

    def _ecrire_journal(self, state: AgentState, chemin: Path) -> None:
        chemin.write_text(
            json.dumps(
                {
                    "horodatage": datetime.now(timezone.utc).isoformat(),
                    "objectif": state.objectif,
                    "statut": state.statut,
                    "confiance": state.confiance,
                    "iterations": state.iteration,
                    "tokens": {"in": state.tokens_in, "out": state.tokens_out},
                    "actions": state.journal,
                    "resultat": state.resultat,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        self._log(f"journal écrit : {chemin}")

    def _log(self, message: str) -> None:
        if self.verbose:
            print(message)
