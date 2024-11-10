import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'data.xlsx'
df = pd.read_excel(file_path)

print(df.head())
y_values = ["Nein, viel weniger produktiv", "Nein, weniger produktiv", "Kein Unterschied", "Ja, etwas produktiver", "Ja, viel produktiver"]

plt.figure(figsize=(10, 7))
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 14
df = df[["Children", "Productivity"]]

sns.violinplot(x='Children', y='Productivity', data=df, palette=['#C88D44', '#EEA954', '#FFC283'])
plt.yticks([1, 2, 3, 4, 5], y_values)
plt.ylim(1, 5)

plt.xlabel('Kinder', fontsize=16, weight='bold')
plt.ylabel('Häufigkeit von Homeoffice', fontsize=16, weight='bold')

plt.tight_layout()
plt.savefig('children_productivity_violinplot.png', dpi=500)
plt.show()
