import random
import numpy as np
numberOfElements = 5
data = np.random.randint(200, size=numberOfElements)
samples = np.copy(data)


def calculatePivValue():
    lowerDigIdx =  np.argmin(qckSort)
    higherDigIdx =  np.argmax(qckSort)
    closePivVal = (qckSort[higherDigIdx] - qckSort[lowerDigIdx]) / 2
    idx = (np.abs(qckSort - closePivVal)).argmin()
    return idx

# print(data)
#  BABELKOWE SORTOWANIE
isBiger = True
isSorted = False
while (isSorted == False):
    for i in range(numberOfElements -1,0,-1):
        if (samples[i] >= samples[i - 1]):
            isBiger = True
            isSorted = True
        else:
            isBiger = False
            buf = samples[i]
            samples[i] = samples[i - 1]
            samples[i - 1] = buf
            isSorted = False
            break

print ("KONIEC")
# SORTOWANIE POPRZEZ WYMIANE
newSamples  = np.copy(data)

print("ENETERING EXCHANGE SORTING")


for i in range (numberOfElements):
    lowerDigIdx =  np.argmin(newSamples[i:])
    buf = newSamples[i]                 # saving the 0, 1, 2 element
    newSamples[i] = newSamples[lowerDigIdx + i]
    newSamples[lowerDigIdx + i] = buf
print("EXCHANGE ARRAY SORTING ENDED")

print("ENETERING QUICKSORT")
qckSort = np.copy(data)
pivotIdx = calculatePivValue()

print("END OF QUICKSORT")
# print(calculatePivValue())
