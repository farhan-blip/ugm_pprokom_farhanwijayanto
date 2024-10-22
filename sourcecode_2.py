matriks = [[0, 0, 0], [0, 0, 0]]
for i in range(2):
    for j in range(3):
        nilai = int(input(f"Masukan nilai untuk matriks[{i}][{j}]: "))
        matriks[i][j] = nilai

print("Matriks yang telah diisi:")
for baris in matriks:
    print(baris)