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

# Nested list untuk menyimpan data hero
heroes = [['Iron Man', 'Tony Stark'], ['Doctor Strange', 'Stephen Strange'], ['Thor', 'Thor Odinson'], ['Hulk', 'Bruce Banner'], ['Captain America', 'Steve Rogers']]

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
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in users and users[username] == password:
            pengguna_sekarang = username
            print(f"Selamat datang, {username}!")

            # Menu pengguna
            while True:
                print("--- User Menu ---")
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
                        for i, hero in enumerate(heroes):
                            print(f"{i + 1}. Nama: {hero[0]}, Alias: {hero[1]}")

                elif pilih_pengguna == "2" and pengguna_sekarang == "admin":
                    nama = input("Masukkan nama hero: ")
                    alias = input("Masukkan alias hero: ")
                    heroes.append([nama, alias])
                    print("Hero berhasil ditambahkan!")

                elif pilih_pengguna == "3" and pengguna_sekarang == "admin":
                    if not heroes:
                        print("Tidak ada hero yang terdaftar.")
                    else:
                        print("Daftar hero:")
                        for i, hero in enumerate(heroes):
                            print(f"{i + 1}. Nama: {hero[0]}, Alias: {hero[1]}")
                        try:
                            index = int(input("Masukkan nomor hero yang ingin diperbarui: ")) - 1
                            if 0 <= index < len(heroes):
                                name = input("Masukkan nama baru hero: ")
                                alias = input("Masukkan alias baru hero: ")
                                heroes[index] = [name, alias]
                                print("Hero berhasil diperbarui!")
                            else:
                                print("Nomor hero tidak valid.")
                        except ValueError:
                            print("Input tidak valid. Silakan masukkan angka.")

                elif pilih_pengguna == "4" and pengguna_sekarang == "admin":
                    if not heroes:
                        print("Tidak ada hero yang terdaftar.")
                    else:
                        print("Daftar hero:")
                        for i, hero in enumerate(heroes):
                            print(f"{i + 1}. Nama: {hero[0]}, Alias: {hero[1]}")
                        try:
                            index = int(input("Masukkan nomor hero yang ingin dihapus: ")) - 1
                            if 0 <= index < len(heroes):
                                heroes.pop(index)
                                print("Hero berhasil dihapus!")
                            else:
                                print("Nomor hero tidak valid.")
                        except ValueError:
                            print("Input tidak valid. Silakan masukkan angka.")

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
