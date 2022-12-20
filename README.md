# DataPrepCHELSA

## Python script to Manipulate CHELSA data for using in ENMs

### clim.py

#### Before Usage

1. Create a directory including the climatic data (i.e. CHELSA_bio1_1981-2010_V.2.1.tif, CHELSA_bio2_1981-2010_V.2.1.tif, ...) and note its path. Please do not combine datasets of different bioclimatic scenarios in this directory. Each scenario should be in different directory and each time you should run clim.py seperately.
2. Specify the path for your shapefile, which you will use as a template to remove non-continental areas.

#### How to Use

Use the script, from bash commandline as ```python3 clim.py ./1981_2010/ ./sources/continents_aoi.shp```

This will crop specified area, resample resolution as 2.5 arc minutes, crop the area as (-20, 20, 60, 60) and reproject the rasters for EPSG:4326.

Resulting rasters are ready to use in maxent, and are named accordingly.

#### Modifiable Settings

Modifiable settings are resolution, cropping area and projection setting. Here is the example code:

```python3 clim.py ./1981_2010/ ./sources/continents_aoi.shp "EPSG:4326" "-20, 20, 60, 60" 0.041666666666667```

* First argument (./test) defines the directory of bioclimatic variables.
* Second argument (./sources/continents_aoi.shp) defines the shapefile of continents, as CHELSA dataset includes oceans, you should cut these areas, if you are working with terrestrial organisms. This continents shapefile must be prepared with the same boundaries as the fourth argument.
* Third argument ("EPSG:4326") defines the projection.
* Fourth argument ("-20, 20, 60, 60") defines the crop area in the order of (minX, minY, maxX, maxY). Be careful because some tools use it in different order.
* Fifth argument (0.041666666666667) defines the resolution of the data. Here 0.041666666666667 is equal to 2.5 arc minutes.

### m_shp.py

This script will create a minimum convex polygon with a desired buffer distance.

#### Before Usage

(You will need to install fiona and shapely packages for python3 to use this script.)
1. Specify the path to your species.csv file. We are following KUENM's format, so csv file should have 3 columns and ordered like: species, longitude and latitude.
2. Specify the buffer distance in degrees.
3. Specify the name of the output file. If not, the file will be named as mcp.shp.

#### How to Use

Use the script, from bash commandline as ```python3 m_shp.py test_mcp/Hmarginatum_joint.csv 0.9 test_mcp/mcp.shp```

This will crop create a buffer area of 0.9 degrees which is approximately 100kms around your species.csv file and create a minimum convex polygon accordingly.

#### Modifiable Settings

Only modifiable setting is buffer distance. Here is the example code:

```python3 m_shp.py test_mcp/Hmarginatum_joint.csv 0.9 test_mcp/mcp.shp```

* First argument (test_mcp/Hmarginatum_joint.csv) defines the species coordinates csv file.
* Second argument (0.9) defines the buffer distance in degrees. The default value is 0.9 which is 100kms.
* Third argument ("test_mcp/mcp.shp") defines the output file.

