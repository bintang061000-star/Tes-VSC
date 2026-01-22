import data_preparation as dp

dp.df['University'] = dp.df['University'].replace(dp.update_university)
dp.df['City'] = dp.df['City'].replace(dp.update_city)
dp.df['Living_Cost_Index'] = dp.df['Living_Cost_Index'].replace(dp.updated_living_costs)
dp.df['Level'] = dp.df['Level'].replace(dp.update_level)