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

```

## Development

To develop with this setup, also install pre-commit and tox

```sh
pip install tox # to run the test and build suites locally
pip install pre-commit # to run the pre-commit hooks on git commit
```
