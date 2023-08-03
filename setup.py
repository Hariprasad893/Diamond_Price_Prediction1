# This file is needed when the project is to be converted into
# an app
# This file contains the basic information of the project

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        req = f.readlines()
        requirements=[r.replace("\n","") for r in req]
        return requirements
    

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Hariprasad V L',
    author_email='hariprasads0s123@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()
)