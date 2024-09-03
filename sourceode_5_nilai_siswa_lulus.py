for i in range(5):
    nama = input("Masukkan nama siswa ke-{} =".format(i+1))
    nilai = int(input("Masukan Nilai Siswa ke-{} =".format(i+1)))
    
    if nilai >= 70:
        print("Selamat Siswa Atas Nama",nama, "Lulus, Dengan Nilai", nilai)
    else:
        print("Mohon Maaf siswa atas nama",nama, "Belum memenuhi persyaratan untuk lulus, dengan Nilai",nilai)
        
        
