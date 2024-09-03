import getpass

pilihan = ['batu', 'gunting', 'kertas']
pemain_1 = getpass.getpass('masukan pilihan pemain 1 (batu,gunting, kertas) = ')
pemain_2 = getpass.getpass('masukan pilihan pemain 2 (batu,gunting, kertas) = ')

print(f'Pemain 1 memilih {pemain_1} dan pemain 2 memilih {pemain_2}')

if pemain_1 == pemain_2:
    print('Seri!')
elif(pemain_1 == 'batu' and pemain_2 == 'guting'):
    print('Pemain 1 menang!')
elif(pemain_1 == 'gunting' and pemain_2 == 'kertas'):
    print("Pemain 1 Menang")
elif(pemain_1 == 'kertas' and pemain_2 == 'batu'):
    print('Pemain 1 menang!')
else:
    print('pemain 2 menang')