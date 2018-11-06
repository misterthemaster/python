from mod_sql import Sql

class SqlExtract(Sql):

    def __init__(self, host, user, password, db):
        self.conn = ""
        Sql.__init__(self, host, user, password, db)

    def readSource(self):
        print("-------------------")
        with self.conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `client_DATA`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)
