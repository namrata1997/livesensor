from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    
    requirements_list : List[str] = []

    return requirements_list


setup(

    name="sensor",
    version="0.0.1",
    author="Nicolas",
    author_email="atri.namrata06@gmail.com",
    packages = find_packages() ## finds all packages in the current directory i.e.__init__.py
    install_requires =  get_requirements()#['pymongo'],
    description = "This is a sensor package"

)