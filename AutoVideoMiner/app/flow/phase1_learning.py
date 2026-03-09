"""阶段一：Explore & Learn DAG 骨架。"""


def build_phase1_flow() -> dict:
    return {
        "name": "phase1_learning",
        "nodes": ["crawler", "explorer", "local_rag_memory", "analyzer", "archivist"],
        "edges": [
            ("crawler", "explorer"),
            ("explorer", "local_rag_memory"),
            ("explorer", "analyzer"),
            ("analyzer", "archivist"),
        ],
    }
