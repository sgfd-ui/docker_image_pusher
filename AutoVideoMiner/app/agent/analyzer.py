from app.agent.base import AgentState, BaseAgent
from app.prompt.analyzer_prompt import ANALYZER_PROMPT
from app.tool.ffmpeg_tool import FFmpegTool
from app.tool.frame_extract_tool import FrameExtractTool


class AnalyzerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="analyzer", system_prompt=ANALYZER_PROMPT)
        self.ffmpeg = FFmpegTool()
        self.extractor = FrameExtractTool()

    def split(self, video_path: str, state: AgentState) -> list[str]:
        timestamps = self.ffmpeg.detect_scene_changes(video_path)
        self.run(state, {"video_path": video_path, "timestamps": timestamps})
        segments = self.ffmpeg.split(video_path, timestamps)
        return [seg for seg in segments if self.extractor.extract(seg, 0.1)]
