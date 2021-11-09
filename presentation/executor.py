import os
import sys
sys.path.insert(0,'C:/Users/user/Desktop/speedtest')
from test_ex import tester,writer

class executor():
    def __init__(self,record_name,record_directory):
        self.__my_test=tester.Test()
        self.__my_writer=writer.write(record_name,record_directory)

    def singleExecution(self):
        self.data=self.__my_test.TestExecution()
        self.__my_writer.file_recorder(self.data)
        print(self.data)
    
    def multipleExecution(self,times):
        for i in range(times):
            self.singleExecution()

path="C:/Users/user/Desktop/speedtest/presentation"
my_executor=executor("record.csv",path)
my_times=int(sys.argv[1])
my_executor.multipleExecution(my_times)