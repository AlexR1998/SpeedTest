from speedtest import Speedtest
from datetime import datetime
import os 

class Test:
    def __init__(self):
        self.__data=[]
        self.__s=Speedtest()

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

class write:
    def __init__(self,csvdir,csvname):
        self.name=csvname
        self.dir=csvdir
        self.file_creator()

    def file_creator(self):
        if(os.path.exists(self.dir+"\\"+self.name)):
            print("Record alredy exist")
            return
        print("Record doesn't exist (creating)")
        f=open(self.dir+"\\"+self.name,"w")
        f.write(f"Date,Download,Upload,Name,Country,Sponsor,Latency\n")
        f.close()

    def file_recorder(self,content):
        self.file_creator()
        f=open(self.dir+"\\"+self.name,"a")
        for element in content:
            f.write(element+",")
        f.write("\n")
        f.close()
