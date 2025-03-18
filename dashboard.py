import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# Judul Dashboard
st.title("Dashboard Analisis Kualitas Udara (2013-2017)")

# Load data
data = pd.read_csv('cleaned_air_quality_data.csv')
data['year'] = pd.Categorical(data['year'], categories=[2013, 2014, 2015, 2016, 2017], ordered=True)

polutant_options = ['PM2.5', 'PM10', 'SO2', 'CO', 'NO2', 'O3']
station_options = ['All'] + list(data['station'].unique())

# Filter global untuk semua barchart
selected_polutant = st.selectbox("Pilih Jenis Polutan", polutant_options)
selected_station = st.selectbox("Pilih Stasiun", station_options)

# Membuat layout grid 2x2
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Visualisasi 1: Tren Bulanan Polutan
with col1:
    if selected_station == "All":
        st.subheader(f"Tren Rata-rata {selected_polutant} per Bulan di Semua Stasiun")
    else:
        st.subheader(f"Tren Rata-rata {selected_polutant} per Bulan di Stasiun {selected_station}")
    filtered_data = data if selected_station == "All" else data[data['station'] == selected_station]
    monthly_trend = filtered_data.groupby(['year', 'month'])[selected_polutant].mean().reset_index()
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=monthly_trend, x='month', y=selected_polutant, hue='year', palette='tab10', 
                hue_order=[2013, 2014, 2015, 2016, 2017], ax=ax1)
    ax1.set_title(f'Tren Rata-rata {selected_polutant} (2013-2017)', fontsize=14)
    ax1.set_xlabel('Bulan', fontsize=12)
    ax1.set_ylabel(f'Mean {selected_polutant}', fontsize=12)
    ax1.set_xticklabels(np.arange(1, 13), fontsize=10)
    ax1.legend(title='Tahun', title_fontsize=12, fontsize=10)
    plt.tight_layout()
    st.pyplot(fig1)

# Visualisasi 2: Tren Tahunan Polutan
with col2:
    if selected_station == "All":
        st.subheader(f"Rata-rata {selected_polutant} per Tahun di Semua Stasiun")
    else:
        st.subheader(f"Rata-rata {selected_polutant} per Tahun di Stasiun {selected_station}")
    yearly_trend = filtered_data.groupby('year')[selected_polutant].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2 = sns.barplot(data=yearly_trend, x='year', y=selected_polutant, palette='tab10')
    for i, row in yearly_trend.iterrows():
        ax2.text(i, row[selected_polutant] + 0.2, f'{row[selected_polutant]:.2f}', ha='center', fontsize=10)
    ax2.set_title(f'Rata-rata {selected_polutant} per Tahun', fontsize=14)
    ax2.set_xlabel('Tahun', fontsize=12)
    ax2.set_ylabel(f'Mean {selected_polutant}', fontsize=12)
    ax2.tick_params(axis='x', labelsize=10)
    plt.tight_layout()
    st.pyplot(fig2)

# Visualisasi 3: Polutan per Stasiun (2016)
with col3:
    st.subheader(f"Rata-rata {selected_polutant} per Stasiun (2016)")
    data_2016 = data[data['year'] == 2016]
    station_trend_2016 = data_2016.groupby('station')[selected_polutant].mean().reset_index()
    station_trend_2016 = station_trend_2016.sort_values(by=selected_polutant, ascending=False)
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ax3 = sns.barplot(data=station_trend_2016, x='station', y=selected_polutant, palette='viridis')
    for i, row in enumerate(station_trend_2016.itertuples()):
        ax3.text(i, row[2] + 0.2, f'{row[2]:.2f}', ha='center', fontsize=10)
    ax3.set_title(f'Rata-rata {selected_polutant} (2016)', fontsize=14)
    ax3.set_xlabel('Stasiun', fontsize=12)
    ax3.set_ylabel(f'Mean {selected_polutant}', fontsize=12)
    ax3.tick_params(axis='x', rotation=45, labelsize=10)
    plt.tight_layout()
    st.pyplot(fig3)

# Visualisasi 4: Heatmap Korelasi
with col4:
    st.subheader("Korelasi Polusi & Meteorologi")
    selected_columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
    corr_matrix = data[selected_columns].corr()
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr_matrix, mask=mask, annot=True, cmap='coolwarm', fmt=".2f", 
                linewidths=0.5, ax=ax4, annot_kws={"size": 10})
    ax4.set_title('Heatmap Korelasi', fontsize=14)
    plt.tight_layout()
    st.pyplot(fig4)

# Menambahkan deskripsi
st.markdown("""
Dashboard ini menampilkan analisis kualitas udara dari tahun 2013-2017.
Visualisasi yang disajikan meliputi tren rata-rata polutan per bulan (berdasarkan stasiun dan jenis polutan), 
rata-rata polutan per tahun (berdasarkan stasiun dan jenis polutan),
rata-rata polutan per stasiun pada tahun 2016, dan heatmap korelasi antara polusi dan meteorologi.
""")
