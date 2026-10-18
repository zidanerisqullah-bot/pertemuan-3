sisi = int(input("masukan sisi persegi: "))
pilihan = input("pilih rumus yang ingin digunakan (luas/keliling): ")
rumus = {"luas": sisi*sisi, "keliling": 4 * sisi }
try:
    print(rumus[pilihan])
except KeyError:
    print('Oops, hanya bisa input "luas" atau "keliling". Periksa kembali input-an Anda')