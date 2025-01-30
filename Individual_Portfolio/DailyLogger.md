# Daily Log of the Workload from the Entire Course

*from week2 I have started to attribute the workload of each day to the specific learning goals.

## Week 1

### Day 1.1
- Getting myself familiar with the projects.
- Brainstorming possible data issues we can solve in a project during the course.

### Day 1.2
- Studying the documentation of the data featured in the description of the project.
- Learning the downloading system of KNMI and Harmonie versions.
- Studying the API tokens.
- Copy/making a script that downloads the data from HARMONIE.
- Problem with the size of the data.

### Day 1.3
- Acquaintance with the Jupyter notebooks.
- Continuous search for ideal data.
- Conversion of the nc file into the shp file.
- Filtering the data.

### Day 1.4
- Exploring the capabilities of the API call for the wins50 data.
- Matching the data from the windmills to the Netherlands geography.
- Preparing the presentation for the project proposal.

### Day 1.5
- **Personal learning plan**: 10:00 - 12:00
- **14:00 - 18:00**: Working on the selection of the windmills only within the administrative boundaries of the Netherlands using the GeoJSON file of the Netherlands. 
- Matching the windmills to the measurements of the Harmonie model.

## Week 2

### Day 2.1
- The intro to the Databases.
- ex01 and ex03 on the databases.
- A look into the GitHub on APIs. Interest found in looking into the publicly available APIs: [public-apis](https://github.com/public-apis/public-apis).

### Day 2.2
- Lecture on ML and data wrangling.
- Learned new ways how to deal with the NaNs.
- Object-oriented programming use in the ML problem.
- Struggling with ArcGIS Pro to match the turbines and stations/Harmonie.
- Managed to match the Harmonie and turbines into one dataset.
- Communication in team about further progress G2.
- Communication about the ethics posters and preliminary analyses.

### Day 2.3
- Work on the project. Preliminary analysis and statistics.
- Analyzing the windspeeds at 10m height. Developing python code to correctly read and plot the windspeeds throughout the year. Pandas library G1.
- Working on the ethics poster.

### Day 2.4
- Making a setup for the day: Watch the content of the day, make notes, review ML day, work on the project, and explore the data further.
- Identifying the potential to use OOP. Making the class of height wind turbine analysis.
- Producing the graph for the analysis of wind turbine 1 and different windspeeds at different heights during the year.
- Setting up an analysis to statistically see if there is a relationship between heights and windspeeds in the example of WT1. G3.
- Resolving the issue of the missing wind turbines 13 and 38.

### Day 2.5
- Presentations.
- Figuring out which ML could suit our project. Structuring the further process in ML. G3.
- The idea to derive “distance to coast variable” as a predictor for the energy/wind speed.
- The algorithm with the best fit for us: “random forest” as a regression problem.
- First ideas of the code and library we need to use: **scikit-learn** G1.
- Plotting additional analyses on different wind turbines to gain more data insights.

## Week 3

### Day 3.1
- Lecture on ethics - making notes, connecting the concepts to our project. G4.
- Scripting the plot of all the measurements for all the turbines throughout the year. Playing around with the classes and practicing the structure of Object-oriented programming. G1.
- Discussing some formatting issues with the team. G2.
- Working on selecting the measurements closest to the ash of the windmills.

### Day 3.2
- The clustering lecture.
- Working on the column distance to coast, which would be one of the predictors for the models.
- Turns out to be more difficult than thought. Problems with the coordinate system, defining the coast from the JSON file. Eventually got the variable distance to coast in meters. G1.
- Working on the regression to investigate the preliminary relationship. G3.

### Day 3.3
- Visualization lecture.
- The correlation plot. G3.
- Struggling with the joins. Ethics posters finish. G4.
- Making decisions with the team regarding the station data (proceed with the limited amount of data or try more techniques to match it).
- Formatting the station data.
- Trying to utilize the station data with the code made for Harmonie.
- Struggle: different variable formats, names, structuring.

### Day 3.4
- Station data analysis extra quickly to catch up with the rest of the project.
- The comparison analysis of the Stations and the Harmonie. G3.
- The ethics debate with other groups. G4.
- Working on the presentation, setting the order, the people presenting. G2.

### Day 3.5
- Finishing the presentation.
- Documenting the code and uploading it to GitHub.
- Presentation.
- Finishing the submission, zipping the final folder.
