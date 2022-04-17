import retrieveData as rD
import getDayWithMostCases as gD

relativeDataPath = "Data/dummy_data.csv"
dataSet = rD.retrieveData()

if __name__ == "__main__":
    gD.getDayWithMostCases("Minnesota")