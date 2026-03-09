from app.agent.base import AgentState, BaseAgent
from app.prompt.explorer_prompt import EXPLORER_PROMPT
from app.tool.local_rag_memory import LocalRAGMemory


class ExplorerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="explorer", system_prompt=EXPLORER_PROMPT)
        self.memory = LocalRAGMemory()

    def observe(self, frame_summaries: list[str], state: AgentState) -> dict:
        merged = "；".join(frame_summaries)
        event_text = f"检测到事件：{merged}"
        memory_result = self.memory.upsert_event(event_text)
        llm_result = self.run(state, {"frames": frame_summaries})
        return {"event": event_text, "memory": memory_result, "llm": llm_result}
