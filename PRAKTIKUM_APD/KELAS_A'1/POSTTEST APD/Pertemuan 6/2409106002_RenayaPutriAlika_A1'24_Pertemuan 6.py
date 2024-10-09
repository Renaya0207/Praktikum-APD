#  Daftar_buku = {
#       #key        #value
#      "buku1" : "harry potter",
#      "buku2" : "percy jackson",
#      "buku3" : "twillight"
#  }

#  print(daftar_buku["buku2"])
#  print(daftar_buku["buku1"])

# biodata = {
#      "nama" : "aldy ramadhan syahputra", #string
#      "NIM" : 2109106079, #int
#      "KRS" : ["program web", "struktur data", "basis data"], #list
#      "mahasiswa_aktif" : True, #bool
#      "social media" : { #dictionary
#          "instagram" : "@aldyyyrmdhns",
#          "discord" : "\ izanami#6484"
#          }
#  }

# print("jumlah data dalam dict biodata = ", len(biodata))
# pinjamdict = biodata.copy()
# print(pinjamdict)

# key = "apel", "jeruk", "mangga"
# value = 1

# buah = dict.fromkeys(key, value)
# print(buah)

# for i, j in biodata, items():
    # print(i)
    # print(f"key = {i} dan value = {j}")

#  print(biodata["KRS"][1])
# print(biodata.get("nama"))

#  print(biodata["nama"])
# print(biodata.get("nama"))

#  print(biodata["alamat"])
# print(biodata.get("alamat"))
# print(biodata.get("alamat", "kosong bang"))

#  games + dict(sekiro = "action", pokemon = "adventure", valorant = "FPS")
#  print(games)

# film = {
#    "avengers endgame" : "action",
#    "sherlock holmes" : "mystery",
#    "the conjuring" : "horror"
# }

# print(film)
# print("film :", dilm.setdefault("oldbook", "horror"))
# print(film)

# for i in film.keys()
# print(i)

# for i in film.value():
#  print(i, end=" ")

# musik = { 
#      "the chainsmoker" : ["all we know", "paris"],
#      "alan walker" : ["alone", "lily"],
#      "neffex" : ["best of me", "memories"]
# }
# for i, j in musik.items():
#     print(f"musik milik {i} adalah : ")
#     for lagu in j:
#        print(lagu)
#     print("")

mahasiswa = {
   101 : {"nama" : "aldy", "umur" : 19},
   111 : {"nama" : "abdul", "umur" : 18}
}
print(f"sebelum : {mahasiswa}")
mahasiswa[101]["angkatan"] = 2023
print(f"sesudah : {mahasiswa}")

# print(mahasiswa)
# mahasiswa[101]["angkatan"] = 2023
# print(mahasiswa)

for i, j in mahasiswa.items():
    print(f"ID : {i}")
    # for i_a, j_a in j.items():
    #    print(f"{i_a} : {j_a}")
    for keynested, valuenested in j.items():
       print(f"{keynested} : {valuenested}")


print(film)
# del film["the conjuring"]
hapus = film.pop("the conjuring")
print(film)
print(f"item yang di hapus = {hapus}")


film["zombieland"] = "comedy" #kurung siku
film.update({"hour" : "thriller"})
print(film)