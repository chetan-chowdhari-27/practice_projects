# database -> data --> train test split -->  model --> predict
import os 
import sys # to handle custom exception 
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
from dataclasses import dataclass
import pandas as pd 
from src.ml_project.utlis import read_sql_data
from sklearn.model_selection import train_test_split


@dataclass 
class DataIngestionConfig:
    """This class contains configuration related to data ingestion."""
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig

    def initiate_data_ingestion(self):
        try:
            df = read_sql_data()
            # Reading the data from 
            logging.info("Reading completed mysql database")
            # saving raw data to csv file
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            # spliting the data 80 % for training and 20% for testing
            train_set, test_set= train_test_split(df, test_size=0.2,random_state=42)
            
            #  saving the data in csv format
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info("Data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
