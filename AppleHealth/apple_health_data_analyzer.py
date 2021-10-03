#Ezra Jaffe
#08/20/2021

import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

def main():
    #Files created from "apple_health_data_extractor.py"
    Outliers('StepsPerDay.csv')
    Outliers('TotalDistancePerDay.csv')
    Outliers('AvgWalkingSpeedPerDay.csv')
    Outliers('AvgHeartRatePerDay.csv')
    print('ALL DONE')

#Outliers Function standardizes the data from these csv files and documents the outliers (3 standard deviations away from mean)
def Outliers(csvFile):

    #CSV to Panda Data Frame
    csv=pd.read_csv(csvFile)
    csvStd=csv.copy()
    columnList=list(csv.columns)
    
    #Standardization Equation
    csvStd[columnList[1]]=(csvStd[columnList[1]] - csvStd[columnList[1]].mean()) / csvStd[columnList[1]].std()

    #Outlier Array Initializer
    rows,cols=(len(csv)-1,2)
    data_arr = [[0 for i in range(cols)] for b in range(rows)] 

    #Loop to search for outlier data (looking for z scores either greater than 3 or less than -3)
    j=0
    for i in range(0,len(csvStd)-1):
        z_score= csvStd.loc[i][columnList[1]]
        if z_score>3 or z_score<-3:
            data_arr[j][0]= csv.loc[i][columnList[0]]
            data_arr[j][1]= csv.loc[i][columnList[1]]
            j=j+1
    
    fileName=csvFile[:len(csvFile)-4]

    #Plot Data
    #StepsPerDay has different process due to having total steps, iPhone steps, and watch steps
    if(fileName=='StepsPerDay'):
        #All types of steps
        graph=csv.plot(figsize=(30,15), title=fileName).get_figure()
        graph.savefig('%s_Plot.pdf' % fileName)

        #Total steps only
        graph=csvStd.plot.scatter(x='date', y=columnList[1], figsize=(30,15), title=fileName).get_figure()
        graph.savefig('%sTOTAL_ONLY_Plot.pdf' % fileName)
        
    else:
        #All other files graphs
        graph=csv.plot.scatter(x='date', y=columnList[1], figsize=(30,15), title=fileName).get_figure()
        graph.savefig('%s_Plot.pdf' % fileName)

    #Transfer data from array into data frame
    outliers=pd.DataFrame(data_arr,columns=[columnList[0],columnList[1]])
    outliers=outliers.drop(range(j,len(outliers)))

    #Outlier Plots
    outlierGraph=outliers.plot.scatter(x='date', y=columnList[1], s=70, figsize=(15,5), title='%s Outliers' % fileName).get_figure()
    outlierGraph.savefig('%s_Outlier_Plot.pdf' % fileName)

    #CSV File creation
    outliers.to_csv('%s_Outliers.csv' % fileName,index=False,sep=',',encoding='utf-8')

#Run Main Function
main()
