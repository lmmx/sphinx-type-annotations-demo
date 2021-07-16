from __future__ import annotations

__all__ = ["BaseSpeaker"]


class BaseSpeaker:
    """
    Subclassed to add a new greeting (by overriding the :meth:`greet` method),
    which by default just returns "...".

    Declares a class variable :attr:`target` as "world".

    Args:
      name : The speaker's name, to be reported in a greeting
    """

    target = "world"

    def __init__(self, name: str = "Testing"):
        self.name = name

    def greet(self) -> str:
        return "..."
