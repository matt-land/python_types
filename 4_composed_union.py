from __future__ import annotations
from typing import Union


_data = {
    "schema": "customer",
    "version": 1.01,
}


def lookup(prop: str) -> Union[str, float, None]:
    """Python <= 3.9"""
    return _data.get(prop)


def lookup2(prop: str) -> str | float | None:
    """Python > 3.9, no import needed"""
    return _data.get(prop)
