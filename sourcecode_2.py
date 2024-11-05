#program menghitung luas bentuk 2 dimensi

#Mencetak menu
def menu():
    print("Pilih Bentuk 2D")
    print("1. Persegi Panjang")
    print("2. Lingkaran") 
    print("3. Segitiga")
    print("4. Keluar")

def persegi():
    print("Menghitung Luas Persegi Panjang")
    p = float(int(input("Masukkan Lebar: ")))
    l = float(int(input("Masukkan Panjang: ")))
    luas = p*l
    print("Luas  Persegi Panjang: ", luas)
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def lingkaran():
    print("Menghitung Luas Lingkaran")
    r = int(input("Masukkan Jari-Jari: "))
    luas = 3.14*(r**2)
    print("Luas Lingkaran adalah", luas)
    print("Cobalagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def segitiga():
    print("Menghitung Luas Segitiga")
    a = int(input("Masukkan Alas: "))
    t = int(input("Masukkan Tinggi: "))
    luas = (a*t)/2
    print("Luas Segitiga adalah", luas)
    print("Cobalagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def main():
    while True:
        menu()
        pilihan = input("Pilih bentuk (1-4): ")
        if pilihan == '1':
            persegi()
        elif pilihan == '2':
            lingkaran()
        elif pilihan == '3':
            segitiga()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

        back = input("Coba lagi [Y/N]? ").upper()
        if back != "Y":
            print("Terima kasih telah menggunakan program ini.")
            break

if __name__ == "__main__":
    main()