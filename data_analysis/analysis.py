import pandas as pd
import sqlite3
from pandas.core.indexes.datetimes import DatetimeIndex
from datetime import datetime

from pandas.io.parquet import FastParquetImpl

class analysis():
    def __init__(self,filepath,filename):
        self.__path=filepath
        self.__filename=filename

    def correctypes(self):
        print(self.__path+"/"+self.__filename)
        self.data=pd.read_csv(self.__path+"/"+self.__filename,index_col=False,encoding='latin-1')
        self.data['Date']=pd.to_datetime(self.data['Date'],format='%d/%m/%Y %H:%M:%S')
        self.data['Day']=DatetimeIndex(self.data['Date']).day
        self.data['Hour']=self.data['Date'].dt.hour
        print(self.data)

    def exportData(self):
        #Review for complete and not re-write entire bd
        self.correctypes()
        connection=sqlite3.connect(self.__path+"/"+'record.db')
        c=connection.cursor()
        self.data.to_sql('record', connection, if_exists='replace', index = False)
        connection.close()
