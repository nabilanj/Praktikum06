Data = {}

def tambah_data (nama, nim, tugas, uts, uas) :
    akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
    Data[nama] = nama, nim, tugas, uts, uas, akhir

def ubah_data (nama):
    if nama in Data.keys() :
        del Data[nama]
        print(" < Edit Data {0} > ".format(nama))
        from View.Input_Nilai import input_data
        input_data()
    else :
        print("                     DAFTAR NILAI MAHASISWA                       ")
        print("==================================================================")
        print("| NO |     NAMA    |    NIM    | TUGAS | UTS | UAS | NILAI AKHIR |")
        print("==================================================================")
        print("|                       DATA {0} TIDAK ADA                       |".format(nama))
        print("==================================================================")

def cari_data (nama) :
    print (" < Search Data Mahasiswa > ")
    print("                     DAFTAR NILAI MAHASISWA                  ")
    print("=============================================================")
    print("|     NAMA    |    NIM    | TUGAS | UTS | UAS | NILAI AKHIR |")
    print("=============================================================")
    if nama in Data.keys():
        print("|  {0:10} | {1:9} | {2:5} | {3:3} | {4:3} |{5:12} |"\
              .format(nama, Data[nama][1], Data[nama][2], Data[nama][3], Data[nama][4], Data[nama][5]))
        print("=============================================================")
    else:
        print("|                       DATA {0} TIDAK ADA                       |".format(nama))
        print("==================================================================")

def hapus_data (nama) :
    print(" < Delete Data Mahasiswa > ")
    if nama in Data.keys():
        del Data[nama]
        print (" Data {0} Berhasil di Hapus ".format(nama))
    else :
        print("                     DAFTAR NILAI MAHASISWA                       ")
        print("==================================================================")
        print("| NO |     NAMA    |    NIM    | TUGAS | UTS | UAS | NILAI AKHIR |")
        print("==================================================================")
        print("|                       DATA {0} TIDAK ADA                       |".format(nama))
        print("==================================================================")



