from pathlib import Path

from app.agent.base import AgentState, BaseAgent
from app.mcp.file_system import MCPFileSystemClient


class ArchivistAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="archivist", system_prompt="你负责终局分类归档")
        self.fs = MCPFileSystemClient()

    def archive(self, clips: list[str], state: AgentState) -> list[str]:
        self.run(state, {"clips": clips})
        out_paths: list[str] = []
        for clip in clips:
            category = "威胁行为" if "threat" in Path(clip).name else "普通行为"
            out_paths.append(self.fs.store_video(clip, category, "待复核事件"))
        return out_paths
