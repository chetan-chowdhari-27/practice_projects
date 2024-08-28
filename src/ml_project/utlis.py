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