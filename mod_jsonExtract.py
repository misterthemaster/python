import json

class JsonExtract:

    def __init__(self,fileName):
        self.fileName = fileName;
        self.__fichier = ""

    def open(self):
        with open(self.fileName) as json_data:
            self.__fichier = json.load(json_data)

    def readSource(self):
        for line in self.__fichier:
            print(line)

    def close(self):
        print("à fermer")