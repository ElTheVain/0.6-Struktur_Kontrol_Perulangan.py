def ganjil(bawah, atas):
    if bawah % 2 == 0:
        bawah += -1 if bawah > atas else 1
    langkah = -2 if bawah > atas else 2
    hasil = []
    while (bawah >= atas if langkah < 0 else bawah <= atas):
        hasil.append(str(bawah))
        bawah += langkah
    print("Hasil deret ganjil:", ", ".join(hasil))
bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
ganjil(bawah, atas)
