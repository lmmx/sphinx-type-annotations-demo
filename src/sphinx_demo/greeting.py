from __future__ import annotations

from typing import TYPE_CHECKING

from .config import OVERRIDE_IMPORT_CONDITION

if OVERRIDE_IMPORT_CONDITION or TYPE_CHECKING:
    import sphinx_demo

__all__ = ["Greeting"]


class Greeting:
    def __init__(self, speaker: sphinx_demo.speaker.Speaker, message: str = "Hello "):
        self.speaker = speaker
        self.greeting = message

    def greet(self) -> str:
        return self.greeting + self.target + " I'm " + self.name

    @property
    def target(self) -> str:
        return self.speaker.target

    @property
    def name(self) -> str:
        return self.speaker.name
