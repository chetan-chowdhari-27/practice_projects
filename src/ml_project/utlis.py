import os
import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from dotenv import load_dotenv
import pandas as pd
import pymysql
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score



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
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for model_name, model in models.items():
            para = param[model_name]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)