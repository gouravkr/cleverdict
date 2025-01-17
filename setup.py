# Auto-generated by easyPyPI: https://github.com/PFython/easypypi
# Preserve current formatting to ensure easyPyPI compatibility.

from pathlib import Path
from setuptools import find_packages
from setuptools import setup

HERE = Path(__file__).parent
NAME = "cleverdict"
GITHUB_ID = "Pfython"
VERSION = "1.9.1"
DESCRIPTION = "A JSON-friendly data structure which allows both object attributes and dictionary keys and values to be used simultaneously and interchangeably."
LICENSE = "MIT License"
AUTHOR = "Peter Fison"
EMAIL = "peter@awsom.solutions"
URL = "https://github.com/Pfython/cleverdict"
KEYWORDS = "cleverdict, data, attribute, key, JSON, autosave, autodelete, to_json, from_json, to_lines, from_lines, to_list, from_list, value, attributes, keys, values, database, utility, tool, clever, dictionary, att, __getattr__, __setattr__, getattr, setattr"
CLASSIFIERS = "Development Status :: 5 - Production/Stable, Intended Audience :: Developers, Operating System :: OS Independent, Programming Language :: Python :: 3.6, Programming Language :: Python :: 3.7, Programming Language :: Python :: 3.8, Programming Language :: Python :: 3.9, Topic :: Software Development :: Libraries :: Python Modules, Topic :: Software Development :: Object Brokering, Topic :: System :: Logging, Topic :: Utilities, License :: OSI Approved :: MIT License"
REQUIREMENTS = ""


def comma_split(text: str):
    """
    Returns a list of strings after splitting original string by commas
    Applied to KEYWORDS, CLASSIFIERS, and REQUIREMENTS
    """
    return [x.strip() for x in text.split(",")]


if __name__ == "__main__":
    setup(
        name=NAME,
        packages=find_packages(),
        version=VERSION,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=(HERE / "README.md").read_text(),
        long_description_content_type="text/markdown",
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        download_url=f"{URL}/archive/{VERSION}.tar.gz",
        keywords=comma_split(KEYWORDS),
        install_requires=comma_split(REQUIREMENTS),
        classifiers=comma_split(CLASSIFIERS),
    )
