from __future__ import annotations

try:
    from typing import TypeAlias  # > 3.10
except ImportError:
    from typing_extensions import TypeAlias


def transpose_accounts(accounts_by_name: dict[str, str]) -> dict[str, str]:
    """typed example"""
    return dict((value, key) for key, value in accounts_by_name.items())


AccountId: TypeAlias = str
Name: TypeAlias = str


def transpose_accounts2(
    accounts_by_name: dict[Name, AccountId]
) -> dict[AccountId, Name]:
    """typed example with aliases"""
    return dict((value, key) for key, value in accounts_by_name.items())


AccountsByName: TypeAlias = dict[Name, AccountId]
AccountsById: TypeAlias = dict[AccountId, Name]


def transpose_accounts3(accounts_by_name: AccountsByName) -> AccountsById:
    """typed example with aliases"""
    return dict((value, key) for key, value in accounts_by_name.items())
