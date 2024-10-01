# Data login, sesuaikan nama dan password dengan data Anda
nama_pengguna = "nayul"
password_benar = "2"

# Login System
jumlah_login = 0  
batas_login = 3
login_berhasil = False

# Loop login hingga login berhasil atau melebihi batas percobaan
while jumlah_login < batas_login:
    username = input("Masukkan nama depan atau nama panggilan: ")
    password = input("Masukkan 3 digit terakhir NIM: ")

    # Validasi username dan password
    if username == nama_pengguna and password == password_benar:
        print("Login berhasil!")
        login_berhasil = True
        break
    else:
        jumlah_login += 1
        print(f"Login gagal! Percobaan ke-{jumlah_login}.")

    if jumlah_login == batas_login:
        print("Anda telah gagal login 3 kali. Program dihentikan.")
        break  

# Jika login berhasil, lanjutkan ke sistem 
while login_berhasil:
    print("Pilih Jenis Kelamin")
    print("1. Pria")
    print("2. Wanita")
    jenis_kelamin = input("Pilihan (1/2): ")

    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
    umur = int(input("Masukkan umur: "))

    if jenis_kelamin == "1":
        bmr = (10 * berat_badan) + (6.25 * tinggi_badan) - (5 * umur) + 5
    elif jenis_kelamin == "2":
        bmr = (10 * berat_badan) + (6.25 * tinggi_badan) - (5 * umur) - 161
    else:
        print("Pilihan jenis kelamin tidak valid.")
        bmr = None

    if bmr is not None:
        print("Level Aktivitas Harian")
        print("1. Aktivitas Minimal (jarang bergerak)")
        print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu)")
        print("3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)")
        aktivitas_harian = input("Pilihan (1/2/3): ")

        if aktivitas_harian == "1":
            tdee = bmr * 1.25
        elif aktivitas_harian == "2":
            tdee = bmr * 1.36
        elif aktivitas_harian == "3":
            tdee = bmr * 1.72
        else:
            print("Pilihan level aktivitas tidak valid.")
            tdee = None

        if tdee is not None:
            print(f"Kebutuhan Kalori Harian Anda (TDEE) adalah: {tdee:.2f} kalori per hari.")
    
   
    berhenti = input("Apakah Anda ingin memulai lagi? (iya/tidak): ")
    if berhenti == "tidak":
        print("Terima Kasih!")
        break