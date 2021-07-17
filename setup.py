from pathlib import Path

from setuptools import find_packages, setup

NAME = "sphinx_demo"
EXTRAS_REQUIRE = {
    "docs": [
        "sphinx>=4",
        "sphinx_rtd_theme",
        "sphinx-autodoc-typehints",
    ],
    "tests": ["pytest"],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["docs"] + ["pre-commit"]
)
PYTHON_REQUIRES = ">=3.8"
PACKAGE_DATA = {"sphinx_demo": ["py.typed"]}

if __name__ == "__main__":
    setup(
        name=NAME,
        packages=find_packages("src"),
        package_dir={"": "src"},
        package_data=PACKAGE_DATA,
        include_package_data=True,
        zip_safe=False,
        extras_require=EXTRAS_REQUIRE,
        python_requires=PYTHON_REQUIRES,
    )
