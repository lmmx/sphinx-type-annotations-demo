from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx_demo.greeting2 import Greeting2
    # will also work with just `from sphinx_demo import greeting2`, but mypy rejects it

from .bases import BaseSpeaker

__all__ = ["Speaker2"]


class Speaker2(BaseSpeaker):
    def set_new_greeting(
        self,
        greeting: Greeting2
    ) -> None:
        self.greeting = greeting
