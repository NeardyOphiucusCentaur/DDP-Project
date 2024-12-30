import streamlit as st

def main():
    st.title("Diet Tracker - Versi Premium")

    menu = ["Pengatur Diet Mingguan", "Catat Berat Badan", "Grafik Perubahan Berat Badan", "Konsultasi Online", "Pengingat Harian"]
    choice = st.sidebar.selectbox("Pilih Menu", menu)

    if choice == "Pengatur Diet Mingguan":
        st.subheader("Pengatur Diet Mingguan Lengkap dengan Resep")
        recipes = {
            "Senin": "Salad Ayam",
            "Selasa": "Nasi Merah dan Tumis Sayur",
            "Rabu": "Ikan Panggang dengan Kentang",
            "Kamis": "Sup Ayam",
            "Jumat": "Tempe Orek dan Sayur Lodeh",
            "Sabtu": "Sandwich Alpukat",
            "Minggu": "Smoothie Bowl"
        }
        for day, recipe in recipes.items():
            st.write(f"{day}: {recipe}")

    elif choice == "Catat Berat Badan":
        st.subheader("Catat Berat Badan")
        weight = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0, step=0.1)
        if st.button("Simpan Berat Badan"):
            with open("weight_logs.txt", "a") as f:
                f.write(f"{weight}\n")
            st.success(f"Berat badan {weight} kg berhasil dicatat.")

    elif choice == "Grafik Perubahan Berat Badan":
        st.subheader("Grafik Perubahan Berat Badan")
        try:
            with open("weight_logs.txt", "r") as f:
                weights = [float(line.strip()) for line in f]
            st.line_chart(weights)
        except FileNotFoundError:
            st.warning("Belum ada data berat badan yang dicatat.")

    elif choice == "Konsultasi Online":
        st.subheader("Konsultasi Online dengan Ahli Gizi")
        st.write("Konsultasi sedang berlangsung... Harap tunggu.")

    elif choice == "Pengingat Harian":
        st.subheader("Pengingat Harian")
        reminders = {
            "olahraga": "Jangan lupa olahraga hari ini!",
            "hidrasi": "Minum air minimal 8 gelas hari ini!"
        }
        for key, reminder in reminders.items():
            st.write(f"- {reminder}")

if __name__ == "__main__":
    main()
