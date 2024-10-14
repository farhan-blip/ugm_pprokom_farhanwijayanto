jumlah_elemen = int(input("Masukkan Jumlah elemen dalam Array:"))

jumlah_array = list(range(1, jumlah_elemen+1))

print("Hasil Array:", jumlah_array)

kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))
tampilkan_kelipatan = [x for x in jumlah_array if x % kelipatan == 0]

print(f"Elemen yang merupakan keipatan dari {kelipatan} \n{tampilkan_kelipatan}")
