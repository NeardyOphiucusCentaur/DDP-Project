# Program Saran Aktivitas Fisik Harian

def saran_aktivitas(waktu, preferensi):
    aktivitas = {
        "ringan": ["jalan santai 30 menit", "yoga 15 menit", "stretching ringan"],
        "sedang": ["lari kecil 20 menit", "bersepeda 30 menit", "senam aerobik 25 menit"],
        "berat": ["lari cepat 15 menit", "angkat beban 30 menit", "HIIT 20 menit"]
    }

    if waktu < 15:
        return "Coba lakukan stretching ringan selama 5-10 menit untuk menjaga kebugaran."
    elif 15 <= waktu <= 30:
        return f"Rekomendasi aktivitas {preferensi}: {', '.join(aktivitas[preferensi][:2])}."
    else:
        return f"Anda punya waktu lebih dari 30 menit, coba {', '.join(aktivitas[preferensi])}!"

# Input dari pengguna
print("Selamat datang di Program Saran Aktivitas Harian!")
waktu_tersedia = int(input("Berapa menit waktu yang Anda miliki untuk olahraga hari ini? "))
preferensi_aktivitas = input("Pilih tingkat intensitas (ringan/sedang/berat): ").lower()

# Output saran
saran = saran_aktivitas(waktu_tersedia, preferensi_aktivitas)
print(saran)