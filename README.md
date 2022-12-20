# DataPrepCHELSA

## Python script to Manipulate CHELSA data for using in ENMs

### clim.py

#### Before Usage

1. Create a directory including the climatic data (i.e. CHELSA_bio1_1981-2010_V.2.1.tif, CHELSA_bio2_1981-2010_V.2.1.tif, ...) and note its path. Please do not combine datasets of different bioclimatic scenarios in this directory. Each scenario should be in different directory and each time you should run clim.py seperately.
2. Specify the path for your shapefile, which you will use as a template to remove non-continental areas.

#### How to Use

Use the script, from bash commandline as ```clim.py ./1981_2010/ ./sources/continents_aoi.shp```

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
