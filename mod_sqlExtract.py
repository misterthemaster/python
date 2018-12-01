from mod_sql import Sql

class SqlExtract(Sql):

    def __init__(self, host, user, password, db, objDest):
        self.conn = ""
        Sql.__init__(self, host, user, password, db)
        self.objDest = objDest

    def readAndExtract(self):
        '''To read the client database'''
        with self.conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `client_DATA`"
            cursor.execute(sql)
            result = cursor.fetchall()
            for line in result:
                self.objDest.insertDestination(line["first_name"], line["last_name"], line["email"], line["gender"],
                                               line["ville"])
                print(line["first_name"] + " " + line["last_name"] + " " + line["email"]
                    + " " + line["gender"] + " " + line["ville"])