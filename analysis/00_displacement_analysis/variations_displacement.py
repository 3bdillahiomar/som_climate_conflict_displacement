"""
Displacement Analysis in Somalia
---------------------------------------

This script analyzes monthly and regional displacement patterns in Somalia for the year 2022 - 2023
using data from the UNHCR-PRMN dataset.

Main analyses included:
- Regional monthly trends
- National monthly trends
- Total displaced by region (destination)
- Total displaced by region of origin

Dataset used:
UNHCR-PRMN-Displacement-Dataset_2022_2023.csv

Author: Abdillahi Omar
GitHub: https://github.com/3bdillahiomar/som_climate_conflict_displacement
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\Zako3\OneDrive - University of Twente\Documents\ITC Courses\2nd Year\Thesis\00_Analysis\objective1\UNHCR_Analysis_2023\UNHCR-PRMN-Displacement-Dataset_2022_2023.csv"
df = pd.read_csv(file_path)

# Convert 'Month End' column to datetime and extract month name
df['Month End'] = pd.to_datetime(df['Month End'], dayfirst=True)
df['Month'] = df['Month End'].dt.strftime('%b')

# Filter data for the year 2023 only
df_2023 = df[df['Year'] == 2023]

# ----------------------------------------
# Regional Monthly Displacement Trends
# ----------------------------------------

# Group by destination region and month
monthly_displacement = df_2023.groupby(['CurrentMapRegion', 'Month'])['TotalIndividuals'].sum().reset_index()

# Pivot table for plotting
pivot_table = monthly_displacement.pivot(index='Month', columns='CurrentMapRegion', values='TotalIndividuals')
pivot_table = pivot_table.reindex(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Plot regional monthly trends
plt.figure(figsize=(16, 9))
pivot_table.plot(marker='o', colormap='tab20', linewidth=2.5, alpha=0.9)

plt.title('📈 Monthly Displacement Trends per Region in Somalia (2023)', fontsize=18, fontweight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Displaced Individuals', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().set_facecolor('#f9f9f9')
plt.gcf().patch.set_facecolor('#ffffff')
plt.legend(title='Region', bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=10, title_fontsize=12)
plt.tight_layout()
plt.show()

# ----------------------------------------
# National Monthly Trend
# ----------------------------------------

monthly_total = df_2023.groupby('Month')['TotalIndividuals'].sum().reset_index()
month_order = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 
               'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
monthly_total['MonthNumber'] = monthly_total['Month'].map(month_order)
monthly_total = monthly_total.sort_values('MonthNumber')

# Line chart
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_total, x='MonthNumber', y='TotalIndividuals', marker='o', color='blue')
plt.title('Total Individuals Displaced per Month in Somalia (2023)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Displaced Individuals', fontsize=12)
plt.xticks(ticks=range(1, 13), labels=list(month_order.keys()), rotation=45)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().set_facecolor('#f9f9f9')
plt.gcf().patch.set_facecolor('#ffffff')
plt.show()

# Smooth line chart (same data)
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_total, x='MonthNumber', y='TotalIndividuals', marker='o', color='blue', ci=None)
plt.title('Smoothed Displacement Trend in Somalia (2023)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Displaced Individuals', fontsize=12)
plt.xticks(ticks=range(1, 13), labels=list(month_order.keys()), rotation=45)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().set_facecolor('#f9f9f9')
plt.gcf().patch.set_facecolor('#ffffff')
plt.show()

# Bar chart
plt.figure(figsize=(12, 6))
sns.barplot(data=monthly_total, x='MonthNumber', y='TotalIndividuals', palette='viridis')
plt.title('Bar Chart: Monthly Displacement in Somalia (2023)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Displaced Individuals', fontsize=12)
plt.xticks(ticks=range(1, 13), labels=list(month_order.keys()), rotation=45)
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().set_facecolor('#f9f9f9')
plt.gcf().patch.set_facecolor('#ffffff')
plt.show()

# ----------------------------------------
# Total Displacement by Region (Destination)
# ----------------------------------------

total_displaced_per_region = df_2023.groupby('CurrentMapRegion')['TotalIndividuals'].sum().reset_index()
total_displaced_per_region = total_displaced_per_region.sort_values('TotalIndividuals', ascending=False)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=total_displaced_per_region, x='CurrentMapRegion', y='TotalIndividuals', palette='viridis')
plt.title('Total Displacement by Destination Region in Somalia (2023)', fontsize=16, fontweight='bold')
plt.xlabel('Region', fontsize=12)
plt.ylabel('Total Displaced Individuals', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().set_facecolor('#f9f9f9')
plt.gcf().patch.set_facecolor('#ffffff')
plt.tight_layout()
plt.show()

# Print as table
print(total_displaced_per_region)

# ----------------------------------------
# Total Displacement by Region of Origin
# ----------------------------------------

total_displaced_per_origin = df_2023.groupby('PreviousRegion')['TotalIndividuals'].sum().reset_index()
total_displaced_per_origin = total_displaced_per_origin.sort_values('TotalIndividuals', ascending=False)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=total_displaced_per_origin, x='PreviousRegion', y='TotalIndividuals', palette='viridis')
plt.title('Total Displacement by Origin Region in Somalia (2023)', fontsize=16, fontweight='bold')
plt.xlabel('Region of Origin', fontsize=12)
plt.ylabel('Total Displaced Individuals', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
plt.gca().set_facecolor('#f9f9f9')
plt.gcf().patch.set_facecolor('#ffffff')
plt.tight_layout()
plt.show()

# Print as table
print(total_displaced_per_origin)
