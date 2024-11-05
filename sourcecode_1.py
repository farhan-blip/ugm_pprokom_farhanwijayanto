import math

a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
c = int(input('Masukkan c: '))

#hitung diskriminan d
d = (b**2) - (4*a*c)

#menemukan xl dan x2
if d > 0:
    xl = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print('Solusinya adalah {0} dan {1}'.format(xl, x2))
else:
    print("Tidak ada soulusi karena diskriminan negatif")