import base64


class FrameExtractTool:
    def extract(self, video_path: str, ts: float) -> str:
        payload = f"{video_path}@{ts}".encode("utf-8")
        return base64.b64encode(payload).decode("utf-8")
