def hitung_rata_rata():
    jumlah_data = int(input("Masukkan jumlah data: "))
    total_data = 0
    for i in range(jumlah_data):
        data = float(input(f"Masukkan data ke-{i+1}: "))
        total_data += data
    rata_rata = total_data / jumlah_data
    
    print(f"Rata-rata dari {jumlah_data} data adalah: {rata_rata}")
hitung_rata_rata()