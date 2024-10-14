angka = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

total_ganjil = 0
total_genap = 0

tampilkan_genap = []
tampilkan_ganjil = []

for num in angka:
    if num % 2 == 0:
        total_genap += 1
        tampilkan_genap.append(num)
    else:
        total_ganjil += 1
        tampilkan_ganjil.append(num)

print("Ini adalah angka genap:", tampilkan_genap)
print("Jumlah total angka genap:", total_genap)
print("Ini adalah angka ganjil:", tampilkan_ganjil)
print("Jumlah total angka ganjil:", total_ganjil)