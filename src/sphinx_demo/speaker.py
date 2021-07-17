from __future__ import annotations

from typing import TYPE_CHECKING

from .bases import BaseSpeaker
from .config import OVERRIDE_IMPORT_CONDITION

if OVERRIDE_IMPORT_CONDITION or TYPE_CHECKING:
    import sphinx_demo

__all__ = ["Speaker"]


class Speaker(BaseSpeaker):
    def set_new_greeting(self, greeting: sphinx_demo.greeting.Greeting) -> None:
        self.greeting = greeting
