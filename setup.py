from setuptools import find_packages, setup
from typing import List

hyphen ='-e .'

def get_requirements(file_path:str)->List[str]:
    """This function returns a list of requirements from a given file path."""
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hyphen in requirements:
            requirements.remove(hyphen)
    return requirements

setup(
    name='mlproject',
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)