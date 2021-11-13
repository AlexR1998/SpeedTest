import sys
sys.path.append("C:\\Users\\user\\Desktop\\speedtest\\execution")

from analysis import analysis
from tester import Test, write

class Main():
    def __init__(self,csvname,csvdir):
        self.test=Test()
        self.write=write(csvdir,csvname)
        self.analyzer=analysis(csvdir,csvname)

    def SingleExecution(self):
        data=self.test.TestExecution()
        print(data)
        self.write.file_recorder(data)
        print("Data Saved")
        self.analyzer.exportData()
        print("Database updated")
    
    def MultipleExecution(self, executions):
        for i in range(executions):
            self.SingleExecution()
        print("Test executed {} times".format(executions))

