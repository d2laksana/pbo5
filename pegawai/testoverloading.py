class Pegawai:
    def __init__(self, NIK,nama,gaji,jml_lembur):
        self.NIK=NIK
        self.nama=nama
        self.gaji=gaji
        self.jml_lembur=jml_lembur
       
    def tampilkanJumlah(self):
        print('Total Pegawai adalah ',Pegawai.jumlah)

    def tampilkan_pegawai(self):
        print('NIK           :',self.NIK)
        print('Nama Pegawai  : ',self.nama)
        print('Gaji          : Rp ',self.gaji)
        print('Jumlah lembur : ',self.jml_lembur)

    def hitung_lembur(self,hari):#akan di overriding
        return hari*20000
    
    def cetak_lembur(self):
        x=self.hitung_lembur(self.jml_lembur)
        print('Pendapatan Lembur adalah Rp ',x)

class Pegawai_Tetap(Pegawai):
    jumlah_tetap=0
    def __init__(self, NIK,nama,gaji,masa_kerja,jml_lembur,tunjangan):
        super().__init__(NIK,nama,gaji,jml_lembur)
        self.masa_kerja=masa_kerja
        self.tunjangan=tunjangan
        Pegawai_Tetap.jumlah_tetap+=1
    
    def tampilkan_pegawai_tetap(self):
        self.tampilkan_pegawai()
        print('Masa Kerja: ',self.masa_kerja,' tahun')
        print('Tunjangan : Rp ',self.tunjangan)
                      
    def tunjangan_pegawai(self,istri=None,anak=None):#overloading
        if(anak!=None) and (istri!=None):
            total=anak+istri
            print('Tunjangan anak+suami/istri = Rp ',total)
        elif(istri!=None) and (anak==None):
            total=istri
            print('Tunjangan suami/istri = Rp ',total)
        elif(anak!=None) and (istri==None):
            total=anak
            print('Tunjangan anak = Rp ',total)
        else:
            total=0
            print('Anda belum berkeluarga dan tidak mendapat tunjangan')
        return total

    def hitung_lembur(self,hari):#overriding
        if hari>20:
            return 20*300000
        elif hari>10:
            return hari*30000
        elif hari<=0:
            return 0
        else:
            return hari*20000
         
    def tampilkanJumlah(self):#overloading
        print('Total Pegawai adalah ',Pegawai_Tetap.jumlah_tetap)
    
    
class Pegawai_Kontrak(Pegawai):
    jumlah_kontrak=0
    def __init__(self,NIK,nama,gaji,durasi_kontrak,jml_lembur):
        super().__init__(NIK,nama,gaji,jml_lembur)
        self.durasi_kontrak=durasi_kontrak
        Pegawai_Kontrak.jumlah_kontrak+=1

    def tampilkan_pegawai_kontrak(self):
        self.tampilkan_pegawai()
        print('durasi kontrak : ',self.durasi_kontrak,' bulan')
           
    def tunjangan_pegawai(self):#overloading
        total=0
        print('pegawai kontrak tidak mendapat tunjangan')
    
    def hitung_lembur(self,hari):#hitung lembur overriding
        if hari>10:
            return 10*15000
        elif hari<=0:
            return 0    
        else:
            return hari*15000
       
    def tampilkanJumlah(self):#overloading
        print('Total Pegawai adalah ',Pegawai_Kontrak.jumlah_kontrak)