Ezra Jaffe 08/25/2021

FitReader.py

This program extracts raw data from .fit files. The .fit files of focus for this code are from the Strava app. Strava records each run/activity as fit files in the iPhone backup. This code extracts the date, time, distance, speed, latitude, and longitude, then stores them in the csv file ’StravaFitData.csv’. 

Steps to Run:
1) Locate the fit file in the backup using iExplorer and open the file in finder. The location in finder should be similar to this path:

/Users/ezrajaffe/Library/ApplicationSupport/MobileSync/Backup/ 00008020-00125C9E0AD0003A/4c/4cefc203052036353c44737b13fdb17b16aa15c2

This hash name: ‘4cefc203052036353c44737b13fdb17b16aa15c2’ will be different for each fit file.

2) Place FitReader.py and the fit file hash found from backup in the same folder (not the source folder).

3)Type name of file in the FitReader argument section:
E.g: with fitdecode.FitReader('4cefc203052036353c44737b13fdb17b16aa15c2') as fit:

3) Run FitReader.py in either IDLE or Terminal (No file paths needed)

4) StravaFitData.csv files will be created/re-written and placed in the stated folder. 
Note: The name of the created csv file can be altered by the user.
