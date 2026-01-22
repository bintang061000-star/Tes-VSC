import data_preparation as dp
import seaborn as sns
import matplotlib.pyplot as plt

# check_corr = dp.df.corr(numeric_only=True).round(3)
# print(check_corr)

# plt.figure(figsize=(12, 8))
# sns.heatmap(check_corr,
#             annot=True,
#             cmap='coolwarm',
#             center=0,
#             fmt='.2f',)
# plt.title('Correlation Matrix')
# plt.show()


# Memeriksa pencilan pada Tuition_USD
sns.boxplot(x=dp.df['Tuition_USD'])
plt.title('Deteksi Outlier Tuition USD')
plt.show()

# # Memeriksa pencilan pada Duration_Years
# sns.boxplot(x=dp.df['Duration_Years'])
# plt.title('Deteksi Outlier Duration Years')
# plt.show()

# # Memeriksa pencilan pada Liv_Cost_Index
# sns.boxplot(x=dp.df['Living_Cost_Index'])
# plt.title('Deteksi Outlier Living Cost Index')
# plt.show()