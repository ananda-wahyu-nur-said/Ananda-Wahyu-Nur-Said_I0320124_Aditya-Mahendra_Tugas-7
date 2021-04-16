pembuka = "ini adalah soal nomor satu di penugasan 7"
x = pembuka.center(80 , '-')
print(x)

def fungsistring(kalimat) :
    print("\nKalimat mula-mula nya : ", kalimat)
    print("\n(",kalimat,") kemudian saat diberikan fungsi capitalize menjadi")
    y = kalimat.capitalize()
    print(y)
    print("\n(",kalimat,") kemudian saat diberikan fungsi endswith menjadi")
    print(kalimat.endswith('sayang'))
    print("\n(",kalimat,") kemudian saat diberi fungsi upper dan lower menjadi")
    u = kata.upper()
    l = kata.lower()
    print(u)
    print(l)
kalimat_anda = input('Masukkanlah kalimat yang ingin anda olah :')
fungsistring(kalimat_anda)