buku = []

def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s"  %(indeks, buku[indeks]))

def insert_data():
    buku_baru =  input("Masukkan judul buku: ")
    buku.append(buku_baru)

def edit_data():
    show_data()
    indeks =  int(input("Masukkan indeks buku yang ingin diedit: "))
    if(indeks > len(buku)):
        print("Indeks buku tidak ada")
    else:
        buku_baru = input("Masukkan judul buku baru: ")
        buku[indeks] = buku_baru

def delete_data():
    show_data()
    indeks = int(input("Masukkan  indeks buku yang ingin dihapus: "))
    if indeks > len(buku):
        print("Indeks buku tidak ada")
    else:
        buku.remove(buku[indeks])
        print("Buku berhasil dihapus")

def show_menu():
    print("\n")
    print("--------- Aplikasi Buku --------")
    print("1. Tampilkan Data Buku")
    print("2. Tambah Data Buku")
    print("3. Edit Data Buku")
    print("4. Hapus Data Buku")
    print("5. Keluar Aplikasi")
    menu = input("Pilih menu:")
    print("\n")
    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        print("Terima kasih telah menggunakan aplikasi buku")
        exit()
    else:
        print("Menu tidak ada")

if  __name__ == "__main__":
    while True:
        show_menu()