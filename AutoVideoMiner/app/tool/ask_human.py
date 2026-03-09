class AskHumanInterrupt(Exception):
    pass


def ask_human(context: dict) -> None:
    raise AskHumanInterrupt(f"需要人工接管: {context}")
