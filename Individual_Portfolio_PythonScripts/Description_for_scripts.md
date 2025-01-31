# Python scripts I have developed during the course of Data Science for Smart Environments with the Learning goal they reflect.

## A) Training for Goal 1 (`trainingGoal1.py`)  G1

In this script I tried to apply the knowledge and skills for small adhoc tasks in a separte python file.
I tried to apply basic libraries like numpy and pandas which I wanted to improve in my first learning goal.
The rest of the scripts were focused on the group project to which we dedicated the majority of the course time.

These following scripts were developed to download, process, analyse and produce meaningful results for the Project of Wind Energy in the Netherlands.
Scripts in this repository are only the scripts developed by Michal Bartek and for the full functionality they need to be grouped with other scripts for the Project.
I add the csvs used for these scripts for the replicability: some alterations need to be done in the paths and installations of the libraries for smooth implementation.

## 1. Downloading (`a01_WINS50_v2.py`)  G1
This script downloads the `.nc` files from the API for the square approximately fitting the land area of the Netherlands. Since WIN50 includes many locations in the North Sea far from the Netherlands, only relevant data is retrieved.

## 2. Transforming (`a02_NcToShp.py`)  G1
This script transforms the `.nc` files into shapefiles, but only retains points that fit within the (bbox) land area of the Netherlands. This is determined by intersecting the dataset with a shapefile of the Netherlands.

## 3. Aggregating (`a03_toLargeShp.py`)  G1
This script merges all individual shapefiles into a single large shapefile.

## Additional Processing (done outside of Python) 
- Converting the original windmill locations into the correct Coordinate Reference System (CRS).  
- Using ArcGIS to buffer the original wind turbines and clip the measurements, ensuring only measurements near actual wind turbines are retained.

# Energy Production and Machine Learning Analysis

## 4. Energy Production Analysis  
- **(`b04_HarmonieEnergyProduced.py` / `b04_StationsEnergyProduced.py`)**  G3
  Code that analyzes the energy produced, building upon the work from Dylan.  

- **(`ap04_timeformatting.py`)**  G1
  A small script that manipulates the time format for both Harmonie and station data.  

- **(`bF04_StationsFormatting.py`)**  G1
  Script that further formats station data for energy production graphs.  

## 5. Preparing Data for Machine Learning and Comparison  
- **Processing the data for possible ML and further investigation**  
  This step involves preparation for ML analysis, including correlation and regression studies.  

- **(`b05_ML_FormatVariables.py`)**  G1
  Adds the variable **"distance to coast,"** which proves to be important for predictions.  
  Direct analyses of the predictors are included in the code.  

- **(`b05_ML_FormatVariables_Stations.py`)**  G1
  Adds the distance from the coast for station data.  
  Direct analyses of the predictors are included in the code.  

## 6. Comparing Data: Harmonie vs. Station Data  
- **(`a06_HarmonieStationsComparison.py`)**  G3/G1
  Script that compares Station and Harmonie data.  
