# Sphinx Type Annotations Demo

A demo of how to build Sphinx docs with type annotations in the presence of circular imports.

Originally a bug reproduction repo, but bug identified and resolved
(sphinx-autodoc-typehints issue
[#180](https://github.com/agronholm/sphinx-autodoc-typehints/issues/180))

## Summary

The README advice for `sphinx-autodoc-typehints` suggests to deal with circular imports as follows:

> Sometimes functions or classes from two different modules need to reference each other in their
> type annotations. This creates a circular import problem. The solution to this is the following:

> 1.  Import only the module, not the classes/functions from it
> 2.  Use forward references in the type annotations
>     (e.g. `def methodname(self, param1: 'othermodule.OtherClass'):`)

This repo contains a working example of resolving this.

It previously did not work due to the presence of the autosummary extension,
which prevented the proper activation of the `typing.TYPE_CHECKING` flag.

## How to reproduce

```sh
git clone https://github.com/lmmx/sphinx-type-annotations-demo
cd sphinx-type-annotations-demo
pip install tox
pip install -e .[docs]
tox -e docs # or `cd docs && make html`
```

## Development

To develop with this setup, also install pre-commit and tox

```sh
pip install tox # to run the test and build suites locally
pip install pre-commit # to run the pre-commit hooks on git commit
```

## Explanation

In short, the important parts of the module `speaker.py` are:

```py
if TYPE_CHECKING:
    import sphinx_demo

class Speaker:
    ...

    def set_new_greeting(self, greeting: sphinx_demo.greeting.Greeting) -> None:
        self.greeting = greeting
```

and in `greeting.py`:

```py
if TYPE_CHECKING:
    import sphinx_demo

class Greeting:
    def __init__(self, speaker: sphinx_demo.speaker.Speaker, message: str = "Hello "):
        self.speaker = speaker
```
