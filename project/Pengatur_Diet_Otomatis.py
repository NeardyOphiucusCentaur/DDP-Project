import streamlit as st

# Daftar menu makanan untuk berbagai diet
menu_low_carb = {
    "Breakfast": "Telur orak-arik dengan alpukat",
    "Lunch": "Salmon panggang dengan brokoli",
    "Dinner": "Ayam panggang dengan sayuran hijau"
}

menu_high_protein = {
    "Breakfast": "Oatmeal dengan protein whey",
    "Lunch": "Dada ayam panggang dengan quinoa",
    "Dinner": "Steak dengan salad hijau"
}

menu_vegetarian = {
    "Breakfast": "Smoothie pisang dengan almond milk",
    "Lunch": "Tahu panggang dengan sayuran",
    "Dinner": "Nasi merah dengan sayuran dan tempe"
}

menu_seimbang = {
    "Breakfast": "Telur rebus dengan roti gandum",
    "Lunch": "Ayam panggang dengan nasi dan sayuran",
    "Dinner": "Ikan bakar dengan kentang dan salad"
}

# Fungsi untuk menghitung kebutuhan kalori berdasarkan berat badan
def hitung_kalori(bobot_kg):
    # Menggunakan rumus Mifflin-St Jeor untuk menghitung kebutuhan kalori (estimasi)
    kalori_per_hari = 10 * bobot_kg + 6.25 * 170 - 5 * 30 + 5  # untuk pria (ini hanya estimasi)
    return kalori_per_hari

# Fungsi untuk memilih menu diet
def rekomendasi_menu(diet, alergi):
    if alergi:
        return "Menu ini mengandung bahan yang mungkin tidak sesuai dengan alergi Anda. Periksa kembali."
    
    if diet == "low-carb":
        return menu_low_carb
    elif diet == "high-protein":
        return menu_high_protein
    elif diet == "vegetarian":
        return menu_vegetarian
    elif diet == "seimbang":
        return menu_seimbang
    else:
        return "Diet tidak dikenal. Pilih dari low-carb, high-protein, vegetarian, atau seimbang."

# Streamlit UI untuk input dan menampilkan hasil
def pengatur_diet():
    st.title("Pengatur Diet Otomatis")

    # Input pengguna
    bobot = st.number_input("Masukkan berat badan (kg):", min_value=1.0, max_value=300.0, step=0.1)
    target_kalori = st.number_input("Masukkan target kalori per hari:", min_value=500, max_value=5000, step=50)
    diet = st.selectbox("Pilih diet (low-carb, high-protein, vegetarian, seimbang):", ["low-carb", "high-protein", "vegetarian", "seimbang"])
    alergi = st.checkbox("Apakah Anda memiliki alergi atau pantangan makanan? (centang jika iya)")

    if st.button("Hitung dan Tampilkan Menu"):
        # Menghitung kebutuhan kalori
        kalori_harian = hitung_kalori(bobot)

        st.write(f"\nKebutuhan kalori Anda per hari adalah {kalori_harian:.2f} kalori.")
        st.write(f"Target kalori Anda: {target_kalori} kalori.")

        if target_kalori > kalori_harian:
            st.write("Anda perlu menambah asupan kalori.")
        elif target_kalori < kalori_harian:
            st.write("Anda perlu mengurangi asupan kalori.")
        else:
            st.write("Kebutuhan kalori Anda sudah tercapai.")

        # Menampilkan rekomendasi menu diet
        st.write("\nRekomendasi menu diet Anda adalah:")
        menu = rekomendasi_menu(diet, alergi)
        if isinstance(menu, dict):
            for waktu, makanan in menu.items():
                st.write(f"{waktu}: {makanan}")
        else:
            st.write(menu)

# Menjalankan Streamlit app
if __name__ == "__main__":
    pengatur_diet()
