from typing import List


def partition(array:List[int], lowerBound:int, upperBound:int) -> List[int]:
    pivot = array[upperBound]
    i = lowerBound - 1
    for j in range(lowerBound, upperBound):
        if array[j] <= pivot:
            i += 1 # i = i + 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[upperBound] = array[upperBound], array[i+1]
    print("pivot = "+str(array[i + 1]), array[lowerBound:upperBound+1])
    return i + 1


def quicksort(unsorted:List[int],lowerBound:int=None, upperBound:int=None )->List[int]:
    if lowerBound == None:
        lowerBound = 0
    if upperBound == None:
        upperBound = len(unsorted) - 1
    if lowerBound < upperBound:
        pivot = partition(unsorted, lowerBound=lowerBound, upperBound=upperBound)
        quicksort(unsorted, lowerBound=lowerBound, upperBound=pivot - 1)        
        quicksort(unsorted, lowerBound=pivot + 1, upperBound=upperBound)

x = [12,43,1,7,-12,-1992,4241,1,2,423,432,1,232,2]
quicksort(x)
print("SORTED LIST, ",x)