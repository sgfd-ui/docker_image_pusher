"""Agent 基类，统一封装模型调用与重试。"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


CHAT_MODEL = "chatgpt"


@dataclass
class AgentState:
    messages: list[dict[str, Any]] = field(default_factory=list)
    retries: int = 0
    token_usage: int = 0


class BaseAgent:
    def __init__(self, name: str, system_prompt: str, model: str = CHAT_MODEL) -> None:
        self.name = name
        self.system_prompt = system_prompt
        self.model = model

    def run(self, state: AgentState, payload: dict[str, Any]) -> dict[str, Any]:
        state.retries += 1
        response = self._call_model(state, payload)
        state.messages.append({"agent": self.name, "response": response})
        return response

    def _call_model(self, state: AgentState, payload: dict[str, Any]) -> dict[str, Any]:
        state.token_usage += len(str(payload))
        return {
            "model": self.model,
            "system_prompt": self.system_prompt,
            "payload": payload,
            "note": "placeholder response",
        }
