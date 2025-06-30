"""
Script: displacement_reason_validation_automation.py

Description:
This script validates and visualizes displacement reasons (conflict, drought, flood, other)
across all Somali regions using UNHCR-PRMN data from 2022–2023. It:
1. Generates side-by-side bar charts for each region pair
2. Saves all visualizations as .png files
3. Zips all plots for easy download

Author: Omar Abdillahi
Affiliation: ITC, University of Twente
Date: 2025-06-30
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import zipfile

# === CONFIGURATION ===
input_csv = r"C:\Your\Path\To\UNHCR-PRMN-Displacement-Dataset_2022_2023.csv"
output_dir = r"C:\Your\Path\To\Output\DisplacementPlots"
zip_output = r"C:\Your\Path\To\Output\displacement_validation_plots.zip"

os.makedirs(output_dir, exist_ok=True)

# === LOAD DATA ===
df = pd.read_csv(input_csv)
df['Month End'] = pd.to_datetime(df['Month End'], dayfirst=True)
df['YearMonth'] = df['Month End'].dt.strftime('%Y-%m')
df = df[['PreviousRegion', 'Reason', 'TotalIndividuals', 'YearMonth']]
df = df.dropna(subset=['PreviousRegion'])

# === REGION PAIRS ===
region_pairs = [
    ("Awdal", "Bakool"),
    ("Banadir", "Bari"),
    ("Bay", "Galgaduud"),
    ("Gedo", "Hiiraan"),
    ("Lower Juba", "Lower Shabelle"),
    ("Middle Juba", "Middle Shabelle"),
    ("Mudug", "Nugaal"),
    ("Sanaag", "Sool"),
    ("Togdheer", "Woqooyi Galbeed")
]

colors = {
    'Conflict/Insecurity': '#66c2a5',
    'Drought': '#8da0cb',
    'Flood': '#ffd92f',
    'Other': '#b3b3b3'
}

# === GENERATE PLOTS ===
for region1, region2 in region_pairs:
    fig, axes = plt.subplots(1, 2, figsize=(16, 10), sharey=True)
    region_data = {}

    for region in [region1, region2]:
        sub_df = df[df['PreviousRegion'] == region].copy()
        grouped = sub_df.groupby(['YearMonth', 'Reason'])['TotalIndividuals'].sum().reset_index()
        monthly_totals = grouped.groupby('YearMonth')['TotalIndividuals'].transform('sum')
        grouped['Percentage'] = (grouped['TotalIndividuals'] / monthly_totals) * 100
        pivot_df = grouped.pivot(index="YearMonth", columns="Reason", values="Percentage").fillna(0)
        region_data[region] = pivot_df

    for ax, region in zip(axes, [region1, region2]):
        region_data[region].plot(
            kind='barh',
            stacked=True,
            ax=ax,
            color=[colors.get(col, '#cccccc') for col in region_data[region].columns]
        )
        ax.set_title(region, fontsize=14, weight='bold')
        ax.set_xlabel("Percentage")
        ax.set_ylabel("Month")
        ax.grid(axis='x', linestyle='--', alpha=0.7)
        ax.legend().set_visible(False)

    # Shared legend
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles, labels, title="Reason",
        loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4, fontsize=10
    )
    plt.tight_layout(rect=[0, 0.06, 1, 1])

    filename = f"displacement_reasons_{region1.replace(' ', '_').lower()}_{region2.replace(' ', '_').lower()}_2022_2023.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, dpi=300)
    plt.close()

# === ZIP OUTPUT ===
with zipfile.ZipFile(zip_output, 'w') as zipf:
    for root, _, files in os.walk(output_dir):
        for file in files:
            zipf.write(os.path.join(root, file), arcname=file)

print(f"✅ All plots saved and zipped to:\n{zip_output}")
