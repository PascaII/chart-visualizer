import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'data.xlsx'
df = pd.read_excel(file_path)

print(df.head())

df = df[["Time", "Way"]]

df_counts = df.value_counts().reset_index(name='Count')
df_counts.columns = ['Time', 'Way', 'Count']

total_count = df_counts['Count'].sum()
print("Total count of entries:", total_count)

x_values = ["Keine Zeitersparnis", "Weniger als 30 Minuten", "30 - 60 Minuten", "1 - 2 Stunden", "Mehr als 2 Stunden"]
y_values = ["Sehr negativ", "Negativ", "Neutral", "Positiv", "Sehr positiv"]

plt.figure(figsize=(9, 6))
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 14


sns.scatterplot(
    x='Time',
    y='Way',
    size='Count',
    sizes=(20, 200),
    hue='Way',
    palette=['#C88D44', '#EEA954', '#FFC283', '#FFD9B8'],
    data=df_counts,
    legend=False
)

sns.regplot(
    x='Time',
    y='Way',
    data=df,
    scatter=False,
    line_kws={'color': 'black'},
    ci=95
)

plt.ylim(0.5, 5.5)
plt.xticks([0, 15, 45, 90, 120], x_values, rotation=35)
plt.yticks([1, 2, 3, 4, 5], y_values)
plt.xlabel('gesparte Zeit', fontsize=16, weight='bold')
plt.ylabel('Zufriedenheit durch Wegfall', fontsize=16, weight='bold')

plt.tight_layout()
plt.savefig('time_way_scatter.png', dpi=500)
plt.show()
