"""
Script: conflict_heatmap_and_charts_2023.py

Description:
This script visualizes conflict event data in Somalia for the year 2023 using:
1. A heatmap showing monthly events per region
2. Bar charts with seasonal highlights for selected regions

Author: Omar Abdillahi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

# === Conflict Data (2023) ===
data_2023 = {
    "Region": ["Bakool", "Banadir", "Bay", "Gedo", "Hiraan", "Lower Juba", "Lower Shabelle", "Middle Juba", "Middle Shabelle"],
    "Jan": [10, 26, 21, 6, 43, 26, 73, 1, 10],
    "Feb": [12, 31, 26, 11, 27, 18, 74, 1, 15],
    "Mar": [9, 31, 30, 10, 28, 22, 50, 3, 16],
    "Apr": [6, 17, 26, 5, 27, 25, 52, 2, 13],
    "May": [9, 33, 21, 1, 14, 12, 76, 6, 10],
    "Jun": [5, 15, 19, 7, 23, 14, 99, 6, 17],
    "Jul": [10, 21, 35, 8, 28, 37, 62, 1, 18],
    "Aug": [13, 15, 28, 12, 30, 19, 67, 4, 19],
    "Sep": [24, 19, 30, 16, 19, 27, 77, 4, 15],
    "Oct": [13, 15, 16, 8, 20, 17, 82, 7, 10],
    "Nov": [6, 8, 13, 2, 8, 16, 92, 2, 10],
    "Dec": [10, 28, 33, 5, 14, 17, 100, 4, 18]
}

df = pd.DataFrame(data_2023)
df["Total"] = df.iloc[:, 1:].sum(axis=1)
df.set_index("Region", inplace=True)

month_data = df.drop(columns="Total")
total_data = df["Total"].to_frame()

# === Heatmap ===
fig = plt.figure(figsize=(16, 7))
gs = GridSpec(1, 2, width_ratios=[12, 1])

ax0 = plt.subplot(gs[0])
sns.heatmap(
    month_data,
    annot=True, fmt="d", cmap="YlOrRd", linewidths=0.5,
    cbar_kws={"label": "Monthly Conflict Events"},
    annot_kws={"size": 14},
    ax=ax0
)
ax0.set_title("Monthly Conflict Events by Region (2023)", fontweight="bold", fontsize=20)
ax0.set_xlabel("Month", fontsize=16)
ax0.set_ylabel("Region", fontsize=16)
ax0.tick_params(axis='x', labelsize=14, rotation=45)
ax0.tick_params(axis='y', labelsize=14)

ax1 = plt.subplot(gs[1])
sns.heatmap(
    total_data,
    annot=True, fmt="d", cmap="Oranges", linewidths=0.5,
    cbar_kws={"label": "Total"},
    annot_kws={"size": 14},
    ax=ax1
)
ax1.set_title("Total", fontweight="bold", fontsize=18)
ax1.set_xticklabels(["Total"], rotation=90, fontsize=14)
ax1.tick_params(axis='y', labelleft=False)

plt.tight_layout()
plt.show()

# === Region-specific bar charts ===

def plot_conflict_chart(region_name, output_file):
    months = df.columns[:-1]  # exclude 'Total'
    values = df.loc[region_name, months]

    plt.figure(figsize=(10, 5))
    bars = plt.bar(months, values, color='steelblue')

    plt.axvspan(1.5, 4.5, color='lightcoral', alpha=0.2, label='MAM')
    plt.axvspan(7.5, 11.5, color='lightcoral', alpha=0.2, label='SOND')

    plt.title(f"Monthly Conflict Events in {region_name} (2023)", fontweight='bold')
    plt.xlabel("Month")
    plt.ylabel("Number of Events")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

plot_conflict_chart("Hiiraan", "conflict_hiiraan_2023.png")
plot_conflict_chart("Lower Shabelle", "conflict_lower_shabelle_2023.png")

print("✅ Saved: conflict_hiiraan_2023.png and conflict_lower_shabelle_2023.png")
