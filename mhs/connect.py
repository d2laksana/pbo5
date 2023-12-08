# install mysql-connector using pip
# pip install mysql-connector
import mysql.connector

class Database:
    def connect(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mahasiswa") # change this to your database name
        self.cur = self.db.cursor()
    
    def createTbl(self):
        query = '''
    Create table if not exists mahasiswa(
    NIM varchar(10) primary key,
    Nama varchar(50),
    Alamat varchar(50),
    No_Telp varchar(15)); ''' 
        self.cur.execute(query)
        self.db.commit()
    