# Dictionary untuk menyimpan data hero
heroes = {
    'iron man': 'tony stark',
    'doctor strange': 'stephen strange',
    'thor': 'thor odinson',
    'hulk': 'bruce banner',
    'captain america': 'steve rogers'
}

# Data pengguna
pengguna = {
    "admin": "adminpass",
    "user": "userpass"
}

# Variabel global
pengguna_sekarang = None
max_hero = 10
hero_count = 0

# Fungsi untuk menghitung jumlah hero
def hitung_hero():
    return len(heroes)

# Fungsi rekursif untuk menampilkan hero
def tampilkan_hero_rekursif(hero_list):
    if not hero_list:
        return
    hero = hero_list[0]
    print(f"Nama: {hero}, Alias: {heroes[hero]}")
    tampilkan_hero_rekursif(hero_list[1:])

# Fungsi untuk menambahkan hero
def tambah_hero(nama, alias):
    global hero_count
    if hero_count >= max_hero:
        return "limit batas max hero."
    if nama in heroes:
        return "Hero sudah ada. Gunakan opsi perbarui untuk memperbarui hero."
    heroes[nama] = alias
    hero_count += 1
    return "Hero berhasil ditambahkan!"

# Fungsi untuk memperbarui nama dan alias hero
def perbarui_hero(nama_lama, nama_baru, alias_baru):
    if nama_lama in heroes:
        heroes[nama_baru] = alias_baru
        if nama_lama != nama_baru:
            del heroes[nama_lama]
        return "Hero berhasil diperbarui!"
    else:
        return "Hero tidak ditemukan."

# Prosedur untuk melihat daftar hero
def lihat_hero():
    if not heroes:
        print("Tidak ada hero yang terdaftar.")
    else:
        print("Daftar hero:")
        tampilkan_hero_rekursif(list(heroes.keys()))

# Prosedur untuk memeriksa akses admin
def cek_admin():
    if pengguna_sekarang != "admin":
        print("Akses ditolak! Hanya admin yang bisa mengakses fitur ini.")
        return False
    return True

# Menu utama
while True:
    print("--- Menu utama ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        if username in pengguna:
            print("Username sudah ada. Silakan coba lagi.")
        else:
            pengguna[username] = password
            print("Registrasi berhasil!")

    elif pilihan == "2":
        username = input("Masukkan username: ").lower()
        password = input("Masukkan password: ")
        if username in pengguna and pengguna[username] == password:
            pengguna_sekarang = username
            print(f"Selamat datang, {username}!")

            # Menu pengguna
            while True:
                print("--- Menu Pengguna ---")
                print("1. Lihat Hero")
                if pengguna_sekarang == "admin":
                    print("2. Tambah Hero (Admin saja)")
                    print("3. Perbarui Hero (Admin saja)")
                    print("4. Hapus Hero (Admin saja)")
                print("5. Logout")

                pilih_pengguna = input("Pilih opsi: ")

                if pilih_pengguna == "1":
                    lihat_hero()

                elif pilih_pengguna == "2" and cek_admin():
                    nama = input("Masukkan nama hero: ").lower()
                    alias = input("Masukkan alias hero: ")
                    print(tambah_hero(nama, alias))

                elif pilih_pengguna == "3" and cek_admin():
                    if not heroes:
                        print("Tidak ada hero yang terdaftar.")
                    else:
                        lihat_hero()
                        nama_lama = input("Masukkan nama hero yang ingin diperbarui: ").lower()
                        nama_baru = input("Masukkan nama baru hero: ").lower()
                        alias_baru = input("Masukkan alias baru hero: ")
                        print(perbarui_hero(nama_lama, nama_baru, alias_baru))

                elif pilih_pengguna == "4" and cek_admin():
                    if not heroes:
                        print("Tidak ada hero yang terdaftar.")
                    else:
                        lihat_hero()
                        nama = input("Masukkan nama hero yang ingin dihapus: ").lower()
                        if nama in heroes:
                            del heroes[nama]
                            hero_count -= 1
                            print(f"Hero {nama} berhasil dihapus!")
                        else:
                            print("Hero tidak ditemukan.")

                elif pilih_pengguna == "5":
                    pengguna_sekarang = None
                    print("Anda telah logout.")
                    break

                else:
                    print("Opsi tidak valid atau Anda tidak memiliki akses.")

        else:
            print("Username atau password salah.")

    elif pilihan == "3":
        print("Keluar dari program.")
        break

    else:
        print("Opsi tidak valid.")