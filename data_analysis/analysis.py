import pandas as pd
import sqlite3
from pandas.core.indexes.datetimes import DatetimeIndex

class analysis():
    def __init__(self,filepath,filename):
        self.__path=filepath
        self.__filename=filename

    def correctypes(self):
        self.data=pd.read_csv(self.__path+"/"+self.__filename,index_col=False,encoding='latin-1')
        self.data['Date']=pd.to_datetime(self.data['Date'],format='%d/%m/%Y %H:%M:%S')
        self.data['Day']=DatetimeIndex(self.data['Date']).day

    def exportData(self):
        #Review for complete and not re-write entire bd
        self.correctypes()
        connection=sqlite3.connect(self.__path+"/"+'record.db')
        c=connection.cursor()
        self.data.to_sql('record', connection, if_exists='replace', index = False)
        connection.close()

    def createAnalysis(self):
        self.exportData()
        connection=sqlite3.connect(self.__path+"/"+'record.db')
        c=connection.cursor()
        c.execute("DROP TABLE IF EXISTS day_avg")
        c.execute("DROP TABLE IF EXISTS ser_avg")
        c.execute("DROP TABLE IF EXISTS gen_avg")

        #Promedio up,down,ping / día
        c.execute("CREATE TABLE day_avg AS SELECT strftime('%Y/%m/%d',Date) AS Date, AVG(download), AVG(upload), AVG(latency) FROM record GROUP BY day")
        #Promedio up,down,ping / servidor
        c.execute("CREATE TABLE ser_avg AS SELECT Sponsor, AVG(download), AVG(upload), AVG(latency) FROM record GROUP BY Sponsor")
        #Promedio general up,down,ping
        c.execute("CREATE TABLE gen_avg AS SELECT strftime('%Y/%m/%d',Date) AS Date, AVG(download), AVG(upload), AVG(latency) FROM record")   
        connection.close()
        print("Analysis Created")
