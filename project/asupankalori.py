# Program Rekomendasi Asupan Kalori Harian Berdasarkan IMT

def hitung_imt(berat, tinggi):
    """Menghitung IMT berdasarkan berat (kg) dan tinggi (m)."""
    return berat / (tinggi ** 2)

def kategori_imt(imt):
    """Menentukan kategori IMT berdasarkan nilai IMT."""
    if imt < 18.5:
        return "Kurus"
    elif 18.5 <= imt <= 24.9:
        return "Normal"
    elif 25 <= imt <= 29.9:
        return "Kelebihan Berat Badan"
    else:
        return "Obesitas"

def rekomendasi_kalori(kategori, berat):
    """Memberikan rekomendasi asupan kalori harian berdasarkan kategori IMT."""
    if kategori == "Kurus":
        return f"Untuk menaikkan berat badan, disarankan mengonsumsi sekitar {35 * berat} kalori per hari."
    elif kategori == "Normal":
        return f"Untuk menjaga berat badan ideal, Anda memerlukan sekitar {30 * berat} kalori per hari."
    elif kategori == "Kelebihan Berat Badan":
        return f"Untuk menurunkan berat badan, disarankan mengonsumsi sekitar {25 * berat} kalori per hari."
    else:  # Obesitas
        return f"Untuk menurunkan berat badan secara bertahap, Anda memerlukan sekitar {20 * berat} kalori per hari."

# Input dari pengguna
print("Selamat datang di Program Rekomendasi Kalori Harian!")
berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))

# Perhitungan dan rekomendasi
imt = hitung_imt(berat_badan, tinggi_badan)
kategori = kategori_imt(imt)
rekomendasi = rekomendasi_kalori(kategori, berat_badan)

# Output hasil
print("\nHasil Perhitungan:")
print(f"IMT Anda: {imt:.2f}")
print(f"Kategori IMT: {kategori}")
print(rekomendasi)