print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
Angka1 = eval(input("Masukkan angka pertama: "))
Angka2 = eval(input("Masukkan angka kedua: "))
Pilih = input("Pilihan Anda: ")

if Pilih == "1":
    Tambah= Angka1+Angka2
    print (f"hasil: {Tambah}")
elif Pilih == "2":
    Kurang= Angka1-Angka2
    print (f"hasil: {Kurang}")
elif Pilih == "3":
    Kali= Angka1*Angka2
    print (f"hasil: {Kali}")
elif Pilih == "4":
    Bagi= Angka1/Angka2
    print (f"hasil: {Bagi}")
    

