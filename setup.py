from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str] :
    # returns the list of all the requirements mentioned in requirements.txt (file path)

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [rep.replace("\n", "") for rep in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup (
    name='Youtube_Comment_Extraction_and_Sentiment_Analysis',
    version='0.0.1',
    author='ByteWizard18',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)