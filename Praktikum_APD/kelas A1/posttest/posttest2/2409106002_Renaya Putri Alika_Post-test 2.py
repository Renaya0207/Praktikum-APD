nama_lengkap = input("nama lengkap: ")
nama_panggilan = input("nama panggilan: ")
tempat_lahir = input("tempat lahir: ")
tanggal_lahir = input("tanggal lahir (format: dd-mm-yyyy): ")
asal_sekolah = input("asal sekolah: ")
nim = int(input("NIM: "))
prodi = input("program studi: ")
umur = int(input("umur: "))
hobi = input("hobi: ")
alasan_masuk = input("alasan masuk: ")
nomor_wa = input("nomor WhatsApp: ")
tinggi_badan = float(input("tinggi badan (dalam cm): "))
berat_badan = float(input("Masukkan berat badan (dalam kg): "))

print(f"\nNama lengkap saya {nama_lengkap}, biasa dipanggil {nama_panggilan}.")
print(f"Saya lahir di {tempat_lahir} pada tanggal {tanggal_lahir}.")
print(f"Saya berasal dari sekolah {asal_sekolah}.")
print(f"Saat ini saya berkuliah di program studi {prodi} dengan NIM {nim}.")
print(f"Saya berusia {umur} tahun dan hobi saya adalah {hobi}.")
print(f"Alasan saya memilih masuk ke program studi ini adalah {alasan_masuk}.")
print(f"Nomor WhatsApp saya adalah {nomor_wa}.")
print(f"Tinggi badan saya adalah {tinggi_badan} cm dan berat badan saya {berat_badan} kg.")

nim_3_digit_terakhir = nim % 1000
hasil_modulus = nim_3_digit_terakhir % 6

print(f"Tiga angka terakhir dari NIM saya adalah {nim_3_digit_terakhir} dan jika dimoduluskan dengan 6, hasilnya adalah {hasil_modulus}.")
