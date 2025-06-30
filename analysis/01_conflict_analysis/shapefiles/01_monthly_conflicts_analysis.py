""" 
This script is used to analyze the monthly conflict data and generate a summary report.
It also will merge 2022 and 2023 data, save csv and merge with shapefile.
"""
import pandas as pd
import geopandas as gpd
import numpy as np
import os


# Merge the total fatalities with the shapefile
# Load the shapefile from the specified path

# Load the shapefile
shapefile_path = r'C:\Users\Zako3\OneDrive - University of Twente\Documents\ITC Courses\2nd Year\Thesis\00_Analysis\objective2\00_conflict_analysis\shapefiles\SOM_Adminbnda_Adm2_Regions_UNOCHA.shp'
somalia_gdf = gpd.read_file(shapefile_path)
somalia_gdf.head()

# Load the conflict data
file_path = r"C:\Users\Zako3\OneDrive - University of Twente\Documents\ITC Courses\2nd Year\Thesis\00_Analysis\objective2\00_conflict_analysis\00_Monthly_Region_Conflict_Summary_with_Totals.csv"
conflict_data = pd.read_csv(file_path)
conflict_data.head()

# Merge using correct column names
merged_gdf = somalia_gdf.merge(conflict_data, left_on='admin1Name', right_on='Region', how='left')

# Preview merged GeoDataFrame
print(merged_gdf.head())

# Save the merged GeoDataFrame to a new GeoPackage
output_gpkg_path = r'C:\Users\Zako3\OneDrive - University of Twente\Documents\ITC Courses\2nd Year\Thesis\00_Analysis\objective2\00_conflict_analysis\shapefiles\00_Comprehensive_Monthly_Conflict_Summary.gpkg'
merged_gdf.to_file(output_gpkg_path, driver='GPKG')
print(f"Merged GeoDataFrame saved to {output_gpkg_path}")

# Visualize the merged data in GeoPandas as a map for the total fatalities and events
# Visualize the following 4 columns:
# total_fatalities_2022, total_events_2023, total_fatalities_2023, total_events_2022

import matplotlib.pyplot as plt

# Define the columns to visualize and their titles
columns_to_plot = {
    'total_fatalities_2022': "Total Fatalities by Region in 2022",
    'total_events_2023': "Total Events by Region in 2023",
    'total_fatalities_2023': "Total Fatalities by Region in 2023",
    'total_events_2022': "Total Events by Region in 2022"
}

# Create a figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
axes = axes.flatten()  # Flatten the 2D array of axes for easier iteration

# Loop through the columns and plot each one
for idx, (column, title) in enumerate(columns_to_plot.items()):
    if column in merged_gdf.columns:
        merged_gdf.plot(
            column=column,
            ax=axes[idx],
            legend=True,
            legend_kwds={'label': title, 'orientation': "horizontal"},
            cmap='OrRd'
        )
        axes[idx].set_title(title)
    else:
        axes[idx].set_title(f"Column '{column}' not found")
        axes[idx].axis('off')  # Turn off the axis if the column is missing

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
