import pymysql.cursors
from mod_sql import Sql

class SqlImport(Sql):
    def __init__(self, host, user, password, db):
        self.conn = ""
        Sql.__init__(self, host, user, password, db)

    def recreateTableDestination(self):
        with self.conn.cursor() as cursor:
            sql = "DROP TABLE IF EXISTS etlDestination"
            cursor.execute(sql)

            sql = """CREATE TABLE etlDestination(
                        id integer primary key autoincrement unique,
                        first_name VARCHAR(30),
                        last_name VARCHAR(30),
                        email VARCHAR(30), 
                        gender VARCHAR(30), 
                        city VARCHAR(30)
                    ) """
            cursor.execute(sql)




    def insertDestination(self,first_name, last_name, email, gender, city):
        with self.conn.cursor() as cursor:
            sql = "INSERT INTO etlDestination (first_name,last_name, email, gender, city) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql,[first_name, last_name, email, gender, city])
            self.conn.commit()

