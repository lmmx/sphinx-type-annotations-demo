from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx_demo import Greeting4

from .bases import BaseSpeaker

__all__ = ["Speaker4"]


class Speaker4(BaseSpeaker):
    def set_new_greeting(self, greeting: Greeting4) -> None:
        self.greeting = greeting
