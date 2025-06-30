# Towards disentangling the interrelationships between hydro-meteorological hazards, conflict and displacement: a case study (for droughts and floods) in Somalia 

The repository here is part of thesis research about **disentangling the complex interrelationships between hydro-meteorological hazards, conflict, and displacement in Somalia**, with a specific focus on droughts and floods. It analyses climate extremes alongside conflict events and displacement patterns; the study also aims to provide insights into how these factors interact spatially and temporally for the period 2022-2023.

## Project Description
For my MSc thesis at the Faculty of Geo-Information Science and Earth Observation (ITC), University of Twente, I explored patterns of displacement in Somalia by integrating conflict and hydrometeorological extremes (drought and floods). The goal was to understand where, when, and how displacement is triggered or intensified by these factors.

## Contents

The repository includes:
- **Datasets:** Aggregated drought, flood, conflict, and displacement data relevant to Somalia, extracted from relevant databases (full description check the data management plan).
- **Scripts:** Python/JavaScript codes used for data analysis, modeling, and generating the outputs.
- **Reports & Documentation:** Research findings and analysis reports.

## Scripts 

**01_Displacement_Aggregation**
Aggregates population and IDP counts per region and district, then merges with corresponding administrative boundary shapefiles for spatial analysis.

**02_Conflict_Analysis**
Generates monthly heatmaps of conflict events by region and produces seasonal bar charts (e.g., MAM, SOND) for the different regions.

**03_Drought_Analysis**
Executed using Google Earth Engine (GEE). All scripts were run within the GEE Code Editor, and results were exported to QGIS for post-processing. [GEE Script Link](https://code.earthengine.google.com/eefd5341366cea4e8b2912b633d794bd)

**04_Flood_Analysis**
Flood maps are extracted from [SWALIM](https://spatial.faoswalim.org/#/)

**05_Displacement_Attribution**
Creates stacked percentage bar charts showing the distribution of displacement reasons—Conflict/Insecurity, Drought, Flood, and Other—over time for each region.

QGIS files and map productions have been added to the relevant folders for spatial visualization and further analysis.

## 📫 Any feedback reach out to
- **LinkedIn:** [Abdillahi Osman](https://www.linkedin.com/in/abdillahi-osman-omar-7b2724173/)
- **Email:** [abdillahiosmanomar@student.utwente.nl](mailto:abdillahiosmanomar@student.utwente.nl)

---

This was part of my MSc thesis within **[4D Earth](https://www.itc.nl/research/research-themes/4d-earth/) - at the Faculty of Geo-Information Science and Earth Observation (ITC), University of Twente**.
