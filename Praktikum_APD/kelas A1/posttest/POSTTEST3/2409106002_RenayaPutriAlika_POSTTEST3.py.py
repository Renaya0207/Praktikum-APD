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