Ezra Jaffe 08/20/2021

apple_health_data_analyzer.py

This program standardizes the data from apple health csv files created by apple_health_data_extractor.py. The standardized data is searched through to find Z scores either greater than 3 or less than -3. This is 3 standard deviations which indicates an outlier. The outliers are placed into a data array, then a csv data file for each respective data set. The program also creates scatter plots for all the data sets and the outlier data sets.

Steps:
1) Place apple_health_data_analyzer.py in same folder as CSV files created from apple_health_data_extractor.py ( StepsPerDay.csv, TotalDistancePerDay.csv, AvgWalkingSpeedPerDay.csv, AvgHeartRatePerDay.csv)

2) Run apple_health_data_analyzer.py in either IDLE or Terminal (No file paths needed)

3) Outlier CSV Files and graph pdf files will be created and placed in the stated folder
