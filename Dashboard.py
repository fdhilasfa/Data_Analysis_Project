import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
from babel.numbers import format_currency
sns.set(style='dark')
from datetime import datetime
import datetime as dt

st.set_page_config(page_title='Brazilian E-Commerce', page_icon=':bar_chart:', layout='wide')

# Header
st.title('Dashboard Aplikasi E-Commerce')
st.subheader('Fadhila Syahda Faustina Austrin')

# Content
df = pd.read_csv("merged_file.csv")
st.header('Brazilian E-Commerce Dashboard :sparkles:')

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center;'>
            <div style='margin-left: 10px; font-size: 24px; font-weight: bold; color: #53ECEC;'>Fadhila E-Commerce Projects</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<hr style='margin: 15px 0; border-color: #53ECEC;'>", unsafe_allow_html=True)

    st.markdown("### E-Commerce Dataset")
    st.markdown("[Kaggle E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)")

    st.markdown("<hr style='margin: 15px 0; border-color: #53ECEC;'>", unsafe_allow_html=True)

    st.markdown("### About")
    st.markdown(
        """
        This dashboard displays insights from the E-Commerce dataset. 
    
        """
    )

    st.markdown("<hr style='margin: 15px 0; border-color: #53ECEC;'>", unsafe_allow_html=True)

    st.markdown("### Contact")
    st.markdown(
        """
        If you have any questions or feedback, feel free to reach out at:
        - Email: [fadhilaaustrin@gmail.com](mailto:fadhilaaustrin@gmail.com)
        - Linkedin: [fadhilasyahda](https://www.linkedin.com/in/fadhilasyahda)
        """,
        unsafe_allow_html=True
    )


## Barchart Kota dengan customer terbanyak

# Baca dataset
customer_df = pd.read_csv("merged_file.csv")

# Customer di setiap kota
st.header("1. Hitung jumlah unik customer di setiap kota")
st.markdown("- Grafik Customer")

# Hitung jumlah unik customer di setiap kota
city_customer_count = customer_df.groupby(by="customer_city").customer_id.nunique().sort_values(ascending=False)

# Buat DataFrame baru untuk visualisasi
df_visual = pd.DataFrame(city_customer_count).reset_index()
df_visual.columns = ['City', 'Number of Customers']

# Buat plot
plt.figure(figsize=(10,6))
sns.barplot(x='Number of Customers', y='City', data=df_visual.head(10), palette='coolwarm')

# Tampilkan plot
plt.title('Top 10 Cities by Number of Customers')
st.pyplot(plt)


# Berapa rata rata skala skor ulasan dari produk yang dijual?

# Rata rata skala skor ulasan dari produk yang dijual
st.header("2.  Rata rata skala skor ulasan dari produk yang dijual")
st.markdown("- Rata rata skala skor ulasan")

# Baca dataset
review_df = pd.read_csv("merged_file.csv")

# Hitung rata-rata review_score
average_review_score = review_df['review_score'].mean()

st.write(f"Rata-rata skala skor ulasan adalah {average_review_score:.2f}")

# Buat histogram
plt.figure(figsize=(10,6))
plt.hist(review_df['review_score'], bins=5, edgecolor='black')

# Tambahkan judul dan label
plt.title('Distribusi Skor Ulasan')
plt.xlabel('Skor Ulasan')
plt.ylabel('Jumlah Ulasan')

# Tampilkan plot
st.pyplot(plt)

# Berapa rata-rata waktu pengiriman?

# Rata-rata waktu pengiriman
st.header("3.  Rata rata waktu pengiriman")
st.markdown("- Rata rata waktu pengiriman")

# Baca dataset
order_df = pd.read_csv("merged_file.csv")

# Ubah kolom ke datetime
order_df["order_delivered_carrier_date"] = pd.to_datetime(order_df["order_delivered_carrier_date"])
order_df["order_delivered_customer_date"] = pd.to_datetime(order_df["order_delivered_customer_date"])

# Hitung selisih waktu dalam detik
delivery_time = order_df["order_delivered_carrier_date"] - order_df["order_delivered_customer_date"]
delivery_time = delivery_time.apply(lambda x: x.total_seconds())

# Ubah detik ke hari dan bulatkan ke bawah
delivery_time = (delivery_time/86400).apply(np.floor)

# Tambahkan kolom baru ke dataframe
order_df["delivery_time"] = delivery_time

# Hitung rata-rata delivery date
average_delivery_time = abs(order_df['delivery_time'].mean())
st.write(f"Rata-rata waktu pengiriman adalah {average_delivery_time:.2f} hari")

# Hitung jumlah pesanan untuk setiap status
order_status_counts = order_df["order_status"].value_counts()

# Buat pie chart
fig, ax = plt.subplots()
ax.pie(order_status_counts, labels=order_status_counts.index, autopct='%1.1f%%', colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
plt.title("Distribusi Order Status")

# Tambahkan legenda
ax.legend(order_status_counts.index, title="Order Status", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

st.pyplot(fig)
