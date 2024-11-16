import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'data.xlsx'
df = pd.read_excel(file_path)

df_grouped = df.groupby('Age')['Criterium'].value_counts(normalize=True).unstack() * 100
print(df_grouped)
df_grouped = df_grouped.fillna(0)

categories = [16, 25, 35, 45, 55, 65]
age_labels = {
    16: "Unter 20 Jahre",
    25: "20-29 Jahre",
    35: "30-39 Jahre",
    45: "40-49 Jahre",
    55: "50-59 Jahre",
    65: "60 Jahre und älter"
}

values_ja = [df_grouped.loc[cat, 'Ja'] for cat in categories]
values_nein = [df_grouped.loc[cat, 'Nein'] for cat in categories]

values_ja += values_ja[:1]
values_nein += values_nein[:1]
categories += categories[:1]

angles = [n / float(len(categories)-1) * 2 * np.pi for n in range(len(categories))]

plt.figure(figsize=(10, 10))
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 12

ax = plt.subplot(111, polar=True)

ax.plot(angles, values_ja, 'o-', linewidth=2, color='#C88D44', label='Ja')
ax.fill(angles, values_ja, alpha=0.25, color='#C88D44')

ax.plot(angles, values_nein, 'o-', linewidth=2, color='#EEA954', label='Nein')
ax.fill(angles, values_nein, alpha=0.25, color='#EEA954')

ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

ax.set_xticks(angles[:-1])
ax.set_xticklabels([age_labels[cat] for cat in categories[:-1]], fontsize=10)

plt.title('Homeoffice als Kriterium nach Altersgruppe',
          fontsize=16,
          weight='bold',
          pad=20)

ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'])

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('age_homeoffice_radar.png', dpi=500, bbox_inches='tight')
plt.show()