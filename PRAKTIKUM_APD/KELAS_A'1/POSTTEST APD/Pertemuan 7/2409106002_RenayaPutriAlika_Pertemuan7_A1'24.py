# def salam(salam):
#     print(salam)
    # print("selamat datang mahasiswa baru 2024")   
    # print(iso)

# iso = "salam iso"
# salam(iso)

# sisi = 2
# luas = sisi * sisi

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def luas_persegi2(sisi):
#     luas = sisi * sisi
#     return luas

# luas = luas_persegi(2)
# print(luas)

# membuat variabel lokal
# def info():
#     nama = "informatika"
#     mata_kuliah = "pengantar teknik elektro"
    # mengakses variabel lokal
    # print("Prodi:", Nama)
    # print("Mata kuliah:", Mata_kuliah)

# def info2():
#     print("Prodi:", Nama)
#     print("Mata kuliah:", Mata_kuliah)

# mengakses variabel global
# print("prodi:", Nama)
# print("Mata kuliah:", Mata_kuliah)
# memanggil fungsi info
# info()
# info2()

# buku()

# def show_data():
#     if len(buku) <= 0:
#         print ("belum ada data")
#     else:
#         print("ID", "nama buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])

# def insert_data():
#     buku_baru = input("judul buku : ")
#     buku.append(buku_baru)

# def edit_data():
#     show_data()
#     indeks = int(input("masukkan ID buku: "))
#     if indeks >= len(buku) or indeks < 0 :
#         print("ID salah")
#     else :
#         judul_baru = input("masukkan judul baru buku: ")
#         buku[indeks] = judul_baru

# def delete_data():
#     show_data()
#     indeks = int(input("masukkan ID buku: "))
#     if indeks >= len(buku) or indeks < 0:
#         print("ID salah")
#     else:
#         buku.remove(buku(indeks))

# def show_menu():
#     print("menu")
#     print("1. read")
#     print("2. create")
#     print("3. update")
#     print("4. delete")
#     pilihan = int(input("masukkan pilihan : "))
#     if pilihan == 1:
#         show_data()
#     elif pilihan == 2:
#         insert_data()
#     elif pilihan == 3:
#         edit_data()
#     elif pilihan == 4:
#         delete_data()
#     else:
#         print("pilihan tidak valid")


# while(True):
#     show_menu()

# def luas_segitiga():
#     alas = float(input("masukkan alas segitiga: "))
#     tinggi = float(input("masukkan tinggi segitiga: "))
#     luas = 0.5*alas*tinggi
#     return luas
# luas = luas_segitiga()
# print (luas)


def luas_persegi():
    panjang = int(input('masukkan panjang : '))
    lebar = int(input('masukkan lebar : '))
    luas = panjang * lebar
    return luas

print(luas_persegi_panjang)