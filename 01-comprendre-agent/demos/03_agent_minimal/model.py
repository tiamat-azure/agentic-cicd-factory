"""Abstraction de modèle - l'embryon du Model Gateway du chapitre 05.

Principe model-agnostic : le reste du code ne connaît QUE `ModelClient`,
`ModelResponse` et `ToolCall`. Aucun `if provider == ...` ne doit exister
ailleurs que dans ce fichier.

Format de message neutre utilisé partout dans la formation :

    {"role": "user"      , "content": "texte"}
    {"role": "assistant" , "content": "texte", "tool_calls": [ToolCall, ...]}
    {"role": "tool"      , "tool_call_id": "...", "name": "...", "content": "texte"}
"""

from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass, field
from typing import Any, Protocol

import requests

# --------------------------------------------------------------------------- #
# Types neutres
# --------------------------------------------------------------------------- #


@dataclass
class ToolCall:
    """Une intention d'action émise par le modèle. Le modèle n'exécute rien."""

    id: str
    name: str
    arguments: dict[str, Any]


@dataclass
class ModelResponse:
    text: str = ""
    tool_calls: list[ToolCall] = field(default_factory=list)
    usage: dict[str, int] = field(default_factory=dict)

    @property
    def is_final(self) -> bool:
        """Terminaison naturelle : le modèle ne demande plus rien."""
        return not self.tool_calls


class ModelClient(Protocol):
    """Le seul contrat que l'agent connaît."""

    def complete(
        self,
        system: str,
        messages: list[dict],
        tools: list[dict] | None = None,
    ) -> ModelResponse: ...


# --------------------------------------------------------------------------- #
# Adaptateur Anthropic
# --------------------------------------------------------------------------- #


class AnthropicClient:
    def __init__(self, model: str | None = None, api_key: str | None = None):
        self.model = model or os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
        self.api_key = api_key or os.environ["ANTHROPIC_API_KEY"]
        self.url = "https://api.anthropic.com/v1/messages"

    def complete(self, system, messages, tools=None) -> ModelResponse:
        payload: dict[str, Any] = {
            "model": self.model,
            "max_tokens": 2048,
            "system": system,
            "messages": [self._to_anthropic(m) for m in messages],
        }
        if tools:
            payload["tools"] = [
                {
                    "name": t["name"],
                    "description": t["description"],
                    "input_schema": t["parameters"],
                }
                for t in tools
            ]

        r = requests.post(
            self.url,
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json=payload,
            timeout=120,
        )
        r.raise_for_status()
        data = r.json()

        text, calls = "", []
        for block in data.get("content", []):
            if block["type"] == "text":
                text += block["text"]
            elif block["type"] == "tool_use":
                calls.append(ToolCall(block["id"], block["name"], block["input"]))

        u = data.get("usage", {})
        return ModelResponse(
            text=text,
            tool_calls=calls,
            usage={
                "input_tokens": u.get("input_tokens", 0),
                "output_tokens": u.get("output_tokens", 0),
            },
        )

    @staticmethod
    def _to_anthropic(msg: dict) -> dict:
        if msg["role"] == "tool":
            return {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": msg["tool_call_id"],
                        "content": msg["content"],
                    }
                ],
            }
        if msg["role"] == "assistant" and msg.get("tool_calls"):
            blocks: list[dict] = []
            if msg.get("content"):
                blocks.append({"type": "text", "text": msg["content"]})
            blocks += [
                {"type": "tool_use", "id": c.id, "name": c.name, "input": c.arguments}
                for c in msg["tool_calls"]
            ]
            return {"role": "assistant", "content": blocks}
        return {"role": msg["role"], "content": msg["content"]}


# --------------------------------------------------------------------------- #
# Adaptateur Ollama (local)
# --------------------------------------------------------------------------- #


class OllamaClient:
    def __init__(self, model: str | None = None, base_url: str | None = None):
        self.model = model or os.getenv("OLLAMA_MODEL", "qwen3:14b")
        self.base_url = (base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")).rstrip("/")

    def complete(self, system, messages, tools=None) -> ModelResponse:
        payload: dict[str, Any] = {
            "model": self.model,
            "stream": False,
            "messages": [{"role": "system", "content": system}]
            + [self._to_ollama(m) for m in messages],
        }
        if tools:
            payload["tools"] = [
                {
                    "type": "function",
                    "function": {
                        "name": t["name"],
                        "description": t["description"],
                        "parameters": t["parameters"],
                    },
                }
                for t in tools
            ]

        r = requests.post(f"{self.base_url}/api/chat", json=payload, timeout=300)
        r.raise_for_status()
        data = r.json()
        message = data.get("message", {})

        calls = []
        for c in message.get("tool_calls") or []:
            fn = c["function"]
            args = fn.get("arguments", {})
            if isinstance(args, str):
                args = json.loads(args)
            # Ollama ne fournit pas d'id : on en fabrique un pour garder le contrat.
            calls.append(ToolCall(c.get("id") or f"call_{uuid.uuid4().hex[:8]}", fn["name"], args))

        return ModelResponse(
            text=message.get("content", ""),
            tool_calls=calls,
            usage={
                "input_tokens": data.get("prompt_eval_count", 0),
                "output_tokens": data.get("eval_count", 0),
            },
        )

    @staticmethod
    def _to_ollama(msg: dict) -> dict:
        if msg["role"] == "tool":
            return {"role": "tool", "content": msg["content"], "tool_name": msg["name"]}
        if msg["role"] == "assistant" and msg.get("tool_calls"):
            return {
                "role": "assistant",
                "content": msg.get("content", ""),
                "tool_calls": [
                    {"function": {"name": c.name, "arguments": c.arguments}}
                    for c in msg["tool_calls"]
                ],
            }
        return {"role": msg["role"], "content": msg["content"]}


# --------------------------------------------------------------------------- #
# Fabrique - le SEUL endroit du code où le nom d'un fournisseur apparaît
# --------------------------------------------------------------------------- #

_PROVIDERS = {"anthropic": AnthropicClient, "ollama": OllamaClient}


def get_client(provider: str | None = None) -> ModelClient:
    name = (provider or os.getenv("LLM_PROVIDER", "anthropic")).lower()
    if name not in _PROVIDERS:
        raise ValueError(f"Fournisseur inconnu : {name!r}. Attendu : {list(_PROVIDERS)}")
    return _PROVIDERS[name]()
