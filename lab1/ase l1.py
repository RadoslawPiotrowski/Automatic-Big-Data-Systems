import time
import numpy as np

#DATA GENERATION
numberOfElements = 1000
data = np.random.randint(2, size=numberOfElements)

#BABELKOWE SORTOWANIE

samples = np.copy(data)

def bubbleSorting(array):
    arrayLen = len(array)
    for i in range(arrayLen):
        for j in range(0, arrayLen-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

# SORTING BY EXCHANGE
newSamples  = np.copy(data)

def exchangeSorting(array):
    for i in range (numberOfElements):
        lowerDigIdx =  np.argmin(array[i:])
        buf = array[i]                 # saving the 0, 1, 2 element
        array[i] = array[lowerDigIdx + i]
        array[lowerDigIdx + i] = buf

# SORTING BY QUICKSORT

qkSort  = np.copy(data)

def part(array, leftIdx,rightIdx):
    pivotIdx = leftIdx
    pivotVal = array[rightIdx]
    for i in range(leftIdx,rightIdx):
        if array[i] <= pivotVal:
            array[i], array[pivotIdx] = array[pivotIdx], array[i]
            pivotIdx += 1
    array[rightIdx], array[pivotIdx] = array[pivotIdx], array[rightIdx]
    return pivotIdx

def quickSortWhole(array, leftIdx, rightIdx):
    if(leftIdx < rightIdx):
        pIndex = part(array,leftIdx,rightIdx)
        quickSortWhole(array,leftIdx, pIndex -1)
        quickSortWhole(array,pIndex + 1, rightIdx)

print ("BUBBLE SORTING START")
start = time.time()
bubbleSorting(samples)
sortingTimeOne = time.time() - start
print ("BUBBLE SORTING END")
print("EXCHANGE SORTING START")
start1 = time.time()
exchangeSorting(newSamples)
sortingTimeTwo = time.time() - start1
print("EXCHANGE SORTING END")
print("QUICKSORT START")
start2 = time.time()
quickSortWhole(qkSort, 0, numberOfElements -1)
sortingTimeThird = time.time() - start2
print("QUICKSORTEND")

print("TIMES: ")
print(sortingTimeOne)
print(sortingTimeTwo)
print(sortingTimeThird)

# def quickSort(array, leftidX, rightidX):
#         pivotIdx = np.random.randint(leftidX, rightidX)
#         pivotVal = array[pivotIdx]
#         # print ("PivotValue", array[pivotIdx])
#         print(array)
#         while(leftidX < rightidX):
#             for i in range (leftidX, rightidX):
#                 if array[i] >= pivotVal:
#                     leftidX = i
#                     # print("LEFT: ",array[leftidX])
#                     break
#             for j in range(rightidX, leftidX, -1):
#                 if array[j] <= array[leftidX] and array[j] <= pivotVal:
#                     rightidX = j
#                     # print("RIGHT: ",array[rightidX])
#                     break
#             if(array[leftidX] >= pivotVal >= array[rightidX] and leftidX < rightidX):
#                 # print(array[leftidX], array[rightidX])
#                 buf = array[leftidX]
#                 array[leftidX] = array[rightidX]
#                 array[rightidX] = buf
#                 leftidX += 1
#             else: leftidX += 1
#             if(leftidX >= rightidX): break
#             # print(array)
#         return pivotIdx
