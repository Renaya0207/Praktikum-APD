print(
"""
===========================
|     LIST HERO MARVEL    |
===========================
|   1. TAMBAH DATA HERO   |           
|   2. LIHAT HERO         |          
|   3. PERBARUI HERO      |     
|   4. HAPUS HERO         |      
|   5. KELUAR             |  
===========================
"""
)

# Dictionary untuk menyimpan data hero
heroes = {'iron man': 'tony stark', 'doctor Strange': 'stephen strange', 'thor': 'thor odinson', 'hulk': 'bruce banner', 'captain america': 'steve rogers'}

# Data pengguna
users = {"admin": "adminpass", "user": "userpass"}
pengguna_sekarang = None

# Menu utama
while True:
    print("--- Menu ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        if username in users:
            print("Username sudah ada. Silakan coba lagi.")
        else:
            users[username] = password
            print("Registrasi berhasil!")

    elif pilihan == "2":
        username = input("Masukkan username: ").lower()
        password = input("Masukkan password: ")
        if username in users and users[username] == password:
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
                    if not heroes:
                        print("Tidak ada hero yang terdaftar.")
                    else:
                        print("Daftar hero:")
                        for hero, alias in heroes.items():
                            print(f"Nama: {hero}, Alias: {alias}")

                elif pilih_pengguna == "2" and pengguna_sekarang == "admin":
                    nama = input("Masukkan nama hero: ")
                    alias = input("Masukkan alias hero: ")
                    if nama in heroes:
                        print("Hero sudah ada. Gunakan opsi perbarui untuk memperbarui hero.")
                    else:
                        heroes[nama] = alias
                        print("Hero berhasil ditambahkan!")

                elif pilih_pengguna == "3" and pengguna_sekarang == "admin":
                    if not heroes:
                        print("Tidak ada hero yang terdaftar.")
                    else:
                        print("Daftar hero:")
                        # Tampilkan hero yang terdaftar
                        for hero, alias in heroes.items():
                            print(f"Nama: {hero}, Alias: {alias}")
                        
                        # Meminta pengguna memasukkan nama hero yang ingin diperbarui
                        nama = input("Masukkan nama hero yang ingin diperbarui: ")
                        
                        # Jika nama hero ditemukan dalam dictionary heroes
                        if nama in heroes:
                            alias_baru = input("Masukkan alias baru hero: ")
                            heroes[nama] = alias_baru  # Perbarui alias
                            print("Hero berhasil diperbarui!")
                        else:
                            print("Hero tidak ditemukan.")

                elif pilih_pengguna == "4" and pengguna_sekarang == "admin":
                    if not heroes:
                        print("Tidak ada hero yang terdaftar.")
                    else:
                        print("Daftar hero:")
                        # Menampilkan daftar hero yang ada
                        for hero, alias in heroes.items():
                            print(f"Nama: {hero}, Alias: {alias}")
                            
                        # Meminta admin untuk memasukkan nama hero yang ingin dihapus
                        nama = input("Masukkan nama hero yang ingin dihapus: ")
                        
                        # Validasi apakah hero ada dalam dictionary
                        if nama in heroes:
                            del heroes[nama]  # Menghapus hero dari dictionary
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
