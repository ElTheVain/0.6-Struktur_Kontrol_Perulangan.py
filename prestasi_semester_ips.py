def hitung_ips():
    jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
    total_sks = 0
    total_nilai = 0
    for i in range(jumlah_mk):
        nilai = input(f"tolong Masukkan nilai mata kuliah {i+1} (A/B/C/D): ").upper()
        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            print("Nilai tidak valid, masukkan A, B, C, atau D.")
            continue 
        sks = 3 
        total_sks += sks
        total_nilai += bobot * sks
    
    if total_sks == 0:
        print("Tidak ada SKS yang dihitung.")
    else:
        ips = total_nilai / total_sks
        print(f"Prestasi Semester (IPS) Anda adalah: {ips:.2f}")
hitung_ips()
