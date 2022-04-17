import retrieveData as rD
import getDayWithMostCases as gD

dummyDataSetRelativePath = "Data/dummy_data.csv"
dataSet = rD.retrieveData(dummyDataSetRelativePath)

if __name__ == "__main__":
    gD.getDayWithMostCases("Minnesota")