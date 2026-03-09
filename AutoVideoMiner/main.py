"""AutoVideoMiner 启动入口。"""

from app.flow.phase1_learning import build_phase1_flow
from app.flow.phase2_execution import build_phase2_flow


def main() -> None:
    phase1 = build_phase1_flow()
    phase2 = build_phase2_flow()
    print("AutoVideoMiner initialized")
    print(f"Phase1 nodes: {phase1['nodes']}")
    print(f"Phase2 nodes: {phase2['nodes']}")


if __name__ == "__main__":
    main()
