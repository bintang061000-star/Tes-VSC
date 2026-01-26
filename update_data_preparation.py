import data_preparation as dp

# ================================
# 1. PIPELINE PENGOLAHAN DATA
# ================================
print("Memproses Data Utama...")

# Kita gunakan copy() agar dp.df asli tidak terganggu jika kita rerun script ini
df_working = dp.df.copy() 

df_clean = dp.update_data(df_working)
df_clean = dp.append_yearly_costs(df_clean)
df_clean = dp.exact_living_cost(df_clean) # Sekarang ini return DataFrame, jadi aman

print("Menghitung Faktor Ekonomi...")
us_tuition_inflation = dp.get_us_avg_growth(dp.df_us_tuition)
uk_tuition_inflation = dp.get_uk_avg_growth(dp.df_uk_tuition)
aus_tuition_inflation = dp.get_aus_avg_growth(dp.df_aus_tuition)
kurs_inflation = dp.exchange_rate_growth()

# ================================
# 3. OUTPUT HASIL
# ================================
print("\n--- HASIL AKHIR ---")
print(f"1. Rata-rata Inflasi Biaya Kuliah US: {us_tuition_inflation}%")
print(f"2. Rata-rata Inflasi Biaya Kuliah UK: {uk_tuition_inflation}%")
print(f"3. Rata-rata Inflasi Biaya Kuliah Australia: {aus_tuition_inflation}%")
print(f"4. Rata-rata Kenaikan Kurs USD/IDR: {kurs_inflation}%")

# print("\nContoh Data Frame Bersih (5 baris pertama):")
# # Kolom 'Total_Yearly_Living_Cost' sekarang sudah pasti ada
# show_coloum = ['University', 'City', 'Level', 'Tuition_Yearly', 'Rent_Yearly']
# print(df_clean[show_coloum].head())