"""本地 RAG 记忆工具：简化版 JSON + 向量占位。"""

from __future__ import annotations

import json
from pathlib import Path


class LocalRAGMemory:
    def __init__(self, taxonomy_path: str = "AutoVideoMiner/data/events_taxonomy.json") -> None:
        self.taxonomy_path = Path(taxonomy_path)
        self.taxonomy_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.taxonomy_path.exists():
            self.taxonomy_path.write_text("[]", encoding="utf-8")

    def upsert_event(self, event_text: str) -> dict:
        events = json.loads(self.taxonomy_path.read_text(encoding="utf-8"))
        for row in events:
            if event_text in row["event"] or row["event"] in event_text:
                row["weight"] += 1
                self.taxonomy_path.write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")
                return {"action": "merged", "event": row}
        new_row = {"event": event_text, "weight": 1, "sources": []}
        events.append(new_row)
        self.taxonomy_path.write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")
        return {"action": "inserted", "event": new_row}
