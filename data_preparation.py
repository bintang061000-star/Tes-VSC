import pandas as pd
import yfinance as yf

#IMPORT FILE
df = pd.read_csv('New International_Education_Costs.csv')
df_us_tuition = pd.read_csv('Private_Avg_Tuition.csv', sep=';')
df_us_tuition.to_csv('Avg_Tuition_Fix.csv', sep=',', index=False)
df_uk_tuition = pd.read_csv('UK_Avg_Tuition.csv')
df_aus_tuition = pd.read_csv('Aus_Avg_Tuition.csv')

#UPDATE DATA
def update_data(df):
    update_typo = {
        'MIT' : 'Boston',
        'Massachusetts' : 'MIT'
    }

    update_level = {
        'Bachelor' : 1,
        'Master' : 2,
        'PhD' : 3
    }

        # Update Living Cost Index
    update_liv_cost = {
        #Australia
        'Brisbane': 69.13,
        'Canberra': 69.18,
        'Melbourne': 72.62,
        'Sydney': 74.45,

        #Austria
        'Vienna': 72.95,

        #Belgium
        'Brussels': 72.15,

        #Canada
        'Montreal': 66.42,
        'Sherbrooke': 58.37,

        #China
        'Beijing': 51.57,

        #Egypt
        'Cairo': 35.10,

        #France
        'Lille': 68.37,
        'Lyon': 73.23,
        'Nice': 74.07,
        'Paris': 79.45,
        'Toulouse': 69.70,

        #Germany
        'Berlin': 67.67,
        'Hamburg': 70.27,
        'Munich': 71.17,

        #Greece
        'Athens': 62.13,

        #Netherlands
        'Amsterdam': 75.97,

        #New Zeeland
        'Auckland': 76.27,

        #Singapore
        'Singapore': 82.02,

        #South Korea'
        'Busan': 69.60,
        'Daejeon': 72.90,
        'Seoul': 82.37,

        #Spain
        'Barcelona': 69.87,

        #Switzerland
        'Basel': 96.80,
        'Lugano': 96.70,

        #UK
        'Bristol': 70.26,
        'Cambridge': 74.10,
        'Edinburgh': 69.70,
        'Leeds': 65.32,
        'London': 78.44,
        'Manchester': 67.34,

        #USA
        'Austin': 70.38,
        'Boston': 82.32,
        'Madison': 70.35
    }
    df['City'] = df['City'].replace(update_typo)
    df['University'] = df['University'].replace(update_typo)
    df['Level'] = df['Level'].map(update_level).fillna(df['Level'])
    df['Living_Cost_Index'] = df['City'].map(update_liv_cost).fillna(df['Living_Cost_Index'])
    return df

#APPEND YEARLY COST COLUMNS
def append_yearly_costs(df):
    df['Rent_Yearly'] = df['Rent_USD'] * 12
    df['Tuition_Yearly'] = df['Tuition_USD'] * 2
    return df
    
#EXACT LIVING COSTS (MONTHLY)
def exact_living_cost(df):
    baseline_spending = 1650                                                              
    living_cost_excl_Rent = (df['Living_Cost_Index'] / 100) * baseline_spending        
    fix_living_cost = living_cost_excl_Rent + df['Rent_USD']                              
    return df

#PERSENTAGE GROWTH US AVG TUITION
def get_us_avg_growth(df):
    # Gunakan .copy() agar tidak merusak data asli
    df_us_avg_tuition = df.copy()
    df_us_avg_tuition['Growth'] = df_us_avg_tuition['Avg_Tuition'].pct_change() * 100
    return round(df_us_avg_tuition['Growth'].mean(), 2)

#PERSENTAGE GROWTH UK AVG TUITION
def get_uk_avg_growth(df):
    # Gunakan .copy() agar tidak merusak data asli
    df_uk_avg_tuition = df.copy()
    df_uk_avg_tuition['Growth'] = df_uk_avg_tuition['Avg_Tuition'].pct_change() * 100
    return round(df_uk_avg_tuition['Growth'].mean(), 2)

#PERSENTAGE GROWTH UK AVG TUITION
def get_aus_avg_growth(df):
    # Gunakan .copy() agar tidak merusak data asli
    df_aus_avg_tuition = df.copy()
    df_aus_avg_tuition['Growth'] = df_aus_avg_tuition['Avg_Tuition'].pct_change() * 100
    return round(df_aus_avg_tuition['Growth'].mean(), 2)

#EXCHANGE RATE USD/IDR (10 YEARS) --> REVISI & CHECKING
def exchange_rate_growth():
    data_kurs = yf.Ticker("IDR=X").history(period="10y")
    kurs_tahunan = data_kurs['Close'].resample('YE').mean()
    growth_kurs = kurs_tahunan.pct_change() * 100
    rerata_kenaikan_kurs = growth_kurs.mean().round(2)
    return (rerata_kenaikan_kurs.mean())