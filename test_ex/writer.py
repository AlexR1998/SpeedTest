import os
class write:
    def __init__(self,filename,dir):
        self.name=filename
        self.dir=dir
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
        f=open(self.dir+"\\"+self.name,"a")
        for element in content:
            f.write(element+",")
        f.write("\n")
        f.close()
