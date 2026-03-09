from pathlib import Path


class YtDlpTool:
    def __init__(self, workspace_dir: str = "AutoVideoMiner/data/workspace") -> None:
        self.workspace = Path(workspace_dir)
        self.workspace.mkdir(parents=True, exist_ok=True)

    def download(self, url: str) -> str:
        safe_name = url.replace("https://", "").replace("/", "_")[:80]
        out_file = self.workspace / f"{safe_name}.mp4"
        out_file.write_bytes(b"placeholder video content")
        return str(out_file)
