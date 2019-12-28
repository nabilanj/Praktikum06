from Model.Daftar_Nilai import Data
def next () :
    print (" Pilihlah Menu Yang Tersedia.......")
def cetak_daftar_nilai () :
    print()
    print("                     DAFTAR NILAI MAHASISWA                       ")
    print("==================================================================")
    print("| NO |     NAMA    |    NIM    | TUGAS | UTS | UAS | NILAI AKHIR |")
    print("==================================================================")
    if Data.keys() :
        i = 0
        for x in Data.values():
            i += 1
            print("| {0:2} |  {1:10} | {2:9} | {3:5} | {4:3} | {5:3} |{6:12} |"\
                  .format(i,x[0], x[1], x[2], x[3], x[4], x[5]))
    else :
        print("|                   TIDAK ADA DATA MAHASISWA                     |")
        print("==================================================================")




def cetak_hasil_pencarian () :
    from View.Input_Nilai import Search
    Search()
