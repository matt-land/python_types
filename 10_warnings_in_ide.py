from __future__ import annotations


def bad_return(points: list[tuple[str, str]]) -> bool:
    """highlights the return as incorrect"""
    for point in points:
        print(point)
    return {"all done": True}


def bad_call(points: list[tuple[str, str]]) -> bool:
    for point in points:
        print(point)
    return True


# highlights the caller as having the wrong arguments
bad_call([(3, 5), (1, 2)])

bad_call([("3", "5"), ("1", "2")])
