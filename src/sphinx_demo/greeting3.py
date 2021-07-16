from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx_demo import speaker3

__all__ = ["Greeting3"]


class Greeting3:
    def __init__(self, speaker: speaker3.Speaker3, message: str = "Hello "):
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
