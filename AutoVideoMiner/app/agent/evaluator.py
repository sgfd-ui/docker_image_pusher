from app.agent.base import AgentState, BaseAgent
from app.prompt.evaluator_prompt import EVALUATOR_PROMPT


class EvaluatorAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(name="evaluator", system_prompt=EVALUATOR_PROMPT)

    def evaluate(self, sampled_titles: list[str], state: AgentState) -> dict:
        self.run(state, {"sampled_titles": sampled_titles})
        matches = [t for t in sampled_titles if len(t) > 3]
        score = round((len(matches) / max(1, len(sampled_titles))) * 100, 2)
        return {
            "pass": score >= 80,
            "score": score,
            "advice": "建议加入排除词 -搞笑 -整蛊" if score < 80 else "采样质量合格",
        }
