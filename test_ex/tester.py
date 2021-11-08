from speedtest import Speedtest
from datetime import datetime

class Test:
    def __init__(self):
        self.__s=Speedtest()
        self.__data=[]

    def TestExecution(self):
        self.__data.clear()
        print("Testing...")
        self.__data.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.__data.append(str(round(self.__s.download()/1048576,2)))
        self.__data.append(str(round(self.__s.upload()/1048576,2)))
        self.__data.append(self.__s.get_best_server()['name'])
        self.__data.append(self.__s.get_best_server()['country'])
        self.__data.append(self.__s.get_best_server()['sponsor'])
        self.__data.append(str(self.__s.get_best_server()['latency']))
        return self.__data
