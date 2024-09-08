import os
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from dotenv import load_dotenv
import pandas as pd
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
passwords = os.getenv("passwords")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading from SQL Database Started")
    try:
        mydb= pymysql.connect(
            host=host,
            user=user,
            password=passwords,
            db=db
        )
        logging.info("Connection Established")
        df = pd.read_sql_query('SELECT * FROM students;',mydb)
        print(df.head())

        return df
    except Exception as x:
        raise CustomException(x,sys)
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)