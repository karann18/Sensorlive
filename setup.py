from setuptools import find_packages, setup
from typing import List

def getRequirements() -> List[str]:
    """
    
    This function returns a list of requirements for the package.

    """
    requirements_list : List[str] = []

    """
    write a code to get the requirmennts from thee requirements.txt file

    """
    return requirements_list



setup(
    name="sensorlive",
    version="0.0.1",
    author="karan",
    author_email="karanvishwakarma2718@gmail.com",
    packages=find_packages(),
    install_requires=getRequirements(),
)
