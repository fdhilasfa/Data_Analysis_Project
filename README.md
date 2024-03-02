# Data_Analysis_Project

## Project Data Analytics


## Deskripsi

Proyek ini bertujuan untuk melakukan analisis data terhadap dataset E-Commerce yang telah disediakan publik. Tujuan dari project ini adalah untuk menghasilkan insight yang berguna dari data yang diselidiki terkait dengan tren dan pola dalam aktivitas E-Commerce tersebut.

## Struktur Direktori

- **Dataset**: Direktori ini berisi data-data yang digunakan dalam proyek, dalam format .csv .
- **Dashboard.py**: File ini digunakan untuk mengenerate dashboard hasil visualisasi menggunakan streamlit.
- **notebook.ipnyb**: File ini digunakan untuk melakukan analisis data hingga visualisasinya.

## Instalasi

1. Clone repository ini ke komputer lokal Anda menggunakan perintah berikut:

   ```shell
   git clone [https://github.com/fdhilasfa/Data_Analysis_Project.git]
   ```

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run steamlit app
```
streamlit run Dashboard.py
```

