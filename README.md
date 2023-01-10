# Python scripts to Manipulate CHELSA data for using in ENMs

## clim.py

### Before Usage

1. Create a directory including the climatic data (i.e. CHELSA_bio1_1981-2010_V.2.1.tif, CHELSA_bio2_1981-2010_V.2.1.tif, ...) and note its path. Please do not combine datasets of different bioclimatic scenarios in this directory. Each scenario should be in different directory and each time you should run clim.py seperately.
2. Specify the path for your shapefile, which you will use as a template to remove non-continental areas.

### How to Use

Use the script, from bash commandline as ```python3 clim.py ./1981_2010/ ./sources/continents_aoi.shp```

This will crop specified area, resample resolution as 2.5 arc minutes, crop the area as (-20, 20, 60, 60) and reproject the rasters for EPSG:4326.

Resulting rasters are ready to use in maxent (After converting them to ASCII), and are named accordingly. Also, original rasters are deleted. If you need them for future use, save them in another directory.

### Modifiable Settings

Modifiable settings are resolution, cropping area and projection setting. Here is the example code:

```python3 clim.py ./1981_2010/ ./sources/continents_aoi.shp "EPSG:4326" "-20, 20, 60, 60" 0.041666666666667```

* First argument (./test) defines the directory of bioclimatic variables.
* Second argument (./sources/continents_aoi.shp) defines the shapefile of continents, as CHELSA dataset includes oceans, you should cut these areas, if you are working with terrestrial organisms. This continents shapefile must be prepared with the same boundaries as the fourth argument.
* Third argument ("EPSG:4326") defines the projection.
* Fourth argument ("-20, 20, 60, 60") defines the crop area in the order of (minX, minY, maxX, maxY). Be careful because some tools use it in different order.
* Fifth argument (0.041666666666667) defines the resolution of the data. Here 0.041666666666667 is equal to 2.5 arc minutes.

## m_shp.py

This script will create a minimum convex polygon with a desired buffer distance.

### Before Usage

(You will need to install fiona and shapely packages for python3 to use this script.)
1. Specify the path to your species.csv file. We are following KUENM's format, so csv file should have 3 columns and ordered like: species, longitude and latitude.
2. Specify the buffer distance in degrees.
3. Specify the name of the output file. If not, the file will be named as mcp.shp.

### How to Use

Use the script, from bash commandline as ```python3 m_shp.py test_mcp/Hmarginatum_joint.csv 0.9 test_mcp/mcp.shp```

This will crop create a buffer area of 0.9 degrees which is approximately 100kms around your species.csv file and create a minimum convex polygon accordingly.

### Modifiable Settings

Only modifiable setting is buffer distance. Here is the example code:

```python3 m_shp.py test_mcp/Hmarginatum_joint.csv 0.9 test_mcp/mcp.shp```

* First argument (test_mcp/Hmarginatum_joint.csv) defines the species coordinates csv file.
* Second argument (0.9) defines the buffer distance in degrees. The default value is 0.9 which is 100kms.
* Third argument ("test_mcp/mcp.shp") defines the output file.

## m_area.py

This script will crop rasters according to the shapefile which is created from m_shp.py.

### Before Usage

1. Specify the path to your shapefile which will be used as a template for cropping.
2. Specify the path to your m_area rasters. 

### How to Use

Use the script, from bash commandline as ```python3 m_area.py test_mcp/mcp.shp test_marea/```

This will crop your rasters by using mcp.shp as a template. M_area rasters could be the resulting rasters from clim.py.

### Modifiable Settings

There is no modifiable setting here. The code is:

```python3 m_area.py test_mcp/mcp.shp test_marea/```

* First argument (test_mcp/mcp.shp) defines the path to shapefile which will be used as the template to crop the rasters.
* Second argument ("test_marea/") defines the path to rasters which will be cropped. The script will create ```cropped/``` directory in this directory and it includes all the cropped files.

## tif2asc.py

This script will convert TIFF rasters to ASCII rasters.

### Before Usage

1. Specify the path to your TIFF files. You can also add as many directories in that path. Script will convert contents of each directory in there. 

### How to Use

Use the script, from bash commandline as ```python3 m_area.py test```

This will convert every TIFF file in the directory, including the ones in different directories in that path.

### Modifiable Settings

There is no modifiable setting here. The code is:

```python3 tif2asc.py test```

* First argument (test_mcp/mcp.shp) defines the path to TIFF files or directories in there which include these files. 

## sets.py

This script will create directories in a structure compatible with KUENM R package. 

### Before Usage

1. Prepare all of your data (clip, convert, select), which is ready to use in Maxent. Put all of your G variables in a single directory.
2. Categorize variable sets. You can categorize them according to species needs or correlation thresholds. In this example they were categorized according to correlation thresholds and a .csv file was created. That file should be in the following format and named as sets.csv (You should not add the header. It is added for explanatory purposes):

| set | var 1 | var 2 | var 3 |var 4 | var 5| var 6| var 7| var 8| var 9|var 10|var 11|var 12|
|:---:| :---: | :---: | :---: |:---: | :---:| :---:| :---:| :---:| :---:|:---:|:---:|:---:|
| 0.9 | bio13 | bio14 | bio15 | bio2 | bio3 | bio4 | bio6 | bio7 | gdd0 | gsp | gst | npp |
| 0.8 | bio13 | bio14 | bio15 | bio2 | bio4 | bio6 | gst  |      |      |     |     |     |
| 0.7 | bio13 | bio2  | bio4  | bio6 | gst  |      |      |      |      |     |     |     |
| 0.6 | bio13 | bio2  | bio4  | gst  |      |      |      |      |      |     |     |     |

### How to Use

Use the script, from bash commandline as ```python3 sets.py```

This will create a G_variables directory and structure them to use for KUENM, accordingly.

### Modifiable Settings

There are no modifieble settings. You can only set different csv tables. You should not pass any arguments in the commandline, like the previous scripts.
