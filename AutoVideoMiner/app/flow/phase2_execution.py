"""阶段二：Target & Execute DAG 骨架，包含反馈闭环。"""


def build_phase2_flow() -> dict:
    return {
        "name": "phase2_execution",
        "nodes": ["planner", "crawler", "evaluator", "analyzer", "archivist"],
        "edges": [
            ("planner", "crawler"),
            ("crawler", "evaluator"),
            ("evaluator", "planner", "if score < 80"),
            ("evaluator", "analyzer", "if score >= 80"),
            ("analyzer", "archivist"),
        ],
    }
