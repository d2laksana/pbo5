import mysql.connector
class Database:
    def __init__(self, host, user, passwd, database) :
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def connect(self):
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd, 
            database=self.database
        )
        self.cur = self.db.cursor()
        
    def createTbl(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS pegawai_tetap (
            id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
            data VARBINARY(65535)
            );''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS pegawai_kontrak (
            id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
            data VARBINARY(65535)
            );''')
        self.db.commit()
        
    def insert(self, column, data):
        self.cur.execute("INSERT INTO "+ column +" (data) VALUES (%s)", (data,))
        self.db.commit()

    def select(self, column):
        self.column = column
        self.cur.execute(f"SELECT * FROM {self.column}" )
        return self.cur.fetchall()
    
    def update(self, column, data, id):
        self.cur.execute("UPDATE "+ column +" SET data = %s WHERE id = %s", (data, id))
        self.db.commit()
    
    def delete(self, column, id):
        self.cur.execute("DELETE FROM "+ column +" WHERE id = %s", (id,))
        self.db.commit()

