print("merhaba,sayılar; P(1. sayı, 2. sayı) şeklindedir")
print(" ")

x = input("1.sayı:")
y = input("2.sayı:")
x = int(x)
y = int(y)
sonuc = "lütfen güncellemeleri bekleyiniz"

if x > y:
    if y == 0:
        sonuc = 1
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 1:
        sonuc = x
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 2:
        sonuc = x * (x - 1)
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 3:
        sonuc = x * (x - 1) * (x - 2)
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 4:
        sonuc = x * (x - 1) * (x - 2) * (x - 3)
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 5:
        sonuc = x * (x - 1) * (x - 2) * (x - 3) * (x - 4)
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 6:
        sonuc = x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5)
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 7:
        sonuc = x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5) * (x - 6)
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 8:
        sonuc = x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5) * (x - 6) * (x - 7)
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 9:
        sonuc = (
            x
            * (x - 1)
            * (x - 2)
            * (x - 3)
            * (x - 4)
            * (x - 5)
            * (x - 6)
            * (x - 7)
            * (x - 8)
        )
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 10:
        sonuc = (
            x
            * (x - 1)
            * (x - 2)
            * (x - 3)
            * (x - 4)
            * (x - 5)
            * (x - 6)
            * (x - 7)
            * (x - 8)
            * (x - 9)
        )
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 11:
        sonuc = (
            x
            * (x - 1)
            * (x - 2)
            * (x - 3)
            * (x - 4)
            * (x - 5)
            * (x - 6)
            * (x - 7)
            * (x - 8)
            * (x - 9)
            * (x - 10)
        )
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 12:
        sonuc = (
            x
            * (x - 1)
            * (x - 2)
            * (x - 3)
            * (x - 4)
            * (x - 5)
            * (x - 6)
            * (x - 7)
            * (x - 8)
            * (x - 9)
            * (x - 10)
            * (x - 11)
        )
        sonuc = int(sonuc)
        print(sonuc)
    elif y == 13:
        sonuc = (
            x
            * (x - 1)
            * (x - 2)
            * (x - 3)
            * (x - 4)
            * (x - 5)
            * (x - 6)
            * (x - 7)
            * (x - 8)
            * (x - 9)
            * (x - 10)
            * (x - 11)
            * (x - 12)
        )
        sonuc = int(sonuc)
        print(sonuc)
else:
    print(sonuc)
