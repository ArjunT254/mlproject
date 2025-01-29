from setuptools import find_packages,setup
# find packages finds out all the packages you have used in your code
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requierments=[]
    with open(file_path) as file_obj:
        requierments=file_obj.readlines()
        requierments=[req.replace("\n","") for req in requierments]
        if HYPEN_E_DOT in requierments:
            requierments.remove(HYPEN_E_DOT)
    
    print(requierments)
    return requierments
                                
setup(
    name='mlproject',
    version='0.0.1',
    author='Arjun',
    author_email='arjunt426@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn']   # list of packages you would be using  
    install_requires=get_requirements('requirements.txt')  # this function read the libraries in requirement
)