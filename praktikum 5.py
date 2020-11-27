print("========Program Input Nilai =========")
data={}
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if c.lower() == 'k':
        print("Keluar Program")
        break

    elif c.lower() == 'l':
        if data.items():
            print("Daftar Nilai Mahasiswa")
            print("================================================================================================")
            print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
            print("================================================================================================")
            i=0
            for x in data.items():
                i+=1
                print(" | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |"
                      .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("================================================================================================")
        else:
            print("Daftar Nilai Mahasiswa")
            print("================================================================================================")
            print("| NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
            print("================================================================================================")
            print("|                                      TIDAK ADA DATA                                         |")
            print("================================================================================================")

    elif c.lower() == 't':
        print("=======Tambah Data=======")
        nama    =input("Nama                :  ")
        nim     =input("NIM                 :  ")
        tugas   =int(input("Masukan nilai tugas :  "))
        uts     =int(input("Masukan nilai uts   :  "))
        uas     =int(input("Masukan nilai uas   :  "))
        akhir   = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir
        print("=========================")

    elif c.lower() == 'u':
        print('=======Ubah Data Mahasiswa=======')
        nama = input('Nama                :  ')
        if nama in data.keys():
            nim     =input('NIM                 :  ')
            tugas   =int(input("Masukan nilai tugas baru:  "))
            uts     =int(input("Masukan nilai uts baru  :  "))
            uas     =int(input("Masukan nilai uas baru  :  "))
            akhir   =(0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
            print("Data berhasil di update!")
        else:
            print("Data Nilai Tidak Ada".format(nama))
        print("=================================")

    elif c.lower() == 'h':
        print("====Hapus Data Mahasiswa====")
        nama=input("Nama :  ")
        if nama in data.keys():
            del data[nama]
            print("Data telah dihapus!")
        else:
            print("Data Nilai Tidak Ada".format(nama))
        print("============================")

    elif c.lower() == 'c':
        print("===Cari Data mahasiswa===")
        nama=input("Masukan Nama :  ")
        if nama in data.keys():
            print("Daftar Nilai Mahasiswa")
            print("======================================================================================")
            print(" |     NAMA      |    NIM     |    TUGAS    |     UTS     |     UAS     |  AKHIR   | ")
            print("======================================================================================")
            print(" | {0:12s}  | {1:10} | {2:11d} | {3:11d} | {4:11d} | {5:8.2f} |"\
                   .format(nama, nim, tugas, uts, uas, akhir))
            print("======================================================================================")
        else:
            print("Data {0} Tidak tersedia ".format(nama))

    else:
        print(" === Pilih Sesuai Menu Yang Tersedia === ")