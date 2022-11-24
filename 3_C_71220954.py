Daftar = input("Masukkan daftar pesanan : ")
pesanan = Daftar.split(',',4)
print (f"Daftar pesanan : {pesanan}")
Tambahan = input("Masukkan pesanan yang ingin ditambahkan : ")
pesanan.append(Tambahan)
print(f"Hasil penambahan pada daftar pesanan : {pesanan}")


