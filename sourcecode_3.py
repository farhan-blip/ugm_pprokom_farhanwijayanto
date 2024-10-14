array = [4, 5, 11, 12, 16, 16, 19]
bilangan_prima = []

for a in array:
    if a <= 1:
        continue
    if_prima = True
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            if_prima = False
            break
    if if_prima:
            bilangan_prima.append(a)

jumlah_prima = len(bilangan_prima)

print("Array asli:", array)
print("Bilangan prima:", bilangan_prima)
print("Jumlah bilangan prima:", jumlah_prima)