import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException 
from src.ml_project.components.data_ingestion import DataIngestionConfig
from src.ml_project.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    logging.info('the  script is running')

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion= DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e,sys)