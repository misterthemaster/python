class FileExtract:

    def __init__(self,fileName):
        self.fileName = fileName;
        self.__fichier = ""

    def open(self):
        self.__fichier = open(self.fileName)

    def readSource(self):
        for line in self.__fichier:
            print (line)

    def close(self):
        print("à fermer")