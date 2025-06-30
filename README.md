# **Laporan Proyek Analisis Data: Kualitas Udara**

* Nama: Andi Adnan
* Email: adnanandi252@gmail.com
* ID Dicoding: andi_adnan_252

## **Latar Belakang**
Proyek ini bertujuan untuk melakukan analisis mendalam terhadap dataset kualitas udara yang mencakup periode dari tahun 2013 hingga 2017. Data ini berisi pengukuran berbagai polutan udara seperti Karbon Monoksida (CO), Sulfur Dioksida (SO2), Nitrogen Dioksida (NO2), serta partikel PM2.5 dan PM10 dari 12 stasiun pengukuran yang berbeda. Selain itu, data ini juga mencakup variabel meteorologi seperti suhu (TEMP), tekanan udara (PRES), kelembapan (DEWP), curah hujan (RAIN), dan kecepatan angin (WSPM).

Tujuan utama dari analisis ini adalah untuk memahami tren kualitas udara, mengidentifikasi lokasi dengan tingkat polusi tertentu yang signifikan, dan mengeksplorasi hubungan antara polutan dengan faktor cuaca. Hasil dari analisis ini divisualisasikan dalam sebuah dashboard interaktif menggunakan Streamlit untuk mempermudah pemantauan dan pengambilan keputusan.

## **Pertanyaan Bisnis**
Analisis ini dirancang untuk menjawab tiga pertanyaan utama:
1. Bagaimana tren kualitas udara berdasarkan konsentrasi Karbon Monoksida (CO) dalam periode waktu tertentu?
2. Bagaimana hasil pengukuran sulfur dikoksida berdasarkan stasiun pengukuran di tahun 2016?
3. Bagaimana hubungan antara faktor meteorologi (suhu, tekanan udara, kelembaban, curah hujan, arah dan kecepatan angin) dengan tingkat polusi udara?

## **Data Wrangling**
Tahapan ini mencakup proses pengumpulan, penilaian, dan pembersihan data untuk memastikan kualitas dan kesiapannya untuk dianalisis.
1. Gathering Data
Data dikumpulkan dengan menggabungkan 12 file CSV terpisah yang berasal dari 12 stasiun pengukuran yang berbeda. Setelah digabungkan, dataset akhir terdiri dari 420.768 baris dan 18 kolom.

2. Assessing Data
Pada tahap penilaian, ditemukan beberapa isu utama:
* Tipe Data: Sebagian besar data sudah memiliki tipe yang sesuai (numerik untuk pengukuran dan objek untuk kategori).
* Missing Values: Ditemukan sejumlah besar nilai yang hilang (missing values) pada kolom-kolom polutan (seperti CO, NO2, SO2) dan beberapa kolom meteorologi. Kolom CO memiliki missing values terbanyak, yaitu sebanyak 20.701 baris.
* Data Duplikat: Tidak ditemukan adanya data duplikat dalam dataset.

3. Cleaning Data
Proses pembersihan data dilakukan untuk mengatasi isu yang ditemukan:
* Penanganan Missing Values:
    * Untuk data numerik, digunakan metode imputasi interpolasi linear. Metode ini dipilih karena sangat cocok untuk data time-series seperti data kualitas udara, di mana nilai yang hilang dapat diestimasi berdasarkan nilai sebelum dan sesudahnya.
    * Untuk data kategorikal (kolom wd atau arah angin), digunakan metode imputasi modus, yaitu mengisi nilai yang hilang dengan nilai yang paling sering muncul.
* Setelah proses pembersihan, dataset sudah tidak memiliki nilai yang hilang dan siap untuk tahap analisis eksplorasi.

## **Exploratory Data Analysis (EDA) & Visualisasi**
Analisis dan visualisasi data difokuskan untuk menjawab pertanyaan-pertanyaan bisnis yang telah ditentukan.

### **Pertanyaan 1: Bagaimana tren kualitas udara berdasarkan konsentrasi Karbon Monoksida (CO)?**
Untuk menjawab pertanyaan ini, dibuat dua visualisasi utama: tren rata-rata CO bulanan dan tahunan.
* Tren Rata-rata CO per Bulan (2013-2017)
    Dari visualisasi tren bulanan, tidak ditemukan pola kenaikan atau penurunan yang konsisten dari tahun ke tahun. Fluktuasi nilai CO cenderung acak, kecuali pada bulan Mei dan September yang menunjukkan tren penurunan konsisten dari tahun 2013 hingga 2016. Secara umum, level CO cenderung lebih tinggi pada bulan-bulan musim dingin (Desember, Januari) dan lebih rendah pada musim panas (Agustus).
* Tren Rata-rata CO per Tahun
    Jika dilihat secara tahunan, rata-rata konsentrasi CO tidak menunjukkan perubahan yang signifikan dari 2013 hingga 2016. Nilai pada tahun 2017 terlihat melonjak, namun hal ini disebabkan oleh data yang tidak lengkap (hanya sampai bulan Februari).

### **Pertanyaan 2: Bagaimana hasil pengukuran Sulfur Dioksida (SO2) berdasarkan stasiun di tahun 2016?**
Analisis ini fokus pada data tahun 2016 untuk membandingkan tingkat SO2 antar stasiun.
* Terdapat perbedaan yang jelas dalam konsentrasi SO2 antar stasiun, yang mengindikasikan bahwa kualitas udara sangat bergantung pada lokasi.
* Tiga stasiun dengan rata-rata SO2 tertinggi adalah:
    1. Nongzhanguan (11.56 µg/m³)
    2. Guanyuan (11.48 µg/m³)
    3. Dongsi (11.47 µg/m³)

* Tiga stasiun dengan rata-rata SO2 terendah adalah:
    1. Huairou (6.64 µg/m³)
    2. Dingling (7.17 µg/m³)
    3. Changping (8.14 µg/m³)

* Perbedaan ini kemungkinan besar disebabkan oleh perbedaan karakteristik lokasi, misalnya antara area pusat kota yang padat dengan area pinggiran yang lebih lengang.

### **Pertanyaan 3: Bagaimana hubungan antara faktor meteorologi dengan tingkat polusi udara?**
Sebuah heatmap korelasi digunakan untuk memvisualisasikan hubungan antara polutan dan variabel cuaca.
* Suhu (TEMP): Memiliki korelasi negatif yang cukup kuat dengan polutan seperti PM2.5, PM10, SO2, NO2, dan CO. Ini berarti saat suhu meningkat, konsentrasi polutan-polutan tersebut cenderung menurun.
* Ozon (O3): Menunjukkan perilaku yang berbeda, di mana O3 memiliki korelasi positif yang kuat dengan suhu (TEMP) dan kecepatan angin (WSPM). Ini menandakan bahwa pembentukan ozon di permukaan justru meningkat saat suhu tinggi.
* Tekanan Udara (PRES): Berkolerasi negatif kuat dengan suhu (TEMP), yang wajar terjadi. Korelasinya dengan polutan lain cenderung lemah.
* Kelembapan (DEWP): Menunjukkan korelasi positif dengan hampir semua polutan, kecuali Ozon.

## **Conclusion**
Berdasarkan hasil analisis, dapat ditarik beberapa kesimpulan dan saran:

### Kesimpulan Pertanyaan 1 (Tren CO)
* Kesimpulan: Tren konsentrasi CO tidak menunjukkan pola musiman yang jelas dari tahun ke tahun, mengindikasikan bahwa sumber polusinya mungkin bervariasi dan tidak sepenuhnya bergantung pada siklus cuaca tahunan. Level CO cenderung lebih tinggi pada musim dingin.
* Saran: Perlu dilakukan analisis lebih lanjut untuk mengidentifikasi faktor-faktor spesifik (misalnya, aktivitas industri atau lalu lintas) yang menyebabkan fluktuasi CO.

### Kesimpulan Pertanyaan 2 (SO2 per Stasiun)
* Kesimpulan: Kualitas udara terkait SO2 sangat bervariasi berdasarkan lokasi. Stasiun yang kemungkinan berada di pusat kota (seperti Nongzhanguan) mencatat tingkat polusi yang lebih tinggi dibandingkan stasiun di area pinggiran (seperti Huairou).
* Saran: Kebijakan pengendalian polusi dapat difokuskan pada area-area dengan tingkat SO2 tinggi. Selain itu, praktik baik dari lokasi dengan udara bersih (seperti Huairou) dapat dipelajari dan diterapkan di lokasi lain.

### Kesimpulan Pertanyaan 3 (Hubungan Polusi & Cuaca)
* Kesimpulan: Faktor meteorologi memiliki korelasi yang signifikan dengan tingkat polutan. Suhu yang lebih tinggi cenderung membantu menyebarkan polutan seperti CO, NO2, dan partikel PM, tetapi justru meningkatkan pembentukan Ozon.
* Saran: Sistem peringatan dini kualitas udara dapat dikembangkan dengan mengintegrasikan data prakiraan cuaca. Selama periode suhu tinggi, perhatian khusus perlu diberikan pada lonjakan konsentrasi Ozon.

## **Lampiran: Setup dan Deployment Dashboard**
Untuk mereproduksi analisis dan menjalankan dashboard interaktif, ikuti langkah-langkah berikut:

### **Kebutuhan Pustaka**
Proyek ini memerlukan beberapa pustaka Python yang tercantum dalam requirements.txt:
```python
streamlit
pandas
numpy
matplotlib
seaborn
```
### **Pengaturan Lingkungan (Anaconda)**
Disarankan untuk menggunakan lingkungan virtual untuk menjaga dependensi proyek.

```bash
# Buat environment baru
conda create --name main-ds python=3.9

# Aktifkan environment
conda activate main-ds

# Install pustaka yang dibutuhkan
pip install -r requirements.txt
```

### **Menjalankan Dashboard Streamlit**
Dashboard interaktif dibuat menggunakan Streamlit untuk memvisualisasikan hasil analisis.

```bash
streamlit run dashboard.py
```

### **Dashboard Live**
Dashboard hasil analisis dapat diakses secara online melalui tautan berikut:
https://airqualitydashboard-adnandi252.streamlit.app/