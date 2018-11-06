import json

class JsonExtract:

    def __init__(self,fileName, objDest):
        self.fileName = fileName;
        self.__fichier = ""
        self.objDest = objDest

    def open(self):
        with open(self.fileName) as json_data:
            self.__fichier = json.load(json_data)

    def readAndExtract(self):
        '''To read the json and extract it to the etl database'''
        for line in self.__fichier:

            #Gender is not always there
            gender = ""
            if 'gender' in line:
                gender = line["gender"].replace("Male","M").replace("Female","F")

            self.objDest.insertDestination(line["first_name"], line["last_name"], line["email"], gender,line["ville"])
            print(line["first_name"] + " " + line["last_name"] + " " + line["email"] + " " +
                  gender + " " + line["ville"])

    def close(self):
        print("")