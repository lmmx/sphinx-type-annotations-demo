from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import sphinx_demo

print(f"{TYPE_CHECKING=}")

__all__ = ["Speaker"]


class Speaker:
    def __init__(self, name: str = "Testing"):
        self.target = "world"
        self.name = name

    def greet(self) -> str:
        return self.greeting.greet() if hasattr(self, "greeting") else "..."

    def set_new_greeting(self, greeting: sphinx_demo.greeting.Greeting) -> None:
        self.greeting = greeting
