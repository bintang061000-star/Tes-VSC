import data_preparation as dp
import seaborn as sns
import matplotlib.pyplot as plt

check_corr = dp.df.corr(numeric_only=True).round(3)
print(check_corr)

plt.figure(figsize=(12, 8))
sns.heatmap(check_corr,
            annot=True,
            cmap='coolwarm',
            center=0,
            fmt='.2f',)
plt.title('Correlation Matrix')
plt.show()


# # Memeriksa pencilan pada Tuition_USD
# sns.boxplot(x=dp.df['Tuition_USD'])
# plt.title('Deteksi Outlier Tuition USD')
# plt.show()

# # Memeriksa pencilan pada Duration_Years
# sns.boxplot(x=dp.df['Duration_Years'])
# plt.title('Deteksi Outlier Duration Years')
# plt.show()

# # Memeriksa pencilan pada Liv_Cost_Index
# sns.boxplot(x=dp.df['Living_Cost_Index'])
# plt.title('Deteksi Outlier Living Cost Index')
# plt.show()

# #NORDIC MODEL COUNTRY
# check_tuition_nordic = dp.df[dp.df['Country']
#                       .isin(['Denmark',
#                              'Sweden',
#                              'Finland',
#                              'Norway',
#                              'Iceland'])][['Country', 'Tuition_USD']].groupby(['Country']).mean().round(2).sort_values(by='Tuition_USD', ascending=False)
# print(check_tuition_nordic)

# #CONTINENTAL MODEL COUNTRY
# check_tuition_continent = dp.df[dp.df['Country']
#                                 .isin(['Austria',
#                                        'France',
#                                        'Italy',
#                                        'Spain',
#                                        'Luxembourg',
#                                        'Italy',
#                                        'Portugal',
#                                        'Belgium',
#                                        'Poland',
#                                        'Czech Republic',
#                                        'Hungary'])][['Country', 'Tuition_USD']].groupby(['Country']).mean().round(2).sort_values(by='Tuition_USD', ascending=False)
# print(check_tuition_continent)

# #LIBERAL MODEL COUNTRY
# check_tuition_liberal = dp.df[dp.df['Country']
#                               .isin(['USA',
#                                      'UK',
#                                      'Australia',
#                                      'Canada',
#                                      'New Zealand'])][['Country', 'Tuition_USD']].groupby(['Country']).mean().round(2).sort_values(by='Tuition_USD', ascending=False)
# print(check_tuition_liberal)

# print(dp.df_aus_tuition)