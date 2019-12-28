def input_data ():
    print(" < Tambahkan Data >")
    from Model.Daftar_Nilai import tambah_data
    while (True) :
        nama = input (" Masukkan Nama : ")
        if nama == ' ' :
            print (' Please Inputkan Nama Mahasiswa ')
        else :
            break

    while (True) :
        try:
            nim = int(input(" Masukkan NIM    : "))
            if nim == '':
                print(' Please Inputkan NIM Mahasiswa ')
        except ValueError:
            print(' Please Inputkan NIM Mahasiswa ')
        else:
            break
    while (True) :
        try:
            tugas = int(input(" Masukkan Nilai Tugas  : "))
            if tugas == '':
                print(' Please Inputkan Nilai Tugas ')
        except ValueError:
            print(' Please Inputkan Nilai Tugas ')
        else:
            break

    while (True) :
        try:
            uts = int(input(" Masukkan Nilai UTS    : "))
            if uts == '':
                print(' Please Inputkan Nilai UTS ')
        except ValueError:
            print(' Please Inputkan Nilai UTS ')
        else:
            break
    while (True):
        try:
            uas = int(input(" Masukkan Nilai UAS    : "))
            if uas == '':
                print(' Please Inputkan Nilai UAS ')
        except ValueError:
            print(' Please Inputkan Nilai UAS ')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)


def Edit ():
    from Model.Daftar_Nilai import ubah_data
    ubah_data (nama= input(" Masukkan Nama : "))


def Delete ():
    from Model.Daftar_Nilai import hapus_data
    hapus_data(nama= input(" Masukan Nama  : "))

def Search ():
    from Model.Daftar_Nilai import cari_data
    cari_data(nama= input(" Masukkan Nama : "))
