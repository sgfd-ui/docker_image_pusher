from app.agent.base import AgentState, BaseAgent
from app.prompt.planner_prompt import PLANNER_PROMPT


class PlannerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="planner", system_prompt=PLANNER_PROMPT)

    def make_plan(self, event: str, state: AgentState, feedback: str = "") -> dict:
        payload = {"event": event, "feedback": feedback}
        self.run(state, payload)
        keywords = [event, f"{event} 监控", f"{event} cctv"]
        return {
            "event": event,
            "keywords": keywords,
            "urls": [
                f"https://www.youtube.com/results?search_query={event}",
                f"https://search.bilibili.com/all?keyword={event}",
            ],
        }
