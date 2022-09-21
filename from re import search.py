from re import search


int_list = [1,2,3,4,5,6,7,8,9,0,234,2432,43]

def somefunction(int_list:list(int)):
    for i in int_list:
        print(x)

class Search:
    def binarySearch(self, value, search_space, min, mid, max) -> int:
        if value == search_space[mid]:
            return mid
        elif max <= min:
            return -1
        elif value < search_space[mid]:
            return self.binarySearch(value, search_space, min, max=int((min + mid) / 2), max=(mid-1))
        elif value > search_space[mid]:
            return self.binarySearch(value, search_space, min = (mid + 1), mid = int((mid + max) / 2), max=max)
        else:
            return -1
        


int_list = [1,2,3,4,5,6,7,8,9,0,234,2432,43]

search_space = int_list
value = 3
min = 0
max = len(int_list)
mid = int((min + max)/2)
found = False

while min < max and not found:
    if value == search_space[mid]:
        found = True
        break
    elif value < search_space[mid]:
        max = mid - 1 
        mid = int((min + max)/2)
    elif value < search_space[mid]:
        min = mid + 1
        mid = int((min + max)/2)



# for i in int_list:
#     if i == value:
#         return True

# for (int i = 0; i < 10; i++);

