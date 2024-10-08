import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException 
from src.ml_project.components.data_ingestion import DataIngestionConfig
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.components.data_transformation import DataTransformation
from src.ml_project.components.model_trainer import ModelTrainerConfig,ModelTrainer

if __name__ == "__main__":
    logging.info(' The script is running')

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion= DataIngestion()
        # data_ingestion.initiate_data_ingestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        # Model trainer 
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e,sys)