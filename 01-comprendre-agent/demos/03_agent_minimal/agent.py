"""Agent v0.1 - la boucle Think / Act / Observe, sans aucun framework.

Tout le chapitre 01 tient dans `Agent.run()`. Lis-la en premier.
"""

from __future__ import annotations

import json

from model import ModelClient, get_client
from state import AgentState
from tools import TOOL_SPECS, executer

SYSTEM_PROMPT = """\
Tu es un agent d'analyse de dépôt logiciel, composant de la Agentic CI/CD Factory.

Ta méthode :
1. Découvre la structure du dépôt avant toute chose.
2. Lis les fichiers pertinents. Ne devine jamais leur contenu.
3. Vérifie tes hypothèses par les faits (exécute les tests).
4. Quand tu as la réponse, énonce-la clairement, sans appeler d'autre outil.

Contraintes :
- Un seul objectif à la fois, celui de l'utilisateur.
- Si un outil renvoie une erreur, corrige ton appel, ne le répète pas à l'identique.
- Sois concis. Ne rends pas de conclusion que tu n'as pas vérifiée.
"""


class Agent:
    def __init__(self, client: ModelClient | None = None, max_iterations: int = 8, verbose: bool = True):
        self.client = client or get_client()
        self.max_iterations = max_iterations
        self.verbose = verbose

    # ----------------------------------------------------------------- #

    def run(self, objectif: str) -> AgentState:
        state = AgentState(objectif=objectif, max_iterations=self.max_iterations)
        state.ajouter_utilisateur(objectif)

        while not state.termine:
            # --- garde-fou dur : la boucle doit pouvoir s'arrêter sans le modèle
            if state.budget_epuise():
                state.termine = True
                state.statut = "budget_epuise"
                state.resultat = f"Budget de {state.max_iterations} itérations épuisé."
                break

            state.iteration += 1
            self._log(f"\n─── itération {state.iteration}/{state.max_iterations} ───")

            # ---------------------------------------------------------- THINK
            reponse = self.client.complete(
                system=SYSTEM_PROMPT, messages=state.messages, tools=TOOL_SPECS
            )
            state.tokens_in += reponse.usage.get("input_tokens", 0)
            state.tokens_out += reponse.usage.get("output_tokens", 0)
            state.ajouter_assistant(reponse.text, reponse.tool_calls)

            if reponse.text:
                self._log(f"[think] {reponse.text.strip()[:400]}")

            # --------------------------------------- TERMINAISON (naturelle)
            if reponse.is_final:
                state.termine = True
                state.statut = "succes"
                state.resultat = reponse.text
                break

            # ------------------------------------------------- ACT + OBSERVE
            for appel in reponse.tool_calls:
                if state.action_repetee(appel.name, appel.arguments):
                    self._log(f"[!] ping-pong détecté sur {appel.name}")
                state.historique_actions.append((appel.name, appel.arguments))

                self._log(f"[act] {appel.name}({json.dumps(appel.arguments, ensure_ascii=False)})")
                observation = executer(appel.name, appel.arguments)  # ACT
                self._log(f"[observe] {observation.strip()[:300]}")
                state.ajouter_observation(appel.id, appel.name, observation)  # OBSERVE

        self._log(f"\n=== fin : statut={state.statut} | {state.resume_couts()} ===")
        return state

    # ----------------------------------------------------------------- #

    def _log(self, message: str) -> None:
        if self.verbose:
            print(message)
