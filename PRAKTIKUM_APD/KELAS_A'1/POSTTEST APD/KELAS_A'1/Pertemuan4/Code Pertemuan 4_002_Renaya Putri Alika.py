#perulangan for
batas = 10
for i in range(1, batas, 2):
    print("Perulangan ke-"+str(i))

buah = ("apel", "mangga", "anggur")
for i in buah:
    print(i)

buah_banyak = ("apel", "mangga", "anggur")
for buah in buah_banyak:
    print(buah)

for baris in range (1,4):
    print("baris ke", baris)
    for kolom in range (1,4):
        print(kolom, "kolom", end=" ")
    print()
    print()
    
#perulangan while
lagi = "yes"
ulang = 0
while lagi == "yes":
    ulang +=1
    print("gas")
    lagi = input("mabar lagi gk? ")
print("selesai mabar")
print(f"Perulangan terjadi sebanyak : {ulang} kali")

for i in range(1,10):
    if i == 5:
        break
    else:
        print(f"Perulangan ke-{i}")

buah_banyak = ("apel", "mangga", "anggur", "semangka")
for buah in buah_banyak:
    if buah == "anggur":
        print("anggur ketemu")
        break
    else:
        print("belum ketemu")

while True:
    ulang = input("mabar lagi? ")
    if ulang == "gk":
        break
    print("mabar lagi")

for i in range(1,10):
    if i % 2 == 1:
        continue
    print(i)



#for i in range(6):
#    for i in range(6):
#        print("*", end="")
#    print()

#for i in range(6):
#    print("*", end == " ")


kesempatan = 3
while kesempatan > 0:
    username = input("masukkan username: ")
    password = input("masukkan password: ")

    if username == "admin" and password == "admin#1234":
        print("berhasil login")
        break
    else:
        print("username atau password salah")
        kesempatan -= 1
        print(f"kesempatan tersisa {kesempatan} kali")
        
print("program utama")  