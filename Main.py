from View.View_Nilai import cetak_daftar_nilai, cetak_hasil_pencarian, next
from View.Input_Nilai import input_data,Edit, Delete

while True:
    print("")
    A = input("[ (A)dd, (E)dit, (D)elete, (S)earch, (L)ist, (Q)uit ] : ")
    #QUIT PROGRAM
    if A.lower() == 'q':
        break

    #TABEL DAFTAR NILAI MAHASISWA
    elif A.lower() == 'l':
        cetak_daftar_nilai()

    #MENGINPUTKAN DATA
    elif A.lower() == 'a':
        input_data()

    #MENGEDIT DATA MAHASISWA
    elif A.lower() == 'e':
        Edit()

    #MENCARI DATA MAHASISWA
    elif A.lower() == 's':
        cetak_hasil_pencarian()

    #MENGHAPUS DATA DARI SALAH SATU MAHASISWA
    elif A.lower() == 'd':
        Delete()
    else:
        next()