import data_preparation as dp
import update_data as ud

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