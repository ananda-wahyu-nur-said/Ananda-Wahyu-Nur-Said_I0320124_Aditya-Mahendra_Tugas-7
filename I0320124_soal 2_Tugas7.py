pembuka = "Selamat datang di Soal 2 Penugasan 7 tentang Fungsi Numerik"
x = pembuka.center(80 , '-')
print(x)

import math
import random

def fungsinumerik(angkapertama,angkakedua,angkaketiga):
    print('\nPenggunaan fungsi abs dan fabs')
    print(angkapertama, 'menjadi',abs(angkapertama))
    print(angkakedua, 'menjadi',abs(angkakedua))
    print(angkaketiga, 'menjadi', abs(angkaketiga))
    print(angkapertama, 'menjadi',math.fabs(angkapertama))
    print(angkakedua, 'menjadi',math.fabs(angkakedua))
    print(angkaketiga, 'menjadi', math.fabs(angkaketiga))
    print('\nPenggunaan fungsi ceil')
    print(angkapertama, 'menjadi',math.ceil(angkapertama))
    print(angkakedua, 'menjadi',math.ceil(angkaketiga))
    print(angkaketiga, 'menjadi', math.ceil(angkaketiga))
    print('\nPenggunaan fungsi floor')
    print(angkapertama, 'menjadi', math.floor(angkapertama))
    print(angkakedua, 'menjadi',math.floor(angkakedua))
    print(angkaketiga, 'menjadi', math.floor(angkaketiga))
    print('\nMencari nilai minimal dan maksimal')
    print('nilai minimal antara ketiganya adalah = ', min(angkapertama,angkakedua,angkaketiga))
    print('nilai maksimal antara ketiganya adalah = ', max(angkapertama,angkakedua,angkaketiga))
    print('\nPemilihan nilai random dengan choice')
    y = [angkapertama,angkakedua,angkaketiga]
    print('a= ', y)
    print('random pertama')
    print('choice= ', random.choice(y))
    print('random kedua')
    print('choice= ', random.choice(y))
    print('random ketiga')
    print('choice= ', random.choice(y))

print('Gunakanlah tanda titik untuk menulis desimal')
a = float(input('Masukkan angka pertama: '))
b = float(input('Masukkan angka kedua: '))
c = float(input('Masukkan angka ketiga: '))
fungsinumerik(a,b,c)