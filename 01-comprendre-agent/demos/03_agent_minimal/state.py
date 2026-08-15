"""State de l'agent.

Rappel du principe du chapitre : **contexte ⊂ state**.
`messages` part au modèle. Tout le reste reste côté runtime.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentState:
    objectif: str

    # --- CONTEXTE : envoyé au modèle -------------------------------------- #
    messages: list[dict] = field(default_factory=list)

    # --- RUNTIME : jamais envoyé au modèle -------------------------------- #
    iteration: int = 0
    max_iterations: int = 8
    tokens_in: int = 0
    tokens_out: int = 0
    termine: bool = False
    statut: str | None = None  # "succes" | "echec" | "budget_epuise"
    resultat: str | None = None
    historique_actions: list[tuple[str, dict[str, Any]]] = field(default_factory=list)

    # ---------------------------------------------------------------------- #

    def ajouter_utilisateur(self, contenu: str) -> None:
        self.messages.append({"role": "user", "content": contenu})

    def ajouter_assistant(self, contenu: str, tool_calls: list | None = None) -> None:
        self.messages.append(
            {"role": "assistant", "content": contenu, "tool_calls": tool_calls or []}
        )

    def ajouter_observation(self, tool_call_id: str, nom: str, contenu: str) -> None:
        """OBSERVE : sans cet appel, l'agent boucle sur la même action."""
        self.messages.append(
            {"role": "tool", "tool_call_id": tool_call_id, "name": nom, "content": contenu}
        )

    def budget_epuise(self) -> bool:
        return self.iteration >= self.max_iterations

    def action_repetee(self, nom: str, args: dict) -> bool:
        """Détecteur de ping-pong : même action qu'au tour précédent."""
        return bool(self.historique_actions) and self.historique_actions[-1] == (nom, args)

    def resume_couts(self) -> str:
        return (
            f"{self.iteration} itération(s), "
            f"{self.tokens_in} tokens in / {self.tokens_out} tokens out"
        )
