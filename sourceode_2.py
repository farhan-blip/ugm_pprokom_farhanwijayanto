nilai = set({3, 6, 9, 2, 5, 7})

for i in range(1, 11):
    nilai.add(i)
print("Nilai Set Setelah penambahan:", nilai)

nilai.difference_update({1,3,4,5,7,8,10})
print("Nilai Set Setelah penghapusan:", nilai)