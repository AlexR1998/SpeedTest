from os import path
import sys
import pathlib
root_path=str(pathlib.Path().resolve())[:-21]
sys.path.insert(0,root_path)

from data_analysis import analysis
from executor import executor

path=root_path+"\\"+"data"
file="record.csv"

def execution():
    try:
        #Instance clases
        my_executor=executor(path,file)
        my_analysis=analysis.analysis(path,file)

        #Get variables and start execution
        my_times=int(sys.argv[1])
        my_executor.multipleExecution(my_times)

        #Save analysis
        my_analysis.createAnalysis()
    except:
        print("An exception ocurred, check your internet connection and retry the test.")
        return

execution()


