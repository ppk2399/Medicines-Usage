from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.

    Parameters:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of requirements excluding '-e .'
    """
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        # Optional: Validate that requirements are not empty
        if not requirements:
            raise ValueError("The requirements file is empty.")
        
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

    return requirements

setup(
    name='Medicines Usage',
    version='0.0.1',
    author='Pavan',
    author_email='ppk2399@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
