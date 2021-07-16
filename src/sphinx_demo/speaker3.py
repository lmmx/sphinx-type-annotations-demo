from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import sphinx_demo

from .bases import BaseSpeaker

__all__ = ["Speaker3"]


class Speaker3(BaseSpeaker):
    def set_new_greeting(
        self,
        greeting: sphinx_demo.greeting3.Greeting3
    ) -> None:
        self.greeting = greeting
