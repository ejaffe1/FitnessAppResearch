Ezra Jaffe 08/18/2021

apple_health_data_extractor.py

This program reorganizes the data from apple health csv files created by apple_health_data_parser.py. The StepCount.csv, DistanceWalkingRunning.csv, WalkingSpeed.csv, HeartRate.csv files are extracted and modified into StepsPerDay.csv, TotalDistancePerDay.csv, AvgWalkingSpeedPerDay.csv, AvgHeartRatePerDay.csv files. The original files contain large, raw data. The new files organize the data into a per day or an average basis.

Steps:
1) Place apple_health_data_extractor.py in same folder as CSV files created from apple-health-data-parser.py ( StepCount.csv, DistanceWalkingRunning.csv, WalkingSpeed.csv, HeartRate.csv)

2) Run apple_health_data_extractor.py in either IDLE or Terminal (No file paths needed)

3) New CSV Files will be created/re-written and placed in the stated folder

Note: Each CSV file has it’s own function, thus the main function has function calls to each one. If the user does not have a certain csv source file, that function can be commented out in main. 
