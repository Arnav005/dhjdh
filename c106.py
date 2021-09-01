import csv
import numpy as np

def getDataSource(data_path):   
    size_of_tv = []
    Average_time_spent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            Average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))

    return {"x": size_of_tv, "y": Average_time_spent}

def find_correlation(datasource):

      correlation= np.corrcoef( datasource["x"],datasource["y"])
      print("Correlation :-\n--->",correlation[0,1]) 

def setup():
     
    data_path = "c106data.csv" 
    datasource = getDataSource(data_path) 
    find_correlation(datasource)
            
setup()            