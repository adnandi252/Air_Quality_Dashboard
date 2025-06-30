import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# Judul
st.title("Dashboard Analisis Kualitas Udara (2013-2017)")

# Load data
data = pd.read_csv('cleaned_air_quality_data.csv')
data['year'] = pd.Categorical(data['year'], categories=[2013, 2014, 2015, 2016, 2017], ordered=True)

# Sidebar filter
st.sidebar.header("Filter Data")
selected_years = st.sidebar.multiselect("Pilih Tahun", options=[2013, 2014, 2015, 2016, 2017], default=[2013, 2014, 2015, 2016, 2017])

filtered_data = data[data['year'].isin(selected_years)]
pollutants = ['CO', 'SO2', 'NO2', 'PM2.5', 'PM10', 'O3']
selected_pollutant = st.sidebar.selectbox("Pilih Jenis Polusi", pollutants, index=0)

# Membuat layout grid 2x2
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Visualisasi 1: Tren Bulanan Polutan
with col1:
    st.subheader(f"Tren Rata-rata {selected_pollutant} per Bulan")
    monthly_trend = filtered_data.groupby(['year', 'month'])[selected_pollutant].mean().reset_index()
    fig1 = px.bar(monthly_trend, 
              x='month', y=selected_pollutant, color='year', barmode='group',
              color_discrete_sequence=px.colors.qualitative.Set1,
              labels={selected_pollutant: f'Rata-rata {selected_pollutant}', 'month': 'Bulan'},
              title=f'Tren Rata-rata {selected_pollutant} (2013-2017)')
    fig1.update_layout(xaxis=dict(tickmode='array', tickvals=list(range(1,13))))
    st.plotly_chart(fig1, use_container_width=True)

# Visualisasi 2: Tren Tahunan Polutan
with col2:
    st.subheader(f"Rata-rata {selected_pollutant} per Tahun")
    yearly_trend = filtered_data.groupby('year')[selected_pollutant].mean().reset_index()
    fig2 = px.bar(yearly_trend, x='year', y=selected_pollutant,
              color='year', text=selected_pollutant,
              color_discrete_sequence=px.colors.qualitative.Set1,
              labels={selected_pollutant: f'Rata-rata {selected_pollutant}', 'year': 'Tahun'},
              title=f'Rata-rata {selected_pollutant} per Tahun')
    fig2.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig2.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    st.plotly_chart(fig2, use_container_width=True)

# Visualisasi 3: Polutan per Stasiun (2016)
with col3:
    st.subheader(f"Rata-rata SO2 per Stasiun (2016)")
    data_2016 = data[data['year'] == 2016]
    so2_station_2016 = data_2016.groupby('station')['SO2'].mean().reset_index()
    so2_station_2016 = so2_station_2016.sort_values(by='SO2', ascending=False)
    fig3 = px.bar(so2_station_2016, 
                  x='station', y='SO2', text='SO2',
                  color='SO2', color_continuous_scale='Viridis',
                  labels={'SO2': 'Rata-rata SO2', 'station': 'Stasiun'},
                  title='Rata-rata SO2 per Stasiun (2016)')
    fig3.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig3.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig3, use_container_width=True)

# Visualisasi 4: Heatmap Korelasi
with col4:
    st.subheader("Korelasi Polusi & Meteorologi")
    selected_columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
    corr_matrix = filtered_data[selected_columns].corr().round(2)

    fig4 = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale='RdBu',
        reversescale=True,
        zmin=-1, zmax=1,
        text=corr_matrix.values,
        texttemplate="%{text}",
        hoverongaps=False))
    fig4.update_layout(title='Heatmap Korelasi', xaxis_title="", yaxis_title="", width=800, height=500)
    st.plotly_chart(fig4, use_container_width=True)

# Deskripsi
st.markdown("""
Dashboard ini menampilkan analisis kualitas udara dari tahun 2013-2017.  
Visualisasi yang disajikan meliputi:
- **Tren rata-rata CO per bulan**
- **Rata-rata CO per tahun**
- **Rata-rata SO2 per stasiun pada tahun 2016**
- **Heatmap korelasi antara polutan dan variabel meteorologi**
""")
