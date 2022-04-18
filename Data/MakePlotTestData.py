import csv
import random
with open("us_simplified.csv") as file:
    lines = file.readlines()
numlines = len(lines)

randList = range(1,150)
newfile = open("plot_test_data.csv","w")
newfile.write(lines[0])
for i in randList:
    newfile.write(lines[i])
file.close()
newfile.close()