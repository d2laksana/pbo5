class Query:
    def __init__(self, db, cur) -> None:
        self.db = db
        self.cur = cur

    def insert(self, nim, nama, alamat, no_telp):
        self.nim = nim
        self.nama = nama
        self.alamat = alamat
        self.no_telp = no_telp
        sql = f"INSERT INTO mahasiswa (nim, nama, alamat, no_telp) VALUES ('{self.nim}', '{self.nama}', '{self.alamat}', '{self.no_telp}')"
        
        self.cur.execute(sql)
        self.db.commit()


    def update(self, nim, nama, alamat, no_telp):
        self.nim = nim
        self.nama = nama
        self.alamat = alamat
        self.no_telp = no_telp

        sql = f'update mahasiswa set nama="{self.nama}", alamat="{self.alamat}", no_telp="{self.no_telp}" where nim="{self.nim}"'
        self.cur.execute(sql)
        self.db.commit()

    def delete(self, nim):
        self.nim = nim

        sql = f'delete from mahasiswa where nim={self.nim}'
        self.cur.execute(sql)
        self.db.commit()
    
    def select(self, nim):
        self.nim = nim

        sql = f'select * from mahasiswa where nim={self.nim}'
        self.cur.execute(sql)
        return self.cur.fetchall()
    
