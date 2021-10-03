#Ezra Jaffe
#08/18/2021
import os
import csv

def main():
    #Run Functions
    StepsPerDay()
    AvgHeartRatePerDay()
    TotalDistancePerDay()
    AvgWalkingSpeedPerDay()

    
#Functions for each CSV file
    
def StepsPerDay():
    
    #Apple Health File 'StepCount.csv' is Required to Run this Function

    #Initialize 'StepsPerDay.csv'
    with open('StepsPerDay.csv', 'w', newline='') as f:
            csvWriter = csv.writer(f, delimiter=',');
            csvWriter.writerow(['date','total steps','iPhone steps','watch steps'])
            f.close()

    #Open Apple Health File 'StepCount.csv'
    with open('StepCount.csv', 'r') as f:

        #Varaible Initializations
        csvReader=csv.reader(f)
        count=0
        phoneCount=0
        watchCount=0
        prevDate=''
        next(csvReader)

        #CSV PARSER
        for line in csvReader:

            #Extract Date
            timestamp=line[6]
            splitter=str(timestamp)
            tslist=splitter.split()
            date=tslist[0]
            deviceName=line[0]

            #Adds equivalent date's values
            if date==prevDate:
                count+=int(line[8])

                #Conditionals to account for iPhone and Watch steps
                if ('iPhone' in deviceName):
                    phoneCount+=int(line[8])
                else:
                    watchCount+=int(line[8])
                    
            #Once the date changes, write to 'StepsPerDay.csv'  
            if date!=prevDate:
                
                #Open 'StepsPerDay.csv'
                with open('StepsPerDay.csv', 'a+', newline='') as t:
                        csvWriter = csv.writer(t, delimiter=',');

                        #Write date and counts to 'StepsPerDay.csv'
                        if prevDate!='':
                            csvWriter.writerow([prevDate,count,phoneCount,watchCount])

                        count=int(line[8]) #New date first value

                        #Conditionals to account for iPhone and Watch steps
                        if ('iPhone' in deviceName):
                            phoneCount=int(line[8])
                            watchCount=0
                        else:
                            watchCount=int(line[8])
                            phoneCount=0
                            
            #Previous Date Recorded                
            prevDate=date

        #Open 'StepsPerDay.csv' to append final line
        with open('StepsPerDay.csv', 'a+', newline='') as t:
            csvWriter = csv.writer(t, delimiter=',');
            csvWriter.writerow([prevDate,count,phoneCount,watchCount])

    print('STEPS PER DAY COMPLETED')


def AvgHeartRatePerDay():
    
    #Apple Health File 'HeartRate.csv' is Required to Run this Function

    #Initialize 'AvgHeartRatePerDay.csv'
    with open('AvgHeartRatePerDay.csv', 'w', newline='') as f:
            csvWriter = csv.writer(f, delimiter=',');
            csvWriter.writerow(['date','average heart rate'])
            f.close()

    #Open Apple Health File 'HeartRate.csv'        
    with open('HeartRate.csv', 'r') as f:

        #Varaible Initializations
        csvReader=csv.reader(f)
        count=0
        totCount=1
        prevDate=''
        next(csvReader)
        
        #CSV PARSER
        for line in csvReader:

            #Extract Date
            timestamp=line[5]
            splitter=str(timestamp)
            tslist=splitter.split()
            date=tslist[0]

            #Adds equivalent date's values
            if date==prevDate:
                count+=float(line[8])
                totCount+=1

            #Once the date changes, write to 'AvgHeartRatePerDay.csv'
            if date!=prevDate:

                #Open 'AvgHeartRatePerDay.csv'
                with open('AvgHeartRatePerDay.csv', 'a+', newline='') as t:
                        csvWriter = csv.writer(t, delimiter=',');
                        count=count/totCount #Equation for Average HeartRate

                        #Write date and counts to 'AvgHeartRatePerDay.csv'
                        if prevDate!='':
                            csvWriter.writerow([prevDate,count])

                        count=float(line[8]) #New date's first value
                        totCount=1 #Total count reset
                        
            #Previous Date Recorded         
            prevDate=date

        #Open 'AvgHeartRatePerDay.csv' to append final line
        with open('AvgHeartRatePerDay.csv', 'a+', newline='') as t:
            csvWriter = csv.writer(t, delimiter=',');
            count=count/totCount
            csvWriter.writerow([prevDate,count])

    print('AVG HEART RATE COMPLETED')


def TotalDistancePerDay():
    
    #Apple Health File 'DistanceWalkingRunning.csv' is Required to Run this Function

    #Initialize 'TotalDistancePerDay.csv'
    with open('TotalDistancePerDay.csv', 'w', newline='') as f:
            csvWriter = csv.writer(f, delimiter=',');
            csvWriter.writerow(['date','total distance (miles)'])
            f.close()

    #Open Apple Health File 'DistanceWalkingRunning.csv'
    with open('DistanceWalkingRunning.csv', 'r') as f:

        #Varaible Initializations
        csvReader=csv.reader(f)
        count=0
        prevDate=''
        next(csvReader)

        #CSV PARSER
        for line in csvReader:

            #Extract Date
            timestamp=line[6]
            splitter=str(timestamp)
            tslist=splitter.split()
            date=tslist[0]

            #Adds equivalent date's values
            if date==prevDate:
                count+=float(line[8])

            #Once the date changes, write to 'TotalDistancePerDay.csv'
            if date!=prevDate:

                #Open 'TotalDistancePerDay.csv'
                with open('TotalDistancePerDay.csv', 'a+', newline='') as t:
                        csvWriter = csv.writer(t, delimiter=',');

                        #Write date and counts to 'TotalDistancePerDay.csv'
                        if prevDate!='':
                            csvWriter.writerow([prevDate,count])
                            
                        count=float(line[8]) #New date's first value

            #Previous Date Recorded  
            prevDate=date

        #Open 'TotalDistancePerDay.csv' to append final line
        with open('TotalDistancePerDay.csv', 'a+', newline='') as t:
            csvWriter = csv.writer(t, delimiter=',');
            csvWriter.writerow([prevDate,count])

    print('TOTAL DISTANCE COMPLETED')


def AvgWalkingSpeedPerDay():
    
    #Apple Health File 'WalkingSpeed.csv' is Required to Run this Function

    #Initialize 'AvgWalkingSpeedPerDay.csv'
    with open('AvgWalkingSpeedPerDay.csv', 'w', newline='') as f:
            csvWriter = csv.writer(f, delimiter=',');
            csvWriter.writerow(['date','average walking speed (mi/hr)'])
            f.close()

    #Open Apple Health File 'WalkingSpeed.csv'
    with open('WalkingSpeed.csv', 'r') as f:

        #Varaible Initializations
        csvReader=csv.reader(f)
        count=0
        totCount=1
        prevDate=''
        next(csvReader)
        
        #CSV PARSER
        for line in csvReader:

            #Extract Date
            timestamp=line[5]
            splitter=str(timestamp)
            tslist=splitter.split()
            date=tslist[0]

            #Adds equivalent date's values
            if date==prevDate:
                count+=float(line[8])
                totCount+=1

            #Once the date changes, write to 'AvgWalkingSpeedPerDay.csv'
            if date!=prevDate:

                #Open 'AvgWalkingSpeedPerDay.csv'
                with open('AvgWalkingSpeedPerDay.csv', 'a+', newline='') as t:
                        csvWriter = csv.writer(t, delimiter=',');
                        count=count/totCount #Equation for Average Walking Speed

                        #Write date and counts to 'AvgWalkingSpeedPerDay.csv'
                        if prevDate!='':
                            csvWriter.writerow([prevDate,count])
                            
                        count=float(line[8]) #New date's first value
                        totCount=1 #Total count reset

            #Previous Date Recorded              
            prevDate=date

        #Open 'AvgWalkingSpeedPerDay.csv' to append final line
        with open('AvgWalkingSpeedPerDay.csv', 'a+', newline='') as t:
            csvWriter = csv.writer(t, delimiter=',');
            count=count/totCount
            csvWriter.writerow([prevDate,count])
            
    print('AVG WALKING SPEED COMPLETED')
    
#Run Main Function
main()
