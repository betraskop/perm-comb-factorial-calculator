import tkinter as tk


def calculate():
    try:
        # Giriş kutularından değerleri al
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # İşlemi yap ve sonucu etikete yaz
        result = num1 + num2
        label_result.config(text="Sonuç: " + str(result))
    except ValueError:
        # Hatalı giriş durumunda hata mesajını etikete yaz
        label_result.config(text="Hatalı giriş!")


# Ana pencereyi oluştur
root = tk.Tk()
root.title("Basit Hesap Makinesi")

# Giriş kutularını oluştur
entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=2)

# Etiketleri oluştur
label_plus = tk.Label(root, text="+")
label_plus.grid(row=0, column=1)

label_equal = tk.Label(root, text="=")
label_equal.grid(row=0, column=4)

label_result = tk.Label(root, text="")
label_result.grid(row=1, columnspan=5)

# Hesapla düğmesini oluştur
button_calculate = tk.Button(root, text="Hesapla", command=calculate)
button_calculate.grid(row=1, column=3)

# Ana döngüyü başlat
root.mainloop()
