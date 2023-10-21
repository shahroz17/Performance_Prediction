import sys    #provides various function and variables that are used to manipulate different part of runtime envirmnet

from src.logger import logging


def error_message_detail(error,error_detail:sys): # own coustom error
    _,_,exc_tb=error_detail.exc_info()  #which line number where occured this variable will give
    file_name=exc_tb.tb_frame.f_code.co_filename  #exectional handling document 
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):   # to print the error message
        return self.error_message
    

