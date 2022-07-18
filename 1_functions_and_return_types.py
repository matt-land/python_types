import time


# functions
def foo(seconds, message):
    """untyped example"""
    time.sleep(seconds)
    print(message)


def foo_typed(seconds: int, message: str) -> None:
    """typed example"""
    time.sleep(seconds)
    print(message)
