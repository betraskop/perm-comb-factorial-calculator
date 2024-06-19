print("Merhaba, sayılar; P(1. sayı, 2. sayı) şeklindedir")
print(" ")

x = input("1. sayı:")
y = input("2. sayı:")
x = int(x)
y = int(y)
sonuc = "Lütfen güncellemeleri bekleyiniz"

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

print(int(sonuc))
