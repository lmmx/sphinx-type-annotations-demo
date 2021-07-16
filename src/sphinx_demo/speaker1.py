from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    #from sphinx_demo import Greeting1
    from sphinx_demo import greeting1

from .bases import BaseSpeaker

__all__ = ["Speaker1"]


class Speaker1(BaseSpeaker):
    def set_new_greeting(
        self,
        greeting: greeting1.Greeting1
        #greeting: Greeting1
    ) -> None:
        self.greeting = greeting
