#mengelola overriding dan overloading
from testoverloading import Pegawai
from testoverloading import Pegawai_Kontrak
from testoverloading import Pegawai_Tetap
import os
from db import Database
import pickle

db = Database('localhost','root', '','pegawai')
db.connect()
db.createTbl()

print('Imput data pegawai berhenti isi NIK dengan XXXX')

while(True):
    os.system("cls")
    print('Menu ')
    print('1. Input pegawai tetap')
    print('2. Input pegawai kontrak')
    print('3. Cetak Pegawai tetap')
    print('4. Cetak pegawai kontrak')
    print('5. Update data pegawai tetap')
    print('6. Update data pegawai kontrak')
    print('7. Delete data pegawai tetap')
    print('8. Delete data pegawai kontrak')
    print('0. Selesai')
    pilih=int(input('Pilih menu :'))
    if(pilih==1):
        a=str(input('Masukkan NIK pegawai  : '))
        if(a!='XXXX'):
            b=str(input('Masukkan nama pegawai : '))
            c=int(input('Masukkan gaji Rp      : '))
            d=int(input('Masa Kerja (th)     :'))
            e=int(input('Jumlah lembur (hari) :'))
            ya1=str(input('Apakah anda berkeluarga <y/t>? '))
            if(ya1=='y'):
                ya2=str(input('Apakah anda memiliki anak<y/t> ? '))
                if(ya2=='y'):
                    tunj_istri=250000
                    tunj_anak=100000
                else:
                    tunj_anak=None
                    tunj_istri=250000
            else:#ya1!='y'
                ya3=str(input('apakah anda memiliki anak<y/t>?'))
                if(ya3=='y'):#punya anak tapi tidak berkeluarga
                    tunj_istri=0
                    tunj_anak=100000
                else:
                    tunj_anak=None
                    tunj_istri=None
            #masukkan tunjangan pegawai ke atribut
            peg=Pegawai_Tetap(a,b,c,d,e,0)
            x=peg.tunjangan_pegawai(tunj_istri,tunj_anak)#overloading
            peg.tunjangan=x
            db.insert('pegawai_tetap', pickle.dumps(peg))
        else:
            print('Input pegawai tetap selesai')
    elif(pilih==2):
        a=str(input('Masukkan NIK pegawai  : '))
        if(a!='XXXX'):
            b=str(input('Masukkan nama pegawai : '))
            c=int(input('Masukkan gaji Rp      : '))
            d=int(input('durasi kontrak : '))
            e=int(input('Jumlah lembur (hari) :'))
            peg=Pegawai_Kontrak(a,b,c,d,e)
            db.insert('pegawai_kontrak', pickle.dumps(peg))
        else:
            print('Input Selesai')
    elif(pilih==3):
    #cetak pegawai tetep
        print('Cetak Pegawai Tetap')
        data = db.select('pegawai_tetap')
        i=1
        for y in data:
            print('pegawai ke ',i)
            x = pickle.loads(y[1])
            x.tampilkan_pegawai_tetap()
            x.cetak_lembur()
            i+=1
            print('tekan enter -->')
            os.system("pause")
        print('Jumlah Pegawai Tetap ',len(data))
    elif(pilih==4):
        print('Cetak pegawai kontrak')  #overloading tanpa tunjangan
        data = db.select('pegawai_kontrak')
        i=1
        for y in data:
            print('pegawai ke ',i)
            x = pickle.loads(y[1])
            x.tampilkan_pegawai_kontrak()
            x.tunjangan_pegawai()
            x.cetak_lembur()
            i+=1
            print('tekan enter -->')
            os.system("pause")
        print('Jumlah Pegawai kontrak ',len(data))
    elif(pilih==5):
        print('Update data pegawai tetap')
        nik=str(input('Masukkan NIK pegawai yang akan di update : '))
        data = db.select('pegawai_tetap')
        for x in data:
            d = pickle.loads(x[1])
            if nik == d.NIK:
                print('Data ditemukan')
                d.nama = str(input('Masukkan nama pegawai : '))
                d.gaji = int(input('Masukkan gaji Rp      : '))
                d.masa_kerja = int(input('Masa Kerja (th)     :'))
                d.jml_lembur = int(input('Jumlah lembur (hari) :'))
                ya1=str(input('Apakah anda berkeluarga <y/t>? '))
                if(ya1=='y'):
                    ya2=str(input('Apakah anda memiliki anak<y/t> ? '))
                    if(ya2=='y'):
                        tunj_istri=250000
                        tunj_anak=100000
                    else:
                        tunj_anak=None
                        tunj_istri=250000
                else:#ya1!='y'
                    ya3=str(input('apakah anda memiliki anak<y/t>?'))
                    if(ya3=='y'):
                        tunj_istri=0
                        tunj_anak=100000
                t=d.tunjangan_pegawai(tunj_istri,tunj_anak)#overloading
                d.tunjangan=t
                db.update('pegawai_tetap', pickle.dumps(d), x[0])
                break
        else:
            print('Data tidak ditemukan')
    elif(pilih==6):
        print('Update data pegawai kontrak')
        nik=str(input('Masukkan NIK pegawai yang akan di update : '))
        data = db.select('pegawai_kontrak')
        for x in data:
            d = pickle.loads(x[1])
            if nik == d.NIK:
                print('Data ditemukan')
                d.nama = str(input('Masukkan nama pegawai : '))
                d.gaji = int(input('Masukkan gaji Rp      : '))
                d.durasi_kontrak = int(input('durasi kontrak : '))
                d.jml_lembur = int(input('Jumlah lembur (hari) :'))
                db.update('pegawai_kontrak', pickle.dumps(d), x[0])
                break
        else:
            print('Data tidak ditemukan')
    elif(pilih==7):
        print('Delete data pegawai tetap')
        nik=str(input('Masukkan NIK pegawai yang akan di delete : '))
        data = db.select('pegawai_tetap')
        for x in data:
            d = pickle.loads(x[1])
            if nik == d.NIK:
                print('Data ditemukan')
                db.delete('pegawai_tetap', x[0])
                break
        else:
            print('Data tidak ditemukan')
    elif(pilih==8):
        print('Delete data pegawai kontrak')
        nik=str(input('Masukkan NIK pegawai yang akan di delete : '))
        data = db.select('pegawai_kontrak')
        for x in data:
            d = pickle.loads(x[1])
            if nik == d.NIK:
                print('Data ditemukan')
                db.delete('pegawai_kontrak', x[0])
                break
        else:
            print('Data tidak ditemukan')

    elif(pilih==0):
        print('Terimakasih')
        break
    print('tekan enter')
    os.system("pause")