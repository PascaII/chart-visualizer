import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'data.xlsx'
df = pd.read_excel(file_path)

print(df.head())

df = df[["Satisfaction", "Frequency", "Flexibility", "Way","Productivity", "Costs", "Friends"]]

correlation_matrix = df.corr()

print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()
