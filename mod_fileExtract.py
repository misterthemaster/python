class FileExtract:

    def __init__(self,fileName):
        self.fileName = fileName;
        self.__fichier = ""

    def open(self):
        '''To open the file'''
        self.__fichier = open(self.fileName)

    def readAndExtract(self):
        '''To read the file and extract it to the etl database'''
        for line in self.__fichier:
            lineSplit = line.split(",")
            print(lineSplit[1] + " " + lineSplit[2] + " " + lineSplit[3] + " "
                  + lineSplit[4].replace("Male","M").replace("Female","F") + " " + lineSplit[5])

    def close(self):
        self.__fichier.close()