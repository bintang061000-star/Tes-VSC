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