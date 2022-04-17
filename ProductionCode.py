import retrieveData as rD
import getDayWithMostCases as gD
dataSet = rD.retrieveData()

if __name__ == "__main__":
    gD.getDayWithMostCases("Minnesota")
