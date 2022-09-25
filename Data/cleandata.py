with open("Data/us_simplified.csv") as file:
    originalData = file.readlines()
originalData = originalData[1:]

path = "us_simplified_cleaned.csv"
newfile = open(path,"w")
for line in originalData:
    newfile.write(line[:-4])
    newfile.write("\n")