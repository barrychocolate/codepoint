import arcpy
import os

# allow overwritting
arcpy.env.overwriteOutput = True

# path to folder containing the codepoint shapefiles
shapefile_folder = 'C:/temp/codepoint_input/'

# output path the geo database to store the layers
# the database will be created if it does not already exist
output_folder = "C:/temp/codepoint_output/"
output_name = 'codepoint.gdb'
output_gdb = output_folder + output_name

# Check if the geodatabase exists, and if not, create it
if not arcpy.Exists(output_gdb):
    arcpy.CreateFileGDB_management(output_folder, output_name)
    print(f"Created geodatabase: {output_gdb}")
    arcpy.AddMessage(f"Created geodatabase: {output_gdb}")

# Create a list to hold shapefile paths
shapefiles = []

# Loop through the folder and add all shapefiles to the list
for file in os.listdir(shapefile_folder):
    if file.endswith(".shp"):
        shapefiles.append(os.path.join(shapefile_folder, file))

print(f'There are {len(shapefiles)} shapefiles')
arcpy.AddMessage(f'There are {len(shapefiles)} shapefiles')

# Define the output feature layer in memory
merged_layer = "memory/merged_shapefiles"
dissolved_layer = 'memory/dissolved'

# if layer already exists in memory, delete it
# this allows the code to be run more than once in the same session
if arcpy.Exists(merged_layer):
    arcpy.Delete_management(merged_layer)

if arcpy.Exists(dissolved_layer):
    arcpy.Delete_management(dissolved_layer)

# Use the Merge tool to combine all shapefiles into one in-memory layer
arcpy.Merge_management(shapefiles, merged_layer)

# output the merged layer to the geodatabase
arcpy.management.CopyFeatures(
    merged_layer,
    output_gdb + '/codepoint'
)

arcpy.management.Dissolve(
    in_features=merged_layer,
    out_feature_class=dissolved_layer,
    dissolve_field="PC_AREA",
    statistics_fields=None,
    multi_part="MULTI_PART",
    unsplit_lines="DISSOLVE_LINES",
    concatenation_separator=""
)

# output the dissolved layer to the geodatabase
arcpy.management.CopyFeatures(
    dissolved_layer,
    output_gdb + '/postcode_areas'
)

# delete from memory
arcpy.Delete_management(merged_layer)
arcpy.Delete_management(dissolved_layer)
