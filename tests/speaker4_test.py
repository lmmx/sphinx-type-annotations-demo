from pytest import fixture, mark

from sphinx_demo.greeting4 import Greeting4
from sphinx_demo.speaker4 import Speaker4


@fixture
def s():
    return Speaker4()


@fixture
def g(s):
    return Greeting4(speaker=s)


@mark.parametrize("expected", ["..."])
def test_initial_greeting(s, expected):
    """
    Test the ``greet`` method of ``Speaker`` returns "..."
    at initialisation.
    """
    assert s.greet() == expected


@mark.parametrize("expected", ["Hello world I'm Testing"])
def test_set_greeting(s, g, expected):
    """
    Test the ``greet`` method of ``Speaker`` after supplying
    a new greeting.
    """
    s.set_new_greeting(g)
    assert s.greet()
