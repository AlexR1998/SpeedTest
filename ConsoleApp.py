import pandas as pd
import sqlite3
from tabulate import tabulate
import pathlib
import os
import sys

sys.path.append("C:\\Users\\user\\Desktop\\speedtest\\execution\\")
from execution import main

class DataViewer:
    def __init__(self):
        self.dbname="record.db"
        self.csvname="record.csv"
        self.dbpath=str(pathlib.Path().resolve())+"\\execution\\data"
        self.my_execution=main.Main(self.csvname,self.dbpath)
        self.dbpath=self.dbpath+"\\"+self.dbname

    def CreateTables(self):
        connection=sqlite3.connect(self.dbpath)
        all=pd.read_sql("SELECT * FROM record",connection)
        day_avg=pd.read_sql("SELECT strftime('%Y/%m/%d',Date) AS Date, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency , COUNT(Download) AS NTests FROM record GROUP BY day",connection)
        ser_avg=pd.read_sql("SELECT Sponsor, Country, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency FROM record GROUP BY Sponsor",connection)
        gen_avg=pd.read_sql("SELECT strftime('%Y/%m/%d',Date) AS Date, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency FROM record",connection)
        total_count=pd.read_sql("SELECT COUNT(Download) AS TotalTests FROM record", connection)
        by_country=pd.read_sql("SELECT Country, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency), Count(Download) AS TestByCountry FROM record GROUP BY Country",connection)
        by_server=pd.read_sql("SELECT Sponsor, Count(Download) FROM record GROUP BY Sponsor", connection)
        by_hour=pd.read_sql("SELECT Hour, AVG(download) AS avgDownload, AVG(upload) AS avgUpload, AVG(latency) AS avgLatency , COUNT(Download) AS NTests FROM record GROUP BY Hour",connection)
        self.dbs=[all,day_avg,ser_avg,by_hour,gen_avg,by_country,by_server,total_count]

    def ShowMenu(self):
        print("--------------------------------------------------------------------------- SPEEDTEST DATABASE VIEWER ---------------------------------------------------------------------------\n")
        print("Type an option:\n")
        print("TEST OPTIONS\n1 Single Test\n2 Multiple Test\n""\nDATA VIEW OPTIONS\n3 All\n4 Daily Average\n5 Server Average\n6 By Hour Average\n7 General Average \n8 By Country Tests\n9 Server Tests\n10 Total Tests\n11 Menu\n""\n0 Close")

    def Selection(self):
        clear=lambda:os.system('cls')
        clear()
        self.CreateTables()
        self.ShowMenu()
        
        while(True):
            selection=int(input())
            if(selection>11 or selection<0):
                clear()
                print("Argument Out of Range")
                self.ShowMenu()
            elif(selection==1):
                print("Single test execution")
                self.my_execution.SingleExecution()
            elif(selection==2):
                print("Multiple execution")
                times=int(input("Times to be executed: "))
                self.my_execution.MultipleExecution(times)
            elif(selection==11):
                clear()
                self.ShowMenu()
            elif(selection==0):
                return
            else:
                print(tabulate(self.dbs[selection-3], headers='keys', tablefmt='psql'))
                print("Press 11 for return to the main menu")

viewer=DataViewer()
viewer.Selection()

