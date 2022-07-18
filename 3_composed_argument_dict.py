from __future__ import annotations


def foo(items):
    """untyped"""
    results = {}
    running_total = 0
    for key, value in items.items():
        running_total += value
        results[key] = running_total
    return results


def foo_typed(items: dict[str, int]) -> dict[str, int]:
    """typed"""
    results: dict[str, int] = {}
    running_total = 0
    for key, value in items.items():
        running_total += value
        results[key] = running_total
    return results
