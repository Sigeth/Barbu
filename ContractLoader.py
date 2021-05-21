import json
import os

class ContractLoader:
    """
    Convertit les fichiers contracts json en dictionnaire. 
    """

    def __init__(self):
        self.subdir = './contracts'
        self.contractDic = []


    def loadContracts(self) -> list:
        #for every contract file
        for filename in os.listdir(self.subdir):
             if filename.endswith(".json"):    
                self.contractDic.append(self.loadContract(os.path.join(self.subdir,filename)))
        return self.contractDic


    def loadContract(self,filename) -> dict:
        f = open(filename, "r")
        return json.loads(f.read())
