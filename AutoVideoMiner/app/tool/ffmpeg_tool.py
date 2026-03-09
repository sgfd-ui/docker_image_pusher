from pathlib import Path


class FFmpegTool:
    def detect_scene_changes(self, video_path: str) -> list[float]:
        return [5.0, 12.5, 21.3]

    def split(self, video_path: str, timestamps: list[float]) -> list[str]:
        src = Path(video_path)
        segments: list[str] = []
        for idx, _ in enumerate(timestamps, start=1):
            seg = src.with_name(f"{src.stem}_seg_{idx}.mp4")
            seg.write_bytes(b"segment")
            segments.append(str(seg))
        return segments

    def concat(self, files: list[str], out_file: str) -> str:
        Path(out_file).write_bytes(b"concat")
        return out_file
