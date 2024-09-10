# Deklarasi Variabel
var_nilai = 0
var_i = 1

# Perulangan FOR
for var_nilai in range(0, 10):
    print("Perulangan pertama ke", var_nilai)
    for var_i in range(1, 3):
        print("Perulangan ke", var_nilai, ",", var_i)
    # Diluar perulangan var_i, tidak perlu mengubah nilai var_nilai

# Diluar perulangan var_nilai
print("var_nilai =", var_nilai, "= 9. Bernilai False")