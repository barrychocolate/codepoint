# Shapefile Merger and Geodatabase Saver

## Overview
This Python project is designed to work with Ordnance Survey's [Codepoint with polygons](https://www.ordnancesurvey.co.uk/products/code-point-polygons), which provides polygons for Great Britain's 1.6 million postcodes. The script processes 120 shapefiles, each representing a set of postcode polygons, and merges them into a single feature class stored in an Esri geodatabase. After combining the shapefiles, the process dissolves the postcode boundaries to create broader postcode area polygons. 

The code is available in two formats: a Jupyter Notebook for interactive use or as a standalone Python script for automated execution.

### Key Features:
- Merges multiple postcode shapefiles from a folder into a single layer.
- Saves the merged output as a feature class in a geodatabase.
- Dissolves the postcodes by postcode area, to create a seperate postcode area feature class in the geodatabase.
- Automatically creates a new file geodatabase if it does not already exist.  These should be download from [https://osdatahub.os.uk/].

## Requirements

- ArcGIS with Python (ArcPy) installed.
- A folder containing shapefiles that need to be merged.
- Esri file geodatabase or location to create one.

## Installation

1. Install ArcGIS or ArcGIS Pro with `arcpy` support.
2. Clone or download this project.

## Usage

1. Update the script with the correct folder paths:
   - Set the `shapefile_folder` variable to point to the directory containing your shapefiles.
   - Set the `geodatabase_folder` and `geodatabase_name` variables to specify where the output geodatabase should be located.

2. Run the script in an ArcGIS-compatible Python environment:

   ```bash
   python shapefile_merger.py
   ````
