dongu = 1

print("Merhaba, faktoriyel hesaplama")

while dongu < 5:
    print(" ")

    x = input("faktoriyeli hesaplanacak sayı:")

    x = int(x)
    sonuc = 1

    if x >= 0:
        for i in range(1, x + 1):
            sonuc *= x
            x -= 1

    else:
        print("olmaz böyle şey")
        sonuc = " "

    print(sonuc)
