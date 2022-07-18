from typing import Generator, Iterator


def exponential() -> Generator[int, None, None]:
    """technically correct"""
    start = 1
    while start < 100:
        yield start**start
        start += 1


def exponential2() -> Iterator[int]:
    """simpler interface, preferred"""
    start = 1
    while start < 100:
        yield start**start
        start += 1
