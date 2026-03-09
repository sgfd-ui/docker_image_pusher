class DedupTool:
    def __init__(self) -> None:
        self._seen: set[str] = set()

    def exists(self, key: str) -> bool:
        return key in self._seen

    def mark(self, key: str) -> None:
        self._seen.add(key)
