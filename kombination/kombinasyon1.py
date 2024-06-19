dongu = 1

print("Merhaba, sayılar; C(1. sayı, 2. sayı) şeklindedir")

while dongu < 5:
    print(" ")

    x = input("1. sayı:")
    y = input("2. sayı:")
    x = int(x)
    y = int(y)
    sonuc = "Lütfen güncellemeleri bekleyiniz"
    sonuc2 = 1

    if x > y:
        if y == 0:
            sonuc = 1
        else:
            sonuc = 1
            for i in range(1, y + 1):
                sonuc *= x
                x -= 1
    else:
        sonuc = "Lütfen, 1. sayının 2. sayıdan büyük olduğundan emin olun."

    if y >= 0:
        for i in range(1, y + 1):
            sonuc2 *= y
            y -= 1

    else:
        print("olmaz böyle şey")
        sonuc2 = " "

    print(int(sonuc) / int(sonuc2))
