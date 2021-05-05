import json
import os

class ContractLoader:

    def __init__(self):
        print("ça marche ?")
        self.subdir = './contracts'
        self.contractDic = []

    def loadContracts(self):
        #for every contract file
        for filename in os.listdir(self.subdir):
             if filename.endswith(".json"):    
                self.contractDic.append(self.loadContract(os.path.join(self.subdir,filename)))
        return self.contractDic


    def loadContract(self,filename):
        f = open(filename, "r")
        return json.loads(f.read())
