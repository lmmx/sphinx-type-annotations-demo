# Sphinx Type Annotations Demo

A demo of how to build Sphinx docs with type annotations in the presence of circular imports.

## Summary

> The possible ways `sphinx-autodoc-typehints` will let you use absolute imports
> to resolve circular imports from importing annotation classes in a
> `if typing.TYPE_CHECKING` conditional block is a partially overlapping set
> of the possible ways to type hint a library with mypy alone.

## Demo files

There are four working versions that represent different options for type annotations in Sphinx docs,
included in this repo as separate modules:

- [`speaker1.py`](src/sphinx_demo/speaker1.py) - class import from package module, `class` annotation
- [`speaker2.py`](src/sphinx_demo/speaker2.py) - module import from package, `module.class` annotation
- [`speaker3.py`](src/sphinx_demo/speaker3.py) - package import, `package.module.class annotation`
- [`speaker4.py`](src/sphinx_demo/speaker4.py) - direct class import from package, `class` annotation

The 4th has Sphinx-specific caveats that require a little explanation (use with care!)

### Option 1

Option 1 is to import the module:

```py
if typing.TYPE_CHECKING:
    from sphinx_demo import greeting1
```

where the signature for the `set_new_greeting` method of the `Speaker1` class is:

```py
def set_new_greeting(self, greeting: greeting.Greeting1) -> None:
```

### Option 2

Option 2 is to import the class itself

```py
if typing.TYPE_CHECKING:
    from sphinx_demo.greeting2 import Greeting2
```

where the signature for the `set_new_greeting` method of the `Speaker2` class is:

```py
def set_new_greeting(self, greeting: Greeting2) -> None:
```

Note that this will also work with just `from sphinx_demo import greeting2`, i.e.
without importing the class name itself (just the module `greeting2`)!
However mypy rejects this approach.

Like standard Python usage, mypy requires you to specify the 'full address' of names
you use, relative to names you import into the namespace (be they package names or
module names). Sphinx seems to just figure it out, but you shouldn't do so.

### Option 3

Option 3 is to import the entire package

```py
if typing.TYPE_CHECKING:
    import sphinx_demo
```

where the signature for the `set_new_greeting` method of the `Speaker3` class is:

```py
def set_new_greeting(self, greeting: sphinx_demo.greeting3.Greeting3) -> None:
```

This is the most verbose approach, and in my opinion is bad for the code's readability.

Here, only the package name is provided, and yet Sphinx is able to detect
the module name, and just the type annotation `greeting: greeting3.Greeting3` will work!
This time, without importing the module itself (just the package  `sphinx_demo`)!
Just annotating the class name `greeting: Greeting3` will likewise work, as for option 2.
However mypy rejects both of these approaches once again.

### Summary of options

The options are:

1. `greeting: Greeting1` with conditional import `from sphinx_demo.greeting1 import Greeting1`
2. `greeting: greeting2.Greeting2` with conditional import `from sphinx_demo import greeting2`
3. `greeting: sphinx_demo.greeting3.Greeting3` with conditional import `import sphinx_demo`

Which you choose is just down to how concise (or inversely, how informative) you want your
type annotations to be.

Usually it's nice to have concise (shorter, less repetition/"boilerplate"), so we'd choose option 1.
If you always want to note which modules/libraries provide which classes you'd choose option
2 or 3 respectively.

Total characters on the annotation:

1. 9(`Greeting1`) = 9
2. 9+1+9(`greeting2.Greeting2`) = 19
3. 11+1+9+1+9(`sphinx_demo.greeting3.Greeting3`) = 31

Both writing and (re-)reading 9 characters is easier going than 31. We'll come back to this point.

## Restrictions on usage

In particular, to satisfy Sphinx, you need to put all modules containing classes to be
annotated in the package namespace. (mypy does not impose this restriction.)

E.g. for (package.module.class) `pkg.mod.Cls`, you put in `src/pkg/__init__.py` either:

- `from . import mod`
  - `__all__ = ["mod"]` if explicitly declaring the namespace

- `from .mod import Cls` in `pkg/__init__.py`
  - `__all__ = ["mod", "Cls"]` if explicitly declaring the namespace


If you look at [this package's `__init__.py`](src/sphinx_demo/__init__.py) you'll see it uses
the first option: it just imports the modules, not the classes.

Often though you'll want to expose classes as 'top-level' names in the package namespace,
e.g. `sphinx_demo.Speaker1` might be the "main character" of your package's API so you might
want to let users `from sphinx_demo import Greeting1` directly.

Firstly we'd need to import it from the `greeting1` module in the package's `__init__.py`:

```py
from .greeting1 import Greeting1
```

- Note that this puts both `greeting1` and `Greeting1` into the package namespace, so it
  can be removed from the modules listed on the `from . import ...` line

...then modify `speaker1.py` accordingly to use this top-level exposed name, and comment out the
old one:

```py
if TYPE_CHECKING:
    # from sphinx_demo import greeting1
    from sphinx_demo import Greeting1
```

This seems much better, as now you'll be able to replace the type annotation too, surely?

```py
#greeting: greeting1.Greeting1
greeting: Greeting1
```

mypy is happy with this (as the `Greeting1` class been imported into the namespace), but
what about Sphinx?

```
WARNING: Cannot resolve forward reference in type annotations of "sphinx_demo.Greeting1": name
'speaker1' is not defined
```

It won't work with this top-level 'exposed' class `Greeting1`, since the definition of `Greeting1`
relies on importing the module `speaker1`.

It's kind of possible to see the cause here: you're taking a shortcut to the class (`Greeting1`)
directly in the package namespace (`__init__.py`) even though it comes from a module (`greeting1`),
and that module is relying on the module name `speaker1`... which hasn't been 'gotten to' when
you're in the package namespace (`__init__.py`).

It's unclear why mypy wouldn't have a problem with this but Sphinx would, but since it's pretty
clear (as far as I can tell) that this is a hard rule, then to avoid the error you can just make
sure not to take that 'shortcut' when type annotating, since while mypy will allow it,
you'll break your Sphinx build.

#### :four_leaf_clover: Bonus 4th option :four_leaf_clover:

In fact, it's even more strict than that. You cannot (as far as I can tell) import a class which is
in one of these circular reference loops into the top-level namespace (even if you don't then
import it for a type annotation).

To back up to the step before exploring how to import `Greeting1` to annotate `speaker1.Speaker1`
directly, where the import was:

```py
if TYPE_CHECKING:
    from sphinx_demo import greeting1
```

and the signature was

```py
greeting: greeting1.Greeting1
```

and returning to the package `__init__.py`, we'll find it's possible to add the class import:

```py
from sphinx_demo.greeting1 import Greeting1
```

...and without putting `Greeting1` into `__all__`, the docs will still build, and in fact you still
get the class 'available' from the package as a tab-completable name in the namespace:

```py
>>> import sphinx_demo
>>> sphinx_demo.
sphinx_demo.Greeting1(  sphinx_demo.bases       sphinx_demo.greeting1   sphinx_demo.greeting2
sphinx_demo.greeting3   sphinx_demo.speaker1    sphinx_demo.speaker2    sphinx_demo.speaker3
```

...but the moment you put that class into `__all__`, the forward reference error returns to Sphinx.

I don't really feel this is so bad (compared to not being able to put particular classes in the
top-level package namespace at all)!

---

So this means there's a 4th option, with an annotation identical to that of option 1:

> 1. `greeting: Greeting1` with conditional import `from sphinx_demo.greeting1 import Greeting1`

but it will differ in its import line, which can drop the `greeting1` module, provided the class
is available (but not 'exported') in the package 'top-level' namespace.

4. `greeting: Greeting4` with conditional import `from sphinx_demo import Greeting1`

This is the most concise way, but it should come with the warning about the possibility
of breaking your Sphinx build (with an uninformative error message) if you accidentally let
put one of those top-level exposed classes in the package's `__all__` list.

## What you need to know

- **Option 4:**
  If you import classes into the top level of your package, you get more concise type annotation
  imports, but if they get into the `__all__` (or presumably if you don't specify `__all__`
  explicitly whatsoever) you'll break your Sphinx build
  - if you're not using `__all__` but want top-level classes and Sphinx type annotations, start
    using it so you can control your package namespace to keep those classes out of it
  - There's a case that can be argued that letting docs dictate your package layout is undesirable,
    but if it really just comes down to `__all__` then that might not be so bad.
- **Option 1:**
  If you don't want to do any of that, the reliable and most concise option for annotations is
  to import classes from their module.

## Setup

I used `conda` to set up this environment and `tox` to run the CI steps,
with checks done by `pre-commit`.

```sh
conda create -n sphinx_typing_bug_demo
conda activate sphinx_typing_bug_demo
conda install python=3.9
git clone https://github.com/lmmx/sphinx-typing-bug-demo/
pip install -e .[docs]
```

Then `pip install tox`, `tox -e docs` will run the docs step of the CI pipeline.

- If you want to use Python 3.8, this wasn't what I used but you can do so by changing the
  version in the command above. I have verified that the result is identical.
- If you want to use a different version of Sphinx, simply replace `"sphinx>=4",` in the `setup.py`
  list `EXTRAS_REQUIRE` for the `docs` subset of requirements with a specific pinned version, such
  as `"sphinx==4.0.0",`. I tried v4.0.0 and got
  the same result, so it doesn't seem to be a deprecation since this feature was introduced
  in March.
- Disabling the Napoleon extension and features does not affect the result

The simplest way to then build the docs is to run

```sh
cd docs
make html
```

and on any further runs (rebuilding) run the following (again in the `docs/` directory):

```sh
rm -rf _build && make html
```

## Development

To develop with this setup, also install pre-commit and tox

```sh
pip install tox # to run the test and build suites locally
pip install pre-commit # to run the pre-commit hooks on git commit
```

## Addenda

- If using test coverage, add `# pragma: no cover` to the `if TYPE_CHECKING:` line.
  I've not done so here since it's meant to be a minimal reproducible example.

- A good reason to use `tox` for building Sphinx docs is that it uses virtualenv to
  take care of the PATH, whereas if you call `make html` from your `docs` directory
  directly you'll (sometimes? seemingly at random?) get errors about your package not
  being found (but then sometimes it'll build them just fine).
  - To just build the docs in this repo's `tox` workflow, run `tox -e docs`. Just running
    `tox` will run `mypy` and the `tests` too.
