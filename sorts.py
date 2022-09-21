from typing import List

class Sorts:
    def __init__(self) -> None:
        pass

    def __partition(array:List[int], lowerBound:int, upperBound:int) -> List[int]:
        pivot = array[upperBound]
        i = lowerBound - 1
        for j in range(lowerBound, upperBound):
            if array[j] <= pivot:
                i += 1 # i = i + 1
                array[i], array[j] = array[j], array[i]
        
        array[i + 1], array[upperBound] = array[upperBound], array[i+1]
        print("pivot = "+str(array[i + 1]), array[lowerBound:upperBound+1])
        return i + 1

    def quicksort(self, unsorted:List[int],lowerBound:int=None, upperBound:int=None )->List[int]:
        if lowerBound == None:
            lowerBound = 0
        if upperBound == None:
            upperBound = len(unsorted) - 1
        if lowerBound < upperBound:
            pivot = self.__partition(unsorted, lowerBound=lowerBound, upperBound=upperBound)
            self.quicksort(unsorted, lowerBound=lowerBound, upperBound=pivot - 1)        
            self.quicksort(unsorted, lowerBound=pivot + 1, upperBound=upperBound)


    def mergesort(self,unsorted:List[int], lowerBound:int=None, upperBound:int=None):
        if lowerBound == None:
            lowerBound = 0
        if upperBound == None:
            upperBound = len(unsorted) - 1
        mid = (lowerBound + upperBound) // 2
        
        if lowerBound < upperBound:
            left = self.mergesort(unsorted=unsorted[lowerBound:mid])
            right = self.mergesort(unsorted=unsorted[mid+1:upperBound])
            return self.__merge(left=left, right=right)
        
        return unsorted

    def __merge(self,left:List[int],right:List[int]):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        while l < len(left):
            result.append(left[l])
            l += 1
        
        while r < len(right):
            result.append(right[r])
            r += 1
        
        return result

    # int[] bubblesort(int[] unsorted)
    def bubblesort(self, unsorted:List[int]) -> List[int]:
        for i in range(len(unsorted)): #n
            for j in range(i+1, len(unsorted)): #n
                if unsorted[i] > unsorted[j]:
                    temp = unsorted[i]
                    unsorted[i] = unsorted[j]
                    unsorted[j] = temp

        return unsorted
    
x = [-12,43,12,7,1,-1992,4241,1,2,423,432,1,232,2]
s = Sorts()
y = Sorts()
s.quicksort(x)
print("SORTED LIST, ",x)