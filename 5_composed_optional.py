from __future__ import annotations
from typing import Union, Optional


_hello = {"Spanish": "hola", "French": "bonjour", "German": "hallo"}


def translate(language: str) -> Union[str, None]:
    """Python <= 3.9"""
    return _hello.get(language)


def translate2(language: str) -> Optional[str]:
    """Pythonic shortcut of Union"""
    return _hello.get(language)


def translate3(language: str) -> str | None:
    """Python > 3.9, no import needed"""
    return _hello.get(language)
