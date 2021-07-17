# Sphinx Type Annotations Demo

A demo of how to build Sphinx docs with type annotations in the presence of circular imports.

## Summary

The README advice for `sphinx-autodoc-typehints` suggests to deal with circular imports as follows:

> Sometimes functions or classes from two different modules need to reference each other in their
> type annotations. This creates a circular import problem. The solution to this is the following:

> 1.  Import only the module, not the classes/functions from it
> 2.  Use forward references in the type annotations
>     (e.g. `def methodname(self, param1: 'othermodule.OtherClass'):`)

I tried this in a library with a circular import, and it didn't work, nor did it when I simplified
to the minimal possible example (in this repo!)


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
# if True:
if TYPE_CHECKING:
    import sphinx_demo

class Speaker:
    ...
    
    def set_new_greeting(self, greeting: sphinx_demo.greeting.Greeting) -> None:
        self.greeting = greeting
```

and in `greeting.py`:

```py
# if True:
if TYPE_CHECKING:
    import sphinx_demo

class Greeting:
    def __init__(self, speaker: sphinx_demo.speaker.Speaker, message: str = "Hello "):
        self.speaker = speaker
```

If you swap the commented out `if True` with the (uncommented) `if TYPE_CHECKING:`
the error will go away.

Specifically, the error given is that Sphinx cannot resolve a forward reference in each
of the classes `Speaker` and `Greeting`, as the `name 'sphinx_demo' is not defined`
(i.e. the module's name is not defined)

```
WARNING: Cannot resolve forward reference in type annotations of "sphinx_demo.greeting.Greeting":
name 'sphinx_demo' is not defined
WARNING: Cannot resolve forward reference in type annotations of
"sphinx_demo.speaker.Speaker.set_new_greeting": name 'sphinx_demo' is not defined
```

This doesn't make sense given the advice to import the module was followed, so I'm reproducing
it to see if I can find a solution.
