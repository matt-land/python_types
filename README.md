# Python Types

This is a revisit of Python's type system, as it become more modern in recent Python versions.

Intended as a guide for 3.9 & 3.10, but should work for 3.7+

## Why Type:
- Legible to Humans
- Find errors via static analysis
- Future versions of Python will make your code run faster

Where types matter:
- People reading your code: yes
- Code quality tools like mypy: yes
- Python execution time: no

## Recommendations:

### Python 3.10 (October 2021)
- no special steps, typed as in the examples

### Python < 3.10 (October 2020)
- use "from __future__ import annotations"
- Union & Optional instead of X | Y (type or)
- install typing_extensions when using TypeAlias

```python
from __future__ import annotations
try:
    from typing import TypeAlias  # >= 3.10
except ImportError:
    from typing_extensions import TypeAlias



    
    
    

```
