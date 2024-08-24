import logging
import os
from pathlib import Path


logging.basicConfig(level=logging.INFO)

# require files for projects 
project_names = "ml_project"
list_of_files = [
    f'src/{project_names}/__init__.py',
    f'src/{project_names}/components/__init__.py',
    f'src/{project_names}/components/data_ingestion.py',
    f'src/{project_names}/components/data_transformation.py',
    f'src/{project_names}/components/model_trainer.py',
    f'src/{project_names}/components/model_monitoring.py',
    f'src/{project_names}/pipelines/__init__.py',
    f'src/{project_names}/pipelines/training_pipelines.py',
    f'src/{project_names}/pipelines/prediction_pipelines.py',
    f'src/{project_names}/exception.py',
    f'src/{project_names}/logger.py',
    f'src/{project_names}/utlis.py',
    'Dockerfile',
    'app.py'    
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    # print(filename)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directing: {filedir} for the file {filename}")

    if(not os.path.exists(filepath)) or  (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file: {filename}')
    else:
        logging.info(f'file already exists: {filename}')




