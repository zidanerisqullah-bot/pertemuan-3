sisi = int(input("masukan sisi persegi: "))
pilihan = input("pilih rumus yang ingin digunakan (luas/keliling): ")
rumus = {"luas": sisi*sisi, "keliling": 4 * sisi }
print(rumus[pilihan])