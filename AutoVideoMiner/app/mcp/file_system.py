from pathlib import Path


class MCPFileSystemClient:
    def __init__(self, root: str = "AutoVideoMiner/data/archive") -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def store_video(self, source_path: str, level: str, event_name: str) -> str:
        target_dir = self.root / level / event_name
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / Path(source_path).name
        Path(source_path).replace(target_path)
        return str(target_path)
