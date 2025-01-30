import sys # handle exception in python

from logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # this func will give you info about which file the 
    #exception has occured, which line caused the exception
    file_name=exc_tb.tb_frame.f_code.co_filename # to get file name which caused error

    error_message='Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):  # This is inheriting the parent exception
        def __init__(self,error_message,error_detail:sys):
            super().__init__(error_message) #Inherit exception class
            self.error_message=error_message_details(error_message,error_detail=error_detail)

        def __str__(self):
            return self.error_message
        



        