import data_preparation as dp
import update_data_preparation as ud

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(dp.df)
print(dp.city_sort[[ 'Rent_Yearly', 'Tuition_Yearly']].sort_values(by='Tuition_Yearly', ascending=False))
print(dp.city_sort[['University', 'Program']])

city_sort = dp.df.groupby('City').agg({
    'Living_Cost_Index': 'mean',  # Kolom angka: Hitung Rata-ratanya
    'Rent_Yearly': 'mean',        # Kolom angka: Hitung Rata-ratanya
    'Tuition_Yearly': 'mean',     # Kolom angka: Hitung Rata-ratanya
    'University': 'first',        # Kolom Teks: Ambil nama universitas pertama yang muncul
    'Program': 'first'            # Kolom Teks: Ambil nama program pertama yang muncul
}).sort_values(by='Living_Cost_Index', ascending=False).round(2)

checking_table = dp.df[['Level', 'Program', 'University']]
print(checking_table)


# Cek hasil
print(dp.df[['City', 'Living_Cost_Index', 'Total_Monthly_Need']].sort_values(by='Total_Monthly_Need', ascending=False).head(5))
print(dp.df[['City', 'Living_Cost_Index', 'Total_Yearly_Need']].sort_values(by='Total_Yearly_Need', ascending=False).head(5))

# Pastikan menggunakan nama kolom yang tepat: 'Avg_Tuition'
dp.df_avg_tuition_Fix['Avg_Tuition_Yearly'] = dp.df_avg_tuition_Fix['Avg_Tuition'] * 2
print(dp.df_avg_tuition)

print(f"Rata-rata Kenaikan Tahunan: {dp.rata_rata_persen:.2f}%")