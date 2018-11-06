import pymysql.cursors

class Sql:

    def __init__(self, host, user, password, db):
        self.conn = ""
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def open(self):
        self.conn = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def close(self):
        self.conn.close()