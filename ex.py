import sys
sys.path.append("C:\\Users\\user\\Desktop\\speedtest\\execution")
from execution import main
import pathlib

dbpath=str(pathlib.Path().resolve())+"\\execution\\data"
csvname="record.csv"
my_execuution=main.Main(csvname,dbpath)
my_times=int(sys.argv[1])
my_execuution.MultipleExecution(my_times)
