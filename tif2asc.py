#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, glob, sys
from osgeo import gdal, osr

# Function to convert all TIFF rasters in a directory to ASCII and create WGS84 definition files in the same directory.
# The function takes the input directory as an argument.
# The function iterates over all subdirectories in the input directory. SO, IT IS NOT NECESSARY TO CALL THE FUNCTION FOR EACH SUBDIRECTORY.
def tif2asc(input_dir):
    # Find all TIFF files in the input directory
    tif_files = glob.glob(os.path.join(input_dir, "*.tif"))

    # Print tif_files
    print(tif_files)

    # Iterate over each TIFF file
    for tif_file in tif_files:
        # Open the TIFF file using gdal
        src_ds = gdal.Open(tif_file)
        src_band = src_ds.GetRasterBand(1)

        # Create a WGS84 definition file for the raster
        wgs84_def = osr.SpatialReference()
        wgs84_def.ImportFromEPSG(4326)

        # Create an ASCII file in the output directory with the same name as the TIFF file
        output_dir = input_dir
        output_file = os.path.join(output_dir, os.path.basename(tif_file).replace(".tif", ".asc"))

        # Convert the TIFF raster to ASCII using gdal.Translate
        gdal.Translate(output_file, src_ds, format="AAIGrid", noData=src_band.GetNoDataValue(), outputType=gdal.GDT_Float32)

        # Close the datasets
        src_ds = None

        # Delete the original TIFF file and rename the ASCII file to have the same name as the TIFF file DISABLED FOR TESTING
        os.remove(tif_file)

def main():
    # Set the input directory
    input_dir = sys.argv[1]

    # Iterate over all subdirectories in the input directory
    for root, dirs, files in os.walk(input_dir):
        # Convert all TIFF rasters in the current subdirectory to ASCII and create WGS84 definition files in the same subdirectory
        tif2asc(root)

if __name__ == "__main__":
    main()

# IF you remove xml files, ascii files are misread. If you don't remove them, ascii files are correct. You shouldn't remove them.

