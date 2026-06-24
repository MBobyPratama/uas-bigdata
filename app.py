import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman & Tema
st.set_page_config(
    page_title="Tokopedia Consumer Insight Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk mempercantik tampilan kartu indikator agar support Dark & Light Mode
st.markdown("""
    <style>
    .metric-box {
        background-color: var(--secondary-background-color);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    .metric-box h5 {
        color: var(--text-color);
        margin: 0 0 5px 0;
        font-size: 0.95rem;
        opacity: 0.85;
    }
    .metric-box h2 {
        color: var(--text-color);
        margin: 0 0 5px 0;
        font-size: 1.8rem;
        font-weight: 700;
    }
    .metric-box p {
        margin: 0;
        font-size: 0.85rem;
    }
    .text-muted {
        color: #888888 !important;
    }
    .text-success {
        color: #2ecc71 !important;
    }
    .text-info {
        color: #3498db !important;
    }
    .text-purple {
        color: #9b59b6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Memuat Data dari Session Storage
@st.cache_data
def load_data():
    # Pastikan file ini sudah ada di session storage Colab Anda
    df = pd.read_csv('clean_tokopedia_reviews.csv')
    df['review_date'] = pd.to_datetime(df['review_date'])
    df['year'] = df['review_date'].dt.year
    df['month'] = df['review_date'].dt.month
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ File 'clean_tokopedia_reviews.csv' tidak ditemukan. Silakan jalankan analisis lokal terlebih dahulu.")
    st.stop()

# 3. Header Dashboard
st.title("📊 Tokopedia Consumer Insight Dashboard (2015–2025)")
st.markdown("---")

# 4. Ringkasan Eksekutif (KPI Cards untuk Insight Instan)
st.subheader("📌 Ringkasan Performa Utama")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(f"<div class='metric-box'><h5>Total Ulasan Dinalisis</h5><h2>{len(df):,}</h2><p class='text-muted'>Volume Data Big Data</p></div>", unsafe_allow_html=True)
with kpi2:
    avg_rating = df['rating'].mean()
    st.markdown(f"<div class='metric-box'><h5>Rata-rata Rating</h5><h2>{avg_rating:.2f} / 5.0</h2><p class='text-success'>Sangat Puas ⭐</p></div>", unsafe_allow_html=True)
with kpi3:
    # Mengambil proporsi rating 5 dari temuan EDA
    prop_bintang_5 = (df['rating'] == 5).mean() * 100
    st.markdown(f"<div class='metric-box'><h5>Dominasi Bintang 5</h5><h2>{prop_bintang_5:.1f}%</h2><p class='text-info'>Mayoritas Mutlak</p></div>", unsafe_allow_html=True)
with kpi4:
    st.markdown(f"<div class='metric-box'><h5>Akurasi Model AI</h5><h2>96.0%</h2><p class='text-purple'>F1-Score Sentimen Positif</p></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Pembagian Tab Berdasarkan Sudut Pandang Bisnis
tab1, tab2, tab3 = st.tabs(["📈 Tren & Keterlibatan", "⚖️ Analisis Faktor & Hipotesis", "🤖 Prediksi & AI Insight"])

# --- TAB 1: TREN & KETERLIBATAN CONSUMER ---
with tab1:
    st.header("Analisis Tren Temporal Ekonomi Digital")
    col_a, col_b = st.columns([2, 1])

    with col_a:
        tren_tahun = df.groupby('year').size().reset_index(name='Jumlah Review')
        fig_trend = px.line(tren_tahun, x='year', y='Jumlah Review', markers=True,
                            title='Pertumbuhan Volume Ulasan Tahunan',
                            labels={'year': 'Tahun', 'Jumlah Review': 'Volume Transaksi/Ulasan'})
        fig_trend.update_traces(line_color='#28a745', marker=dict(size=8))
        st.plotly_chart(fig_trend, use_container_width=True)

    with col_b:
        st.markdown("""
        ### 💡 Insight Bisnis untuk Manajemen:
        * **Akselerasi Digital (Pasca-2020):** Lonjakan masif ulasan mengonfirmasi pergeseran perilaku konsumen yang makin bergantung pada e-commerce sejak pandemi.
        * **Kematangan Pasar (2024-2025):** Aktivitas mencapai puncaknya, menandakan ekosistem Tokopedia telah menjadi bagian dari rutinitas harian konsumen.
        """)

# --- TAB 2: ANALISIS FAKTOR & HIPOTESIS ---
with tab2:
    st.header("Pengujian Asumsi & Hipotesis Operasional")

    col_c, col_d = st.columns(2)

    with col_c:
        st.subheader("1. Pengaruh Harga Terhadap Kepuasan")
        avg_price = df.groupby('rating')['product_price'].mean().reset_index()
        fig_harga = px.bar(avg_price, x='rating', y='product_price',
                           title='Rata-rata Harga Produk per Skala Rating',
                           labels={'product_price': 'Rata-rata Harga (Rp)', 'rating': 'Rating'},
                           color_discrete_sequence=['#ffc107'])
        st.plotly_chart(fig_harga, use_container_width=True)
        st.info("💡 **Hasil Statistik:** Korelasi Spearman sangat lemah (rho = 0.03). Kepuasan pelanggan bersifat independen terhadap harga barang.")

    with col_d:
        st.subheader("2. Ketangguhan Layanan Saat Harbolnas")
        avg_rating_month = df.groupby('month')['rating'].mean().reset_index()
        avg_rating_month['Keterangan'] = avg_rating_month['month'].apply(lambda x: 'Harbolnas (Desember)' if x == 12 else 'Bulan Biasa')

        fig_harbolnas = px.bar(avg_rating_month, x='month', y='rating', color='Keterangan',
                               title='Stabilitas Rating Bulanan',
                               color_discrete_map={'Harbolnas (Desember)': '#dc3545', 'Bulan Biasa': '#007bff'})
        fig_harbolnas.update_layout(yaxis_range=[4.5, 5.0])
        st.plotly_chart(fig_harbolnas, use_container_width=True)
        st.info("💡 **Hasil Statistik:** Uji Mann-Whitney membuktikan tidak ada penurunan kepuasan yang signifikan di bulan Desember meskipun terjadi lonjakan beban operasional.")

# --- TAB 3: PREDIKSI & AI INSIGHT ---
with tab3:
    st.header("Implementasi Advanced Analytics & Machine Learning")

    col_e, col_f = st.columns(2)

    with col_e:
        st.subheader("Klasifikasi Sentimen Berbasis Teks (SVM)")
        st.markdown("""
        Model kecerdasan buatan dilatih menggunakan algoritma *Support Vector Machine* (SVM) untuk membaca ulasan tekstual konsumen secara otomatis.

        * **Akurasi Sentimen Positif:** **96% (F1-Score)**
        * **Rekomendasi Operasional:** Perusahaan dapat memanfaatkan model ini untuk melakukan *real-time flagging* pada ulasan yang masuk tanpa perlu validasi manual oleh tim CS.
        """)

    with col_f:
        st.subheader("Forecasting Tren Masa Depan (Prophet)")
        st.markdown("""
        Melalui pemodelan *Time Series Forecasting* menggunakan algoritma Prophet, tren volume interaksi diproyeksikan akan terus mengalami pertumbuhan positif.

        * **Rekomendasi Infrastruktur:** Tim IT dan operasional disarankan untuk meningkatkan kapasitas server dan memperkuat kemitraan logistik menjelang kuartal akhir guna mengantisipasi pertumbuhan volume yang diprediksi meningkat.
        """)

