awal = int(input("Masukan saldo awal\t:"))
sisa = awal #jika tidak ada pengeluaran

while (True):
    pengeluaran = int(input("Masukan pengeluaran hari ini (-1 untuk keluar): "))
    if pengeluaran == -1:
        print("Sisa saldo =", sisa)
        break
    sisa -= pengeluaran
    if sisa <0:
        print("Saldo tidak mencukupi")
        print("Sisa saldo =", sisa + pengeluaran)
        break