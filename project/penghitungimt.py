import streamlit as st

def hitung_imt(tinggi_cm, berat_kg):
    tinggi_m = tinggi_cm / 100  # Konversi tinggi ke meter
    imt = berat_kg / (tinggi_m ** 2)

    # Kategori IMT berdasarkan standar WHO
    if imt < 18.5:
        kategori = "Kurus"
    elif 18.5 <= imt < 24.9:
        kategori = "Normal"
    elif 25 <= imt < 29.9:
        kategori = "Overweight"
    else:
        kategori = "Obesitas"

    return imt, kategori

def berat_badan_ideal(tinggi_cm, usia, jenis_kelamin):
    if jenis_kelamin == "Pria":
        ideal = 50 + 0.9 * (tinggi_cm - 152.4)
    elif jenis_kelamin == "Wanita":
        ideal = 45.5 + 0.9 * (tinggi_cm - 152.4)
    else:
        raise ValueError("Jenis kelamin harus 'Pria' atau 'Wanita'.")
    # Penyesuaian berdasarkan usia
    if usia > 50:
        ideal *= 0.95  # Kurangi 5% untuk usia di atas 50 tahun
    return ideal

def tampilkan_grafik_imt(tinggi_cm, berat_kg):
    imt, kategori = hitung_imt(tinggi_cm, berat_kg)

    # Data untuk grafik
    kategori_labels = ["Kurus", "Normal", "Overweight", "Obesitas"]
    batas_imt = [18.5, 24.9, 29.9, 40]
    nilai_imt = [imt if imt <= batas else batas for batas in batas_imt]

    # Warna kategori
    warna = ["blue", "green", "orange", "red"]

    fig, ax = plt.subplots()
    ax.bar(kategori_labels, nilai_imt, color=warna)
    ax.axhline(imt, color='purple', linestyle='--', label=f'IMT Anda: {imt:.2f}')
    ax.set_title("Visualisasi Indeks Massa Tubuh (IMT)")
    ax.set_ylabel("Nilai IMT")
    ax.legend()
    st.pyplot(fig)

# Streamlit app
st.title("Kalkulator Indeks Massa Tubuh (IMT)")

st.sidebar.header("Input Data Anda")
tinggi = st.sidebar.number_input("Masukkan tinggi badan (cm):", min_value=50.0, max_value=250.0, step=0.1)
berat = st.sidebar.number_input("Masukkan berat badan (kg):", min_value=10.0, max_value=300.0, step=0.1)
usia = st.sidebar.number_input("Masukkan usia Anda:", min_value=1, max_value=120, step=1)
jenis_kelamin = st.sidebar.selectbox("Masukkan jenis kelamin:", ["Pria", "Wanita"])

if st.sidebar.button("Hitung"):
    imt, kategori = hitung_imt(tinggi, berat)
    st.subheader(f"Hasil IMT Anda")
    st.write(f"IMT: {imt:.2f}")
    st.write(f"Kategori: {kategori}")

    ideal = berat_badan_ideal(tinggi, usia, jenis_kelamin)
    st.subheader("Berat Badan Ideal")
    st.write(f"Berat badan ideal Anda (Devine): {ideal:.2f} kg")

    st.subheader("Grafik IMT")
    tampilkan_grafik_imt(tinggi, berat)
