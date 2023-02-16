# setup.py for `lpngram`

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
LOCAL_PATH = pathlib.Path(__file__).parent

# The text of the README file
README_FILE = (LOCAL_PATH / "README.md").read_text()

# Load requirements, so they are listed in a single place
with open("requirements.txt") as fp:
    install_requires = [dep.strip() for dep in fp.readlines()]

# This call to setup() does all the work
setup(
    author="Tiago Tresoldi",
    author_email="tiago.tresoldi@lingfil.uu.se",
    classifiers=[        "License :: OSI Approved :: MIT License",        "Operating System :: OS Independent",        "Programming Language :: Python :: 3",        "Topic :: Software Development :: Libraries",],
    description="Python libary for ngram collection and frequency smoothing",
    entry_points={"console_scripts": ["lpngram=lpngram.__main__:main"]},
    include_package_data=True,
    install_requires=install_requires,
    keywords=["ngram", "markov", "smoothing"],
    license="MIT",
    long_description=README_FILE,
    long_description_content_type="text/markdown",
    name="lpngram",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    test_suite="tests",
    tests_require=[],
    url="https://github.com/tresoldi/lpngram",
    version="0.2", # sync with __init__.py
    zip_safe=False,
)
