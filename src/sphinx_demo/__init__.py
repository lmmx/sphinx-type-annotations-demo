r"""
:mod:`sphinx_demo` provides three classes :class:`Speaker1`,
:class:`Speaker2`, and :class:`Speaker3` with a method, ``greet``, which creates an instance of the class
:class:`Greeting`, whose instance retains a reference to the 'parent'
instance of :class:`Foo`.

Type hinting this code creates a circular import, which is deemed
completely legitimate by ``mypy`` but rejected by Sphinx's
``sphinx-autodoc-typehints`` module.
"""

from sphinx_demo.greeting1 import Greeting1  # top-level 'exposed' class Greeting1

from . import greeting1, greeting2, greeting3, speaker1, speaker2, speaker3

__all__ = [
    "speaker1",
    "greeting1",  # note: this module was added to the namespace when importing Greeting1
    "speaker2",
    "greeting2",
    "speaker3",
    "greeting3",
    # "Greeting1",
]
