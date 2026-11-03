"""Rendezvous barrier primitive for multi-agent milestone synchronization."""
from typing import Set, Dict, Any, Optional


class BarrierSync:
    def __init__(self, milestone_name: str, expected_agents: Set[str]):
        self.milestone_name = milestone_name
        self.expected_agents: Set[str] = set(expected_agents)
        self._arrived: Dict[str, Any] = {}

    def arrive(self, agent_id: str, payload: Any = None) -> bool:
        """Records agent arrival at milestone. Returns True if all arrived (released)."""
        if agent_id not in self.expected_agents:
            raise ValueError(f"Agent '{agent_id}' is not an expected party for barrier '{self.milestone_name}'")
        self._arrived[agent_id] = payload
        return self.is_released()

    def is_released(self) -> bool:
        return self.expected_agents.issubset(set(self._arrived.keys()))

    def get_manifest(self) -> Optional[Dict[str, Any]]:
        if not self.is_released():
            return None
        return {
            "milestone": self.milestone_name,
            "participants": list(self.expected_agents),
            "payloads": self._arrived
        }

    def reset(self) -> None:
        self._arrived.clear()
