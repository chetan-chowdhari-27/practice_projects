
from setuptools import setup, find_packages

def get_requirements(file_path:str) -> list[str]:
    '''This functions is return all the list of requirements'''

    requirements = []
    with open(file_path,"r") as f:  # 1.)  Open the file and read all the lines
       requirements = f.readlines()    # 2.)  Read all the lines and store them in a list
       requirements =  [req.replace('\n','') for req in requirements] # 3.)  Strip each line and check if it's not empty
    return requirements # 4.)  Return the list of requirements


setup( 
    name='ml_pratice_projects', 
    version='0.1', 
    description='A Machine Learning Python project for Practice', 
    author='Chetan Chowdhari', 
    author_email='chetanchaudhari90014@gmail.com', 
    packages= find_packages(), 
    install_requires= get_requirements('requirements.txt')
) 


# if __name__ == "__main__":
#     print(get_requirements('requirements.txt'))