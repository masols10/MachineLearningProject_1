from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) ->List[str]:
    '''
    This func will return the list of requiremnts
    '''
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("\n","")for r in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)

    return req 


setup(
name = 'MYPROJECTS',
version = '0.0.1',
author = 'manasa',
author_email = 'manasa.solasa10@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)