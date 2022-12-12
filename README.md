# DataPrepCHELSA

## Python script to Manipulate CHELSA data

1. Create a directory including the climatic data (i.e. CHELSA_bio1_1981-2010_V.2.1.tif, CHELSA_bio2_1981-2010_V.2.1.tif, ...) and note its path.
2. Specify the path for your shapefile, which you will use as a template to remove non-continental areas.

Use the script, from bash commandline as ```clim.py ./1981_2010/ ./sources/continents_aoi.shp```

This will crop specified area, resample resolution as 2.5 arc minutes, crop the area as (-20, 20, 60, 60) and reproject the rasters for EPSG:4326.

Updates to modify these predetermined variables are coming soon...
