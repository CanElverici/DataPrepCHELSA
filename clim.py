#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob, sys, os
from osgeo import gdal

# If sys.argv[3,4 and 5] are not defined, the script will run with the default values
# If sys.argv[3,4 and 5] are defined, the script will run with the values defined by the user
# The default values are: proj = "EPSG:4326", oubound = (-20, 20, 60, 60), res = 0.041666666666667

def main(dirpath, contpathfile, proj = "EPSG:4326", oubound = (-20, 20, 60, 60), res = 0.041666666666667):  # WORK on implementing the arguments
    # Define all the files in the folder as a list named tifs
    pathini = sys.argv[1]
    continents = sys.argv[2]
    tifs = glob.glob(os.path.join(pathini, "*.tif"))                        
    print(tifs)

    # For loop to reproject, crop and rename appropriate to maxent for all the files in the list
    for tif in tifs:
        # Open the file
        ds = gdal.Open(tif)
        # Define the output file name
        out = tif[:-4] + "_reprojected.tif"
        # Define the output projection
        # The default projection is WGS84 (EPSG:4326)
        # The projection can be changed by the user in the input arguments
        if len(sys.argv) > 3:
            proj = sys.argv[3]
        else:
            proj = "EPSG:4326"
        # Define boundaries of the output file
        # The boundaries are defined by the coordinates of the lower left and upper right corners
        # The coordinates are in the order of (minX, minY, maxX, maxY) default is (-20, 20, 60, 60)
        # The boundaries can be changed by the user in the input arguments
        if len(sys.argv) > 4:
            # Take arguments from the command line and convert them to a tuple
            oubound = tuple(map(float, sys.argv[4].split(",")))
        else:
            oubound = (-20, 20, 60, 60)
        # Define the output resolution for x and y
        # For this, output resolution is equal to 2.5 arc minutes as default
        # The resolution can be changed by the user in the input arguments
        if len(sys.argv) >= 5:
            res = float(sys.argv[5])
        else:
            res = float(0.041666666666667)
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
    d01 = "_1981-2010"
    d02 = "_2011-2040"
    d03 = "_2041-2070"
    d04 = "_2071-2100"
    d05 = "_ssp126"
    d06 = "_ssp370"
    d07 = "_ssp585"
    d08 = "_mri-esm2-0"
    d09 = "_mpi-esm1-2-hr"
    d10 = "_ukesm1-0-ll"
    d11 = "_ipsl-cm6a-lr"
    d12 = "_gfdl-esm4"
    d13 = "_V.2.1_reprojected_cropped"
    # For loop to rename the files
    for outfile in outfiles:
        newname = outfile.replace("CHELSA_", "") \
       .replace(d01, "") \
       .replace(d02, "") \
       .replace(d03, "") \
       .replace(d04, "") \
       .replace(d05, "") \
       .replace(d06, "") \
       .replace(d07, "") \
       .replace(d08, "") \
       .replace(d09, "") \
       .replace(d10, "") \
       .replace(d11, "") \
       .replace(d12, "") \
       .replace(d13, "")
        print(newname)
        gdal.Rename(outfile, newname)

    # Remove the input and the intermediate files
    # Files beginning with "CHELSA" are to be removed
    dst_delete = glob.glob(pathini + "CHELSA_*")
    for file in dst_delete:
        os.remove(file)

main(*sys.argv[1:])
