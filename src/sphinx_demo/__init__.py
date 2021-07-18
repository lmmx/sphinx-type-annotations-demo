r"""
:mod:`sphinx_demo` provides a single class :class:`Speaker`,
with a method, ``set_new_greeting``, which takes an instance of the class
:class:`Greeting` and stores it in the :attr:`greeting` attribute.
This instance retains a reference to the 'parent' instance of
class :class:`Speaker`, creating a circular type reference which breaks
the Sphinx build when using the ``sphinx-autodoc-typehints`` extension.
"""

from . import greeting, speaker

__all__ = ["speaker", "greeting"]
