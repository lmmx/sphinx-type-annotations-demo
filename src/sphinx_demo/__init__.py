r"""
:mod:`sphinx_demo` provides a single class :class:`Speaker`,
with a method, ``greet``, which creates an instance of the class
:class:`Greeting`. This instance retains a reference to the 'parent'
instance of :class:`Speaker`, creating a circular import which makes
type checking a little more difficult when building Sphinx with the
``sphinx-autodoc-typehints`` extension.
"""

from . import greeting, speaker

__all__ = ["speaker", "greeting"]
