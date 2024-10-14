array = []

for i in range(5):
    input_angka = float(input(f"Masukkan angka ke-{i+1}: "))
    array.append(input_angka)
    print("angka yang telah dimasukkan:", array)

jumlah_total = sum(array)

while True:
    pilihan = input(" \n1.jumlah\n2.rata-Rata \nApakah anda ingin melihat jumlah atau rata-rata? ")
    if pilihan == "jumlah":
        print("Jumlah total:", jumlah_total)
        break
    elif pilihan == "rata-rata":
        rata_rata = jumlah_total / len(array)
        print("Rata-rata: ",rata_rata)
        break
    else:
        print("Pilihan tidak sesuai. Silahkan tuliskan 'jumlah' atau 'rata-rata' ")