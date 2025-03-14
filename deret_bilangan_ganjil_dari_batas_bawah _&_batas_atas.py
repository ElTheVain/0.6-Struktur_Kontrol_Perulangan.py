def ganjil(bawah, atas):
    langkah = -1 if bawah > atas else 1
    if bawah % 2 == 0:
        bawah += langkah
    hasil = []
    for i in range(bawah, atas + langkah, 2 * langkah):
        hasil.append(str(i))
    print("Hasil deret ganjil:", ", ".join(hasil))

bawah = int(input("Masukkan batas bawah: "))
atas = int(input("Masukkan batas atas: "))
ganjil(bawah, atas)
