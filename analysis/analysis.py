import pandas as pd
import sqlite3

from pandas.core.indexes.datetimes import DatetimeIndex

class analysis():
    def __init__(self,filepath,filename):
        self.__path=filepath+"/"+filename
        print(self.__path)

    def correctypes(self):
        self.data=pd.read_csv(self.__path,index_col=False)
        self.data['Date']=pd.to_datetime(self.data['Date'],format='%d/%m/%Y %H:%M:%S')
        self.data['Day']=DatetimeIndex(self.data['Date']).day

    def exportData(self):
        self.correctypes()
        connection=sqlite3.connect('record.db')
        c=connection.cursor()
        self.data.to_sql('record', connection, if_exists='replace', index = False)
        connection.close()

    def createAnalysis(self):
        self.exportData()
        connection=sqlite3.connect('record.db')
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
        self.n_tests=c.execute("SELECT count(*) FROM record").fetchone()[0]
        connection.close()
        print("Analysis Created")

path="C:/Users/user/Desktop/speedtest"
filename="record.csv"
analyzer=analysis(path,filename)
analyzer.createAnalysis()