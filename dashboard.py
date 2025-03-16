import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

st.title("📊 Dashboard Analisis Peminjaman Sepeda")

st.header("Ringkasan Data")
st.write("### Data Harian")
st.write(day_df.describe())
st.write("### Data Per Jam")
st.write(hour_df.describe())

st.header("Distribusi Data Cuaca & Hari")
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
day_df["weathersit"].hist(ax=ax[0])
day_df["weekday"].hist(ax=ax[1])
ax[0].set_title("Distribusi Kondisi Cuaca")
ax[1].set_title("Distribusi Hari dalam Seminggu")
st.pyplot(fig)

st.header("Tren Peminjaman Sepeda")
min_date = day_df["dteday"].min().to_pydatetime()
max_date = day_df["dteday"].max().to_pydatetime()
date_range = st.slider("Pilih Rentang Tanggal", min_value=min_date, max_value=max_date, value=(min_date, max_date), format="YYYY-MM-DD")
filtered_df = day_df[(day_df["dteday"] >= date_range[0]) & (day_df["dteday"] <= date_range[1])]

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=filtered_df, x="dteday", y="cnt", ax=ax)
ax.set_title("Tren Peminjaman Sepeda dari Waktu ke Waktu")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
plt.xticks(rotation=45)
st.pyplot(fig)

st.header("Distribusi Peminjaman Sepeda berdasarkan Jam")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=hour_df, x="hr", y="cnt", ax=ax)
ax.set_title("Peminjaman Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

st.header("Pengaruh Cuaca terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=day_df, x="weathersit", y="cnt", ax=ax)
ax.set_title("Pengaruh Cuaca terhadap Peminjaman")
ax.set_xlabel("Kondisi Cuaca (1=Baik, 2=Normal, 3=Buruk)")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

st.write("### Sumber Data")
st.write("Dataset diambil dari sistem peminjaman sepeda.")
