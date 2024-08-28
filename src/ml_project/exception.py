import sys
from src.ml_project.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()  # getting the information of error
    file_name=exc_tb.tb_frame.f_code.co_filename # geeting the name of file were the error happpen
    error_message= "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) # formating error as per custom message

    return error_message # printing the values from function

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message) # its a constructor getting the values from parent class
        self.error_message = error_message_detail(error_message, error_details) # storing in error_message

    def __str__(self):
        return self.error_message # printing the error message

    
    