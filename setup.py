from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DIT ="-e ."

def get_requirements(file_path:str)->List[str]:
    """
    this funtion will return the list of requirements
    """
    requirements =[]
    with open("requirements.txt") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]

        if HYPHEN_E_DIT in requirements:
            requirements.remove(HYPHEN_E_DIT)

    return requirements

setup(
    name="Detection_Projects",
    version="0.0.1",
    author="Pushpendra Maurya",
    author_email="pushpendramaurya143654@gmail.com",
    packages=find_packages(),
    Install_requires = get_requirements("requirements.txt")

)        