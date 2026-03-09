"""Streamlit 前端占位：任务下发、日志流和 HITL。"""


def render_layout() -> dict:
    return {
        "title": "AutoVideoMiner 控制台",
        "panels": ["任务下发", "实时日志", "AskHuman 弹窗"],
    }
