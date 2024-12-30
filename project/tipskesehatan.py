# Program Tips Kesehatan Berdasarkan Kategori IMT

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
        return "Overweight"
    else:
        return "Obesitas"

def tips_kesehatan(kategori):
    """Memberikan tips kesehatan dan olahraga sesuai kategori IMT."""
    tips = {
        "Kurus": (
            "Fokus pada makanan tinggi kalori sehat seperti alpukat, kacang-kacangan, "
            "dan susu. Lakukan olahraga kekuatan seperti angkat beban untuk membangun otot."
        ),
        "Normal": (
            "Pertahankan pola hidup sehat dengan olahraga teratur seperti jogging, bersepeda, "
            "atau berenang. Konsumsi makanan seimbang dan hindari stres."
        ),
        "Overweight": (
            "Cobalah olahraga ringan seperti jalan cepat, yoga, atau berenang. "
            "Kurangi makanan berlemak dan gula, serta perbanyak konsumsi sayuran dan buah."
        ),
        "Obesitas": (
            "Fokus pada olahraga intensitas rendah seperti jalan kaki, berenang, atau latihan pernapasan. "
            "Konsultasikan pola makan rendah kalori dengan ahli gizi."
        ),
    }
    return tips[kategori]

# Input dari pengguna
print("Selamat datang di Program Tips Kesehatan Berdasarkan IMT!")
berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))

# Perhitungan dan rekomendasi
imt = hitung_imt(berat_badan, tinggi_badan)
kategori = kategori_imt(imt)
tips = tips_kesehatan(kategori)

# Output hasil
print("\nHasil Perhitungan:")
print(f"IMT Anda: {imt:.2f}")
print(f"Kategori IMT: {kategori}\n")

print("Tips Kesehatan:")
print(tips)
