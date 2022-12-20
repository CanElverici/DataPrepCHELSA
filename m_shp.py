#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import fiona
from shapely.geometry import shape, mapping, Point, Polygon
from shapely.ops import unary_union
from sys import argv as sa

# Define a function to create a buffer around coordinates from a csv file
# and create an minimum convex polygon from that buffer
# 1 degree is approximately 111 km, so if you want 100 km buffer, you should use 0.9 degrees
# We are following KUENM's format, so csv file should have 3 columns and ordered like: species, longitude and latitude
def m_shp(csv_file = sa[1], buffer_distance = sa[2], output_file = sa[3]):
    # If sa[3] is not defined, the script will run with the default value
    # If sa[3] is defined, the script will run with the value defined by the user
    # The default value is: output_file = "mcp.shp"
    if len(sa) > 3:
        output_file = sa[3]
    else:
        output_file = "mcp.shp"

    # If sa[2] is not defined, the script will run with the default value
    # If sa[2] is defined, the script will run with the value defined by the user
    # The default value is: buffer_distance = 0.9
    if len(sa) > 2:
        buffer_distance = float(sa[2])
    else:
        buffer_distance = 0.9
        
    # If sa[1] is not defined, the script will run with the default value
    # If sa[1] is defined, the script will run with the value defined by the user
    # The default value is: csv_file = "coordinates.csv"
    if len(sa) > 1:
        csv_file = sa[1]
    else:
        csv_file = "coordinates.csv"

    # Open the csv file
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        # Create a list of coordinates from the csv file
        coordinates = list(reader)
    
    # Create a list of shapely points from the coordinates, there is header in the csv file, so we start from the second row
    points = [Point(float(x[1]), float(x[2])) for x in coordinates[1:]]

    # Create a list of buffers from the points, the buffer distance is defined by the user and is in degrees
    buffers = [x.buffer(buffer_distance) for x in points]
    
    # Create a minimum convex polygon from the buffers
    mcp = unary_union(buffers).convex_hull
    
    # Create a polygon feature from the minimum convex polygon
    polygon = {'type': 'Feature',
               'properties': {'species': str(coordinates[0][0])},
               'geometry': mapping(mcp)}

    # Define the schema of the shapefile
    schema = {'geometry': 'Polygon', 'properties': {'species': 'str'}}

    # Define the coordinate reference system of the shapefile
    crs1 = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'

    # Write the polygon feature to a shapefile
    with fiona.open(output_file, 'w', 'ESRI Shapefile', schema, crs = crs1) as output:
        output.write(polygon)


m_shp(*sa[1:])