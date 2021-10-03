#Ezra Jaffe
#08/25/2021

import os
import csv
from datetime import datetime
import fitdecode
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S"
prevDist='' #Initializer
with fitdecode.FitReader('4cefc203052036353c44737b13fdb17b16aa15c2') as fit:
    #2021.07.08-1625798747.785489.fit (iExplorer file name)
    
    #Create/reset CSV files
    with open('StravaFitData.csv', 'w', newline='') as f:
            csvWriter = csv.writer(f);
            fields= ['date','time','distance','speed','latitude','longitude']
            csvWriter.writerow(fields)

            for frame in fit:
                check = False
                if isinstance(frame, fitdecode.FitDataMessage):
                    #Variable Initializations for string values of data
                    sdate, stime, sdistance, sspeed, slat, slong=' ', ' ', ' ', ' ', ' ', ' '
                    
                    #If Statements to retreive specfic data fields
                    if frame.has_field('timer_trigger'):
                        print('timer_trigger:', frame.get_value('timer_trigger'))
                        
                    if frame.has_field('timestamp'):
                        #Retrieving timestamp value from fit file
                        timestamp=frame.get_value('timestamp')
                        
                        #UTC to Local Time (PDT) Conversion
                        
                        pacific_timestamp = timestamp.astimezone(timezone('US/Pacific'))
                        pacific_timestamp=pacific_timestamp.strftime(fmt)
                        
                        #Splitting timestamp into date and time
                        splitter=str(pacific_timestamp)
                        tslist=splitter.split()
                        stime=tslist[1]
                        sdate=tslist[0]

                        #print('timestamp:', sdate, stime)
                        
                    if frame.has_field('event_type'): 
                        print('event_type:', frame.get_value('event_type'))
                        
                    if frame.has_field('speed'):
                        speed=frame.get_value('speed')
                        sspeed=str(speed)
                        #print('speed:', speed)
                        
                    #distance is in meters
                    if frame.has_field('distance'):
                        check=True
                        distance=frame.get_value('distance')
                        sdistance=str(distance)
                        #print('distance:', distance)
                        
                    if frame.has_field('position_lat') and frame.has_field('position_long'):
                        lat=frame.get_value('position_lat')
                        long=frame.get_value('position_long')
                        lat=(lat/((2**32)/360)) #conversion for gps locations 
                        long=(long/((2**32)/360))
                        slat=str(lat)
                        slong=str(long)

                    if check==False:
                        sdistance=prevDist #Distance Value is recorded on a different data line; so this if statement adjusts it correctly
                        
                    if sdate!=' ' and slat!=' ': #CSV File Data Input 
                        csvWriter.writerow([sdate,stime,sdistance,sspeed,slat,slong])

                    prevDist=sdistance

    
#gps conversion: (num given)/((2**32)/360)

#Fields in FIT File:
                
##file_id
##time_created  
##type
##manufacturer
##product
##developer_data_id
##developer_data_index
##application_id
##application_version
##field_description
##fit_base_type_id
##field_definition_number
##field_name
##device_info
##device_model
##device_manufacturer
##device_os_version
##mobile_app_version
##timestamp
##battery_status
##record
##event
##event_type
##timer_trigger
##record
##distance
##record
##position_lat
##position_long
##enhanced_speed
##speed
##enhanced_altitude
##gps_accuracy


#Reference Site: https://towardsdatascience.com/parsing-fitness-tracker-data-with-python-a59e7dc17418

