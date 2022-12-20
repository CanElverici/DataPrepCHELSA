#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import sys
from osgeo import gdal


# Code to crop rasters according to test_mcp/mcp.shp in test_marea folder
# The code should be able to crop multiple rasters at once

def m_area(mshp_path, rasters_path):
    # If sys.argv[1,2] are not defined, the script will tell the user to define the path to the shapefile and the path to the folder containing the rasters
    # If sys.argv[1,2] are defined, the script will run with the values defined by the user and crop the rasters
    if len(sys.argv) < 3:
        print("Please define the path to the shapefile and the path to the folder containing the rasters")
        return

    # Define the path to the shapefile
    mshp = sys.argv[1]

    # Define the path to the folder containing the rasters
    rasters = sys.argv[2]

    # Define the output folder
    out = rasters + "cropped/"

    # Create the output folder if it does not exist
    if not os.path.exists(out):
        os.makedirs(out)

    # Define the list of rasters
    rasters = glob.glob(rasters + "*.tif")

    # For loop to crop the rasters
    for raster in rasters:
        # Define the output file name
        out_raster = out + raster.split("/")[-1]
        # Crop the raster
        gdal.Warp(out_raster, raster, cutlineDSName=mshp, cropToCutline=True, dstNodata = -9999, outputType=gdal.GDT_Float32)

    # Print a message to the user
    print("The rasters have been cropped")


m_area(*sys.argv[1:])