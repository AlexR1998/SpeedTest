import test
import writer
import os

class executor():
    def __init__(self,record_name,record_directory):
        self.__my_test=test.Test()
        self.__my_writer=writer.writer(record_name,record_directory)

    def singleExecution(self):
        self.data=self.__my_test.TestExecution()
        self.__my_writer.file_recorder(self.data)
        print(self.data)
    
    def multipleExecution(self,times):
        for i in range(times-1):
            self.singleExecution()

my_executor=executor("record.csv",os.getcwd())
my_executor.multipleExecution(5)