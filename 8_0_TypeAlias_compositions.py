from __future__ import annotations
from typing import TypeAlias  # > 3.10


def t(accounts_by_name: dict[str, str]) -> dict[str, str]:
    return dict((value, key) for key, value in accounts_by_name.items())


AccountId: TypeAlias = str
Name: TypeAlias = str


def t1(accounts_by_name: dict[Name, AccountId]) -> dict[AccountId, Name]:
    return dict((value, key) for key, value in accounts_by_name.items())
