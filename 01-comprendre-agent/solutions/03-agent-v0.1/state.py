"""Solution - exercice 3 : state enrichi (budget tokens, journal, anti ping-pong)."""

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
    max_tokens_total: int = 100_000
    termine: bool = False
    statut: str | None = None
    resultat: str | None = None
    confiance: float | None = None

    historique_actions: list[tuple[str, dict[str, Any]]] = field(default_factory=list)
    dernieres_observations: dict[str, str] = field(default_factory=dict)
    journal: list[dict] = field(default_factory=list)

    # --- contexte ---------------------------------------------------------- #

    def ajouter_utilisateur(self, contenu: str) -> None:
        self.messages.append({"role": "user", "content": contenu})

    def ajouter_assistant(self, contenu: str, tool_calls: list | None = None) -> None:
        self.messages.append({"role": "assistant", "content": contenu, "tool_calls": tool_calls or []})

    def ajouter_observation(self, tool_call_id: str, nom: str, contenu: str) -> None:
        self.messages.append(
            {"role": "tool", "tool_call_id": tool_call_id, "name": nom, "content": contenu}
        )

    # --- garde-fous -------------------------------------------------------- #

    def budget_epuise(self) -> bool:
        return self.iteration >= self.max_iterations or self.budget_tokens_epuise()

    def budget_tokens_epuise(self) -> bool:
        return (self.tokens_in + self.tokens_out) >= self.max_tokens_total

    def action_repetee(self, nom: str, args: dict) -> bool:
        return bool(self.historique_actions) and self.historique_actions[-1] == (nom, args)

    # --- mémoire runtime ---------------------------------------------------- #

    def memoriser_observation(self, nom: str, contenu: str) -> None:
        self.dernieres_observations[nom] = contenu

    def derniere_observation(self, nom: str) -> str:
        return self.dernieres_observations.get(nom, "(aucune)")

    def journaliser_action(self, nom: str, args: dict) -> None:
        self.historique_actions.append((nom, args))
        self.journal.append({"tour": self.iteration, "tool": nom, "args": args})

    def resume_couts(self) -> str:
        return (
            f"{self.iteration} itération(s), "
            f"{self.tokens_in} tokens in / {self.tokens_out} tokens out"
        )
