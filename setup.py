from setuptools import find_packages,setup

#setuptools is a Python package that helps you package, distribute, and install your Python projects.

  #Think of it like a toolbox that helps you turn your raw Python project into a nicely installable Python package that can be shared via PyPI or reused in other projects.

from typing import List
HYPHEN_E_DOT ='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)    
    return requirements 




setup(

    name='Fault Detection',
    version='0.0.1',
    author='Ved pandya',
    author_email='pandyaved943@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)
