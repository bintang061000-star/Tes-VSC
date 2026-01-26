import pandas as pd
import yfinance as yf

# ==========================================
# 1. DATA LOADING & SAVING
# ==========================================
df = pd.read_csv('New International_Education_Costs.csv')

# Bersihkan delimiter Avg_Tuition
df_avg_tuition = pd.read_csv('Private_Avg_Tuition.csv', sep=';')
df_avg_tuition.to_csv('Avg_Tuition_Fix.csv', sep=',', index=False)
df_avg_tuition = pd.read_csv('Avg_Tuition_Fix.csv') # Reload yang sudah bersih

# ==========================================
# 2. PREPROCESSING FUNCTIONS
# ==========================================

def update_data(df):
    """
    Membersihkan typo, mengubah level pendidikan ke angka, 
    dan melengkapi Living Cost Index.
    """
    # KITA PISAH DICTIONARY AGAR TIDAK BENTROK
    # Misal: Jangan sampai kata 'Master' di nama Universitas berubah jadi angka 2
    
    map_fix_typo = {
        'MIT': 'Boston',
        'Massachusetts': 'MIT'
    }
    
    map_level = {
        'Bachelor': 1,
        'Master': 2,
        'PhD': 3
    }
    
    map_living_cost = {
        'Brisbane': 69.13, 'Canberra': 69.18, 'Melbourne': 72.62,
        'Sydney': 74.45, 'Singapore': 82.02, 'Seoul': 82.37,
        'Boston': 82.32, 'Vienna': 72.95, 'Brussels': 72.15,
        'Montreal': 66.42, 'Beijing': 51.57, 'Cairo': 35.10,
        'Paris': 79.45, 'Berlin': 67.67, 'Tokyo': 76.4 # Tambahkan sisanya...
    }

    # EKSEKUSI PERUBAHAN (Wajib Ada!)
    df['City'] = df['City'].replace(map_fix_typo)
    df['University'] = df['University'].replace(map_fix_typo)
    
    # Ubah Level jadi Angka
    df['Level'] = df['Level'].map(map_level).fillna(df['Level']) # fillna biar yg tidak ada di map aman
    
    # Update Living Cost Index (Hanya isi yang kosong/update spesifik)
    # Kita gunakan map ke kolom City
    df['Living_Cost_Index'] = df['City'].map(map_living_cost).fillna(df['Living_Cost_Index'])
    
    return df

def append_yearly_costs(df):
    """Menambah kolom biaya tahunan"""
    df['Rent_Yearly'] = df['Rent_USD'] * 12
    # Asumsi Tuition di data asli adalah per semester/term, jadi dikali 2
    # Kalau data asli sudah per tahun, baris ini tidak perlu dikali 2
    df['Tuition_Yearly'] = df['Tuition_USD'] * 2 
    return df

def calculate_exact_living_cost(df):
    """Menghitung total biaya hidup bulanan"""
    baseline_spending = 1650
    
    # Hitung biaya hidup tanpa sewa
    living_cost_excl_rent = (df['Living_Cost_Index'] / 100) * baseline_spending
    
    # Masukkan hasil ke kolom baru di DataFrame langsung
    df['Total_Monthly_Living_Cost'] = living_cost_excl_rent + df['Rent_USD']
    df['Total_Yearly_Living_Cost'] = df['Total_Monthly_Living_Cost'] * 12
    
    return df

# ==========================================
# 3. ANALYSIS FUNCTIONS (Growth & Rates)
# ==========================================

def get_us_avg_growth(df):
    """Menghitung rata-rata kenaikan biaya kuliah (Data Historis)"""
    # Gunakan .copy() agar tidak merusak data asli
    df_us_avg_tuition = df.copy()
    df_us_avg_tuition['Growth'] = df_us_avg_tuition['Avg_Tuition'].pct_change() * 100
    return round(df_us_avg_tuition['Growth'].mean(), 2)

def get_exchange_rate_growth():
    """Menghitung rata-rata kenaikan kurs USD/IDR"""
    # Menggunakan Ticker.history (Lebih stabil)
    try:
        data_kurs = yf.Ticker("IDR=X").history(period="10y")
        if data_kurs.empty: return 0.0
        
        # Gunakan 'Y' agar aman di Python versi lama
        kurs_tahunan = data_kurs['Close'].resample('Y').mean()
        growth_kurs = kurs_tahunan.pct_change() * 100
        return round(growth_kurs.mean(), 2)
    except Exception as e:
        print(f"Error yfinance: {e}")
        return 0.0

# ==========================================
# 4. MAIN EXECUTION (CARA JALANKANNYA)
# ==========================================

# A. Cleaning Pipeline
print("Memproses Data Utama...")
df_clean = update_data(df)
df_clean = append_yearly_costs(df_clean)
df_clean = calculate_exact_living_cost(df_clean)

# B. Getting External Factors
print("Menghitung Faktor Ekonomi...")
tuition_inflation = get_us_avg_growth(df_avg_tuition)
kurs_inflation = get_exchange_rate_growth()

# C. Menampilkan Hasil
print("\n--- HASIL AKHIR ---")
print(f"1. Rata-rata Inflasi Biaya Kuliah: {tuition_inflation}%")
print(f"2. Rata-rata Kenaikan Kurs USD/IDR: {kurs_inflation}%")
print("\nContoh Data Frame Bersih (5 baris pertama):")
print(df_clean[['University', 'City', 'Level', 'Tuition_Yearly', 'Total_Yearly_Living_Cost']].head())

checking_table = dp.df[['Level', 'Program', 'University']]
print(checking_table)


# FILE: data_preparation.py
import pandas as pd

class InflationEngine:
    def __init__(self, df_main, df_us, df_uk, df_au):
        """
        Ini adalah 'Konstruktor'. Bagian ini jalan otomatis saat Class dipanggil.
        Tugasnya: Menyiapkan semua data agar siap pakai.
        """
        # 1. MEMBUAT PETA (MAPPING) KAMPUS -> NEGARA
        # Mengubah DataFrame menjadi Dictionary agar pencarian super cepat.
        # Contoh hasil: {'MIT': 'USA', 'Oxford': 'UK', 'Melbourne Univ': 'Australia'}
        self.univ_map = dict(zip(df_main['University'], df_main['Country']))
        
        # 2. MENGHITUNG RATE SPESIFIK (Menggunakan Rumus Screenshot Kamu)
        # Kita hitung sekarang, simpan angkanya di memori.
        # Jadi nanti saat user klik tombol, tidak perlu hitung ulang dari nol.
        self.rates = {
            'USA': self._hitung_rumus_growth(df_us),
            'UK': self._hitung_rumus_growth(df_uk),
            'Australia': self._hitung_rumus_growth(df_au)
        }
        
        # 3. SET DEFAULT RATE (Untuk negara selain 3 di atas)
        # Misal kita ambil rata-rata dari ketiga negara tersebut sebagai patokan
        avg_rate = sum(self.rates.values()) / 3
        self.default_rate = round(avg_rate, 2)

    def _hitung_rumus_growth(self, df):
        """
        PRIVATE METHOD: Ini adalah implementasi rumus yang kamu SS sebelumnya.
        Tanda '_' di depan artinya method ini cuma buat pemakaian internal Class.
        """
        # Pastikan nama kolom sesuai dengan excel kamu (misal: 'Avg_Tuition')
        # Logic: Hitung % change tiap tahun -> Ambil rata-ratanya -> Kali 100
        growth = df['Avg_Tuition'].pct_change() * 100
        return round(growth.mean(), 2)

    def get_prediction(self, university_name, current_cost, years):
        """
        PUBLIC METHOD: Ini yang akan dipanggil oleh Streamlit.
        Sistem otomatis mendeteksi negara dan memilih rumus yang tepat.
        """
        # A. Cek Kampus ini ada di Negara mana? (Pake dictionary di langkah 1)
        # Jika kampus tidak dikenal, anggap 'Unknown'
        country = self.univ_map.get(university_name, 'Unknown')
        
        # B. Pilih Rate Inflasi berdasarkan Negara (Pake dictionary di langkah 2)
        # Jika negaranya (misal Germany) gak ada di self.rates, pake self.default_rate
        inflation_rate = self.rates.get(country, self.default_rate)
        
        # C. Hitung Rumus Compound Interest (Bunga Berbunga)
        # Rumus: Biaya * (1 + rate)^tahun
        future_cost = current_cost * ((1 + inflation_rate/100) ** years)
        
        return {
            'future_cost': round(future_cost, 2),
            'inflation_rate_used': inflation_rate,
            'detected_country': country
        }