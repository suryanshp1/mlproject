from setuptools import find_packages, setup
from src.__version__ import __version__
from typing import List


HYPHEN_E_DOT = "-e ."

def get_requirements(filepath: str)->List[str]:
    """
    this function will return list of requirements
    """
    requirements: List[str] = []
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[r.replace("\n","") for r in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name="mlproject",
    version=__version__,
    packages=find_packages(),
    author="Suraj",
    author_email="suryanshp1@gmail.com",
    install_requires=get_requirements("requirements.txt"),
)