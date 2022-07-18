from __future__ import annotations

# technically 3.10 only, but 3.9 doesn't "see" it


def average(test_scores: tuple[float, ...]) -> float:
    return sum(list(test_scores)) / len(test_scores) if len(test_scores) else 0
