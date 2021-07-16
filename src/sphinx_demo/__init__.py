r"""
:mod:`sphinx_demo` provides four classes :class:`Speaker1`,
:class:`Speaker2`, :class:`Speaker3`, and :class:`Speaker4`
with a method, ``greet``, which creates an instance of the class
:class:`Greeting`. This instance retains a reference to the 'parent'
instance of :class:`Foo`, creating a circular import which makes
type checking a little more difficult when building Sphinx with the
``sphinx-autodoc-typehints`` extension.
"""

from sphinx_demo.greeting4 import Greeting4  # top-level 'exposed' class Greeting1

from . import greeting1, greeting2, greeting3, speaker1, speaker2, speaker3, speaker4

__all__ = [
    "speaker1",
    "greeting1",
    "speaker2",
    "greeting2",
    "speaker3",
    "greeting3",
    "speaker4",
    "greeting4",  # note: this module was added to the namespace by importing Greeting4
    # "Greeting4", # note: exposing this class in __all__ will break the Sphinx build!
]
