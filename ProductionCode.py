import sys
import csv
import os
dataSet = []

def retrieveData(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    for i in lines:
        line = []
        for j in i.split(","):
            line.append(j)
        dataSet.append(line)
    file.close()

if __name__ == "__main__":
    cur_path = os.path.dirname(__file__)
    rel_path = "Data/dummy_data.csv"
    abs_file_path = os.path.join(cur_path, rel_path)
    retrieveData(abs_file_path)
    print(dataSet[1][1])