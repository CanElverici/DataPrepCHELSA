#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
from osgeo import gdal
import numpy as np
import sys

def main(dirpath, contpathfile, proj = "EPSG:4326", oubound = (-20, 20, 60, 60), res = 0.041666666666667):  # WORK on implementing the arguments
    # Define all the files in the folder as a list named tifs
    pathini = sys.argv[1]
    continents = sys.argv[2]
    tifs = glob.glob(pathini + "*.tif")                        
    print(tifs)

    # For loop to reproject, crop and rename appropriate to maxent for all the files in the list
    for tif in tifs:
        # Open the file
        ds = gdal.Open(tif)
        # Define the output file name
        out = tif[:-4] + "_reprojected.tif"
        # Define the output projection
        proj = proj
        # Define boundaries of the output file
        # The boundaries are defined by the coordinates of the lower left and upper right corners
        # The coordinates are in the order of (minX, minY, maxX, maxY) default is (-20, 20, 60, 60)
        oubound = oubound
        # Define the output resolution for x and y
        # For this, output resolution is equal to 2.5 arc minutes as default
        resx = res
        resy = -1 * res
        # Reproject and resample the file
        gdal.Warp(out, ds, dstSRS=proj, outputBounds=oubound, xRes=resx, yRes=resy)
        # Crop the file using the boundaries of the continents
        out2 = tif[:-4] + "_reprojected_cropped.tif"
        gdal.Warp(out2, out, cutlineDSName=continents, cropToCutline=True, dstNodata = -9999, outputType=gdal.GDT_Float32)

    # Find the output files and rename them by removing the "CHELSA_" and "_1981-2010_V.2.1_reprojected_cropped" part
    outfiles = glob.glob(pathini + "*_reprojected_cropped.tif")
    print(outfiles)
    # Define the strings to be replaced
    replace1 = "_1981-2010_V.2.1_reprojected_cropped"
    replace2 = "_2011-2040_mri-esm2-0_ssp370_V.2.1_reprojected_cropped"
    for outfile in outfiles:
        newname = outfile.replace("CHELSA_", "").replace(replace1, "").replace(replace2, "")
        print(newname)
        gdal.Rename(outfile, newname)


main(sys.argv[1], sys.argv[2])