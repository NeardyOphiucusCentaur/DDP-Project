import streamlit as st
import datetime

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
    nilai_imt = [18.5, 24.9, 29.9, imt] if imt > 29.9 else [imt if imt <= batas else batas for batas in batas_imt]

    warna = ["blue", "green", "orange", "red"]

    st.write("### Visualisasi IMT")
    for label, nilai, warna in zip(kategori_labels, nilai_imt, warna):
        st.write(f"{label}: **{nilai:.2f}**", unsafe_allow_html=True)
        st.progress(int((nilai / max(batas_imt)) * 100))

def main():
    st.title("IdealFit - Penghitung IMT dan Berat Badan Ideal")

    menu = ["Penghitung IMT", "Fitur Premium"]
    choice = st.sidebar.selectbox("Pilih Fitur", menu)

    if choice == "Penghitung IMT":
        tinggi = st.number_input("Masukkan tinggi badan (cm):", min_value=50.0, max_value=250.0, step=0.1)
        berat = st.number_input("Masukkan berat badan (kg):", min_value=10.0, max_value=300.0, step=0.1)
        usia = st.number_input("Masukkan usia Anda:", min_value=1, max_value=120, step=1)
        jenis_kelamin = st.selectbox("Masukkan jenis kelamin:", ["Pria", "Wanita"])

        if st.button("Hitung"):
            imt, kategori = hitung_imt(tinggi, berat)
            st.subheader(f"Hasil IMT Anda")
            st.write(f"IMT: {imt:.2f}")
            st.write(f"Kategori: {kategori}")

            ideal = berat_badan_ideal(tinggi, usia, jenis_kelamin)
            st.subheader("Berat Badan Ideal")
            st.write(f"Berat badan ideal Anda (Devine): {ideal:.2f} kg")

            tampilkan_grafik_imt(tinggi, berat)

#BAGIAN FITUR PREMIUM
    elif choice == "Fitur Premium":
        def calculate_imt(weight, height):
            height_m = height / 100  # Convert height to meters
            imt = weight / (height_m ** 2)
            return imt

        def calculate_ideal_weight(height):
            return 50 + 0.9 * (height - 152.4)

        def get_imt_category(imt):
            if imt < 18.5:
                return "Kurus"
            elif 18.5 <= imt < 24.9:
                return "Normal"
            elif 25 <= imt < 29.9:
                return "Overweight"
            else:
                return "Obesitas"

        def get_diet_plan(category):
            diet_plans = {
                "Kurus": "Senin: Nasi dengan ayam goreng dan sayur \nSelasa: Roti gandum dengan telur \nRabu: Pasta dengan saus tomat dan keju \nKamis: Alpukat dan daging ikan \nJumat: Sup kacang merah dan roti \nSabtu: Smoothie pisang dan yogurt \nMinggu: Omelet dan buah segar",
                "Normal": "Senin: Nasi merah, ikan bakar, dan sayur \nSelasa: Salad dengan alpukat dan kacang \nRabu: Quinoa dengan dada ayam \nKamis: Oatmeal dengan buah \nJumat: Sup ayam dan roti gandum \nSabtu: Steak ikan dengan kentang \nMinggu: Smoothie hijau",
                "Overweight": "Senin: Sayur kukus dengan dada ayam \nSelasa: Sup sayur dan tahu \nRabu: Salad hijau dengan sedikit minyak zaitun \nKamis: Alpukat dan kacang almond \nJumat: Sup brokoli \nSabtu: Tumis jamur dan ikan panggang \nMinggu: Buah potong",
                "Obesitas": "Senin: Sup sayur tanpa minyak \nSelasa: Salad dengan kacang dan lemon \nRabu: Sayur panggang \nKamis: Oatmeal tanpa gula \nJumat: Sup wortel \nSabtu: Buah segar dan teh hijau \nMinggu: Sayur tumis ringan"
            }
            return diet_plans.get(category, "Rencana diet tidak tersedia.")

        def track_weight_progress():
            st.subheader("Monitor Berat Badan")
            if "weight_progress" not in st.session_state:
                st.session_state.weight_progress = []

            current_weight = st.number_input("Masukkan berat badan Anda saat ini (kg):", min_value=30, max_value=200, step=1)
            date = st.date_input("Tanggal:", datetime.date.today())

            if current_weight <= 0:
                st.error("Berat badan harus lebih dari 0!")
            elif st.button("Simpan Berat Badan"):
                st.session_state.weight_progress.append((str(date), current_weight))
                st.success("Berat badan berhasil disimpan!")

            if st.session_state.weight_progress:
                st.write("### Grafik Perubahan Berat Badan")
                dates = [entry[0] for entry in st.session_state.weight_progress]
                weights = [entry[1] for entry in st.session_state.weight_progress]
                st.write("Tanggal", "|", "Berat Badan (kg)")
                st.write("---")
                for date, weight in zip(dates, weights):
                    st.write(date, "|", weight)
                st.line_chart(weights)


        def set_reminders():
            st.subheader("Pengingat Harian")
            exercise_time = st.time_input("Pilih waktu untuk pengingat olahraga:", datetime.time(7, 0))
            hydration_time = st.time_input("Pilih waktu untuk pengingat hidrasi:", datetime.time(9, 0))
            st.write(f"Pengingat olahraga diatur pukul {exercise_time}.")
            st.write(f"Pengingat hidrasi diatur pukul {hydration_time}.")
            if st.button("Simpan Pengingat"):
                st.success("Pengingat harian berhasil disimpan!")

        def consult_nutritionist():
            st.subheader("Konsultasi Online dengan Ahli Gizi")
            st.write("Silakan isi form berikut untuk mengatur jadwal konsultasi dengan ahli gizi:")
            name = st.text_input("Nama Anda:")
            email = st.text_input("Email Anda:")
            preferred_date = st.date_input("Tanggal Konsultasi:", datetime.date.today())
            preferred_time = st.time_input("Waktu Konsultasi:", datetime.time(10, 0))
            if st.button("Ajukan Konsultasi"):
                st.success(f"Konsultasi berhasil diajukan! {name}, kami akan menghubungi Anda di {email} untuk jadwal pada {preferred_date} pukul {preferred_time}.")

        def main():
            menu = ["Pengatur Diet Mingguan", "Monitoring Berat Badan", "Konsultasi Ahli Gizi", "Pengingat Harian"]
            choice = st.sidebar.selectbox("Pilih Fitur Premium", menu)

            if choice == "Pengatur Diet Mingguan":
                st.header("Pengatur Diet Mingguan")
                height = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=100, max_value=250, step=1)
                weight = st.number_input("Masukkan berat badan Anda (kg):", min_value=30, max_value=200, step=1)
                
                if height and weight:
                    st.button("Hitung")
                    imt = calculate_imt(weight, height)
                    category = get_imt_category(imt)
                    diet_plan = get_diet_plan(category)
                    st.write(f"**Kategori IMT Anda:** {category}")
                    st.write(f"**Rencana Diet Mingguan Anda:**\n{diet_plan}")

            elif choice == "Monitoring Berat Badan":
                track_weight_progress()

            elif choice == "Konsultasi Ahli Gizi":
                consult_nutritionist()

            elif choice == "Pengingat Harian":
                set_reminders()

        main()
if __name__ == "__main__":
    main()
