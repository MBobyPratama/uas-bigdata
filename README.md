# Analisis Temporal Tren Review dan Pola Perilaku Konsumen di Tokopedia (2015–2025)

Proyek ini adalah tugas praktikum Big Data (Kelompok 2) yang menganalisis tren ulasan, perilaku konsumen, pemodelan analisis faktor kepuasan konsumen (Harbolnas), klasifikasi sentimen ulasan menggunakan SVM, serta peramalan volume ulasan menggunakan FB Prophet. Dashboard visualisasi interaktif dibangun menggunakan Streamlit.

🌐 **Live Demo Dashboard:** [uas-bigdata-kel2.streamlit.app](https://uas-bigdata-kel2.streamlit.app/)

## 👥 Anggota Kelompok 2
1. **[Nama Anggota 1]** - [NIM]
2. **[Nama Anggota 2]** - [NIM]
3. **[Nama Anggota 3]** - [NIM]
4. **[Nama Anggota 4]** - [NIM]

---

## 📁 Struktur Proyek

```text
uas/
├── big_data_kelompok_2.py          # Script Python asli hasil ekspor Google Colab
├── big_data_kelompok_2_local.py    # Script lokal bersih untuk preprocessing, EDA, & Modeling
├── app.py                          # Kode dashboard interaktif Streamlit
├── requirements.txt                # Daftar pustaka dependensi Python
├── README.md                       # Dokumentasi petunjuk penggunaan
├── tokopedia_product_reviews_2025.csv # Dataset ulasan mentah (Raw Data)
└── clean_tokopedia_reviews.csv     # Dataset ulasan bersih hasil preprocessing (Clean Data)
```

---

## 🛠️ Persyaratan & Instalasi

Pastikan komputer Anda sudah terinstal **Python 3.8+**. Pustaka yang dibutuhkan dapat diinstal dengan perintah berikut:

```bash
pip install -r requirements.txt
```

*Catatan: Jika ingin menjalankan analisis model lengkap (`big_data_kelompok_2_local.py`), Anda juga perlu menginstal pustaka modeling berikut:*
```bash
pip install matplotlib seaborn scikit-learn scipy imbalanced-learn prophet
```

---

## 🚀 Cara Menjalankan Proyek

### 1. Menjalankan Pipeline Analisis & Preprocessing
Gunakan script ini untuk membaca raw data, melakukan cleaning, menjalankan analisis statistik korelasi & Mann-Whitney, melatih model klasifikasi sentimen SVM, melakukan forecasting volume ulasan dengan Prophet, serta mengekspor hasil dataset bersih (`clean_tokopedia_reviews.csv`):

```bash
python big_data_kelompok_2_local.py
```

### 2. Menjalankan Dashboard Streamlit
Dashboard interaktif dapat dijalankan menggunakan perintah:

```bash
python -m streamlit run app.py
```

Setelah dijalankan, buka alamat `http://localhost:8501` di browser Anda untuk melihat visualisasinya.
