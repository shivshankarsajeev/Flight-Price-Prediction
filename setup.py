from typing import List

from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    This fuction will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="Laptop-Price",
    version="0.0.1",
    author="shiv shankar s",
    author_email="shivshankarsajeev@gmail.com",
    packages=find_packages(),
    install_requiree=get_requirements("requirements.txt"),
)
