i = [1111, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
i.sort()
print(i)

words = ["what", "changes", "about", "our", "searching", "algorithm", "there"]

for i in  words:
    if len(i) == 3:
        print(i)

words.sort()
print(words)


# // Return position of largest value in integer array A
# static int largest(int[] A) { 
#   int currlarge = 0; // Position of largest element seen
#   for (int i=1; i<A.length; i++) { // For each element
#       if (A[currlarge] < A[i]) { // if A[i] is larger
#           currlarge = i; // remember its position
#       }
#   }
#   return currlarge; // Return largest position
# }


def largest(A:list(int)) -> int:  # 3n + 2
    currlarge = 0  # Assignment is 1
    for i in range(1, len(A)):   # 3n
        ''' 
         Each time we assign a value to i is 1 operation
         This happens len(A) times - 1
        '''
        if A[currlarge] < A[i]: # Comparison is 1 operations
            currlarge = i # Assignmenty is 1 operations
    
    return currlarge # 1


def largestOfSorted(A:list(int)) -> int:  # 2
    return len(A) - 1 # 1



def largestRecurse(A:list(int), index= None, largest = None) -> int:  # 3n + 2
    if largest and index:
        if A[largest] < A[index]:
            largest = index
            
        if index < len(A) - 1:
            return largestRecurse(A, index = index + 1, largest = largest)
        else:
            return largest 
    else:
        return largestRecurse(A, index = 1, largest = 0)



def largest(A:list(int)) -> int:  # 5n + 2
    currlarge = 0  # Assignment is 1
    currlarge1 = 0  # Assignment is 1
    currlarge2 = 0  # Assignment is 1
    n = A
    for i in range(1, len(A)):   # 5n
        ''' 
         Each time we assign a value to i is 1 operation
         This happens len(A) times - 1
        '''
        
        if A[currlarge] < A[i]: # Comparison is 1 operations
            currlarge2 = currlarge1
            currlarge1 = currlarge
            currlarge = i # Assignmenty is 1 operations
    
    return A[currlarge] # 1



# 5n + 2  compare  
# 
# 
#  T(N) 3n + 2
#  3n + 2 <= c * f(n)
#  f(n) = n
#  3n + 2 <= c * n
#  3n + 2 <= 3 * n NEVER TRUE
#  3n + 2 <= 4 * n for all n >














#  T(N) = 3n^2 + n + 2
#  3n^2  <= c * f(n) for n greater than some number

#  3n^2  + n + 2  <= 4 * n^2 for n greater than some number












def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)