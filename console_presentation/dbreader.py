import pandas as pd
import sqlite3
from tabulate import tabulate
import pathlib
import os

class DataViewer:
    def __init__(self):
        self.path=str(pathlib.Path().resolve()).replace("\console_presentation","")+"\\data\\record.db"

    def CreateTables(self):
        connection=sqlite3.connect(self.path)
        day_avg=pd.read_sql("SELECT strftime('%Y/%m/%d',Date) AS Date, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency , COUNT(Download) AS NTests FROM record GROUP BY day",connection)
        ser_avg=pd.read_sql("SELECT Sponsor, Country, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency FROM record GROUP BY Sponsor",connection)
        gen_avg=pd.read_sql("SELECT strftime('%Y/%m/%d',Date) AS Date, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency FROM record",connection)
        total_count=pd.read_sql("SELECT COUNT(Download) AS TotalTests FROM record", connection)
        by_country=pd.read_sql("SELECT Country, Count(Download) AS TestByCountry FROM record GROUP BY Country",connection)
        by_server=pd.read_sql("SELECT Sponsor, Count(Download) FROM record GROUP BY Sponsor", connection)
        by_hour=pd.read_sql("SELECT Hour, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency , COUNT(Download) AS NTests FROM record GROUP BY Hour",connection)
        self.dbs=[day_avg,ser_avg,by_hour,gen_avg,by_country,by_server,total_count]

    def ShowMenu(self):
        print("--------------------------------------------------------------------------- SPEEDTEST DATABASE VIEWER ---------------------------------------------------------------------------\n")
        print("Select an option for view the table:\n")
        print("1 Daily Average\n2 Server Average\n3 By Hour Average\n4 General Average \n5 By Country Tests\n6 Server Tests\n7 Total Tests\n8 Menu\n""\n0 Close")

    def Selection(self):
        clear=lambda:os.system('cls')
        clear()
        self.CreateTables()
        self.ShowMenu()
        
        while(True):
            selection=int(input())
            if(selection>8 or selection<0):
                clear()
                print("Argument Out of Range")
                self.ShowMenu()
            elif(selection==8):
                clear()
                self.ShowMenu()
            elif(selection==0):
                return
            else:
                print(tabulate(self.dbs[selection-1], headers='keys', tablefmt='psql'))
                print("Press 8 for return to the main menu")

viewer=DataViewer()
viewer.Selection()

