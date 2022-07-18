from __future__ import annotations


# lists
def foo(messages):
    """untyped function"""
    for message in messages:
        print(message)


def foo_typed(messages: list[str]) -> None:
    """typed function"""
    for message in messages:
        print(message)
