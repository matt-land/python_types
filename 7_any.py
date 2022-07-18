from datetime import datetime
from typing import Any
import random

_data = [datetime.utcnow(), 103.1, False, 14, "Hot Dog"]


def get_something() -> Any:
    """Any is an escape system, best to avoid entirely"""
    return random.choice(_data)
