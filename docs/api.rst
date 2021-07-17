=============
API Reference
=============

Demo classes: :class:`Speaker` and :class:`Greeting`
====================================================

This package contains minimal examples to demonstrate how Sphinx does and doesn't allow you to
handle circular imports in type hints, and where mypy may differ in its approach to
the ``typing.TYPE_CHECKING`` conditional block versus ``sphinx-autodoc-typehints`` (which
turns this flag on when ``set_type_checking_flag`` is set to ``True`` in ``docs/conf.py``).

----

.. automodule:: sphinx_demo
   :members:
   :undoc-members:
   :show-inheritance:


#.. automodule:: sphinx_demo.greeting1
#   :members:
#   :undoc-members:
#   :show-inheritance:
#
#
.. automodule:: sphinx_demo.greeting2
   :members:
   :undoc-members:
   :show-inheritance:


#.. automodule:: sphinx_demo.greeting3
#   :members:
#   :undoc-members:
#   :show-inheritance:
#
#.. automodule:: sphinx_demo.greeting4
#   :members:
#   :undoc-members:
#   :show-inheritance:
#
#.. automodule:: sphinx_demo.speaker1
#   :members:
#   :undoc-members:
#   :show-inheritance:
#
.. automodule:: sphinx_demo.speaker2
   :members:
   :undoc-members:
   :show-inheritance:

#.. automodule:: sphinx_demo.speaker3
#   :members:
#   :undoc-members:
#   :show-inheritance:
#
#.. automodule:: sphinx_demo.speaker4
#   :members:
#   :undoc-members:
#   :show-inheritance:
#
