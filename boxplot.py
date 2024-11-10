import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'data.xlsx'
df = pd.read_excel(file_path)

x_values = ["Unter 20 Jahre", "20-29 Jahre", "30-39 Jahre", "40-49 Jahre", "50-59 Jahre", "60 Jahre und älter"]
y_values = ["Seltener", "Einmal pro Woche", "Mehrmals pro Woche", "Täglich"]

plt.figure(figsize=(11, 6))
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 14

sns.boxplot(x='Age', y='Frequency', data=df,
            width=0.6,
            linewidth=1.0,
            palette=['#C88D44', '#EEA954', '#FFC283', '#FFD9B8'],)

plt.xticks(range(len(x_values)), x_values)

plt.yticks([1, 2, 3, 4], y_values)

plt.ylim(0.5, 4.5)

plt.xlabel('Alter', fontsize=16, weight='bold')
plt.ylabel('Frequenz', fontsize=16, weight='bold')

plt.tight_layout()
plt.savefig('age_frequency_boxplot.png', dpi=500)
plt.show()