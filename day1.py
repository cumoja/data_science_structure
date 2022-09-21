'''
1 1 2 3 5 8 13 21


if condition:
    pass


if condtion:
    pass
else:
    pass

if condition:
    pass
elif condition:
    pass
else:
    pass


LayMans
'''
def fibRecurse(n:int):
    if n <= 0: # f(0) = 0 
        return 0
    elif n == 1: # f(1) = 1 
        return 1   
    else: # f(n) = f(n-1) + f(n -2)
        return fibRecurse(n - 1) + fibRecurse(n -2)

'''
                                    fib( 5 )
                            /                       \
                        fib(4)                       fib( 3 )
                        /      \                    /       \
                     fib(3)      fib(2)          fib(2)     fib(1)   
                    /       \                   /      \
                 fib(2)     fib(1)          fib(1)    fib(0)    
                 /      \
             fib(1)    fib(0)
  
'''

def fibRecurseS(n:int):
    match(n):
        case 0:
            return 0
        case 1: # f(1) = 1 
            return 1   
        case _: # f(n) = f(n-1) + f(n -2)
            return fibRecurseS(n - 1) + fibRecurseS(n -2)
   
def fibIterative(n:int):
       a = 0
       b = 1
       c = 0
       
       while (n-1) > 0:
            c = a + b
            a = b 
            b = c
            n -= 1
       return c 




def fib(n:int, memo:dict):
    if n in memo: # f(0) = 0 
        return memo[n]
    elif n == 0: # f(1) = 1 
        memo[n] = 0
        return 0   
    elif n == 1: # f(1) = 1
        memo[n] = 1 
        return 1   
    else: # f(n) = f(n-1) + f(n -2)
        memo[n] = fib(n - 1, memo) + fib(n -2, memo)
        return memo[n]
    
# print(fibIterative(40))
# print(fib(40, {}))


'''
if n is divisble by 3 PRINT FIZZ
if n is divisble by 5 PRINT BUZZ
if n is divisble by 3 and 5 PRINT FIZZBUZZ

1
2
FIZZ
4
BUZZ
FIZZ
7
8
FIZZ
BUZZ
11
FIZZ
13
14
FIZZBUZZ
16
17
FIZZ
19
BUZZ
'''
# range(5) --> [0,1,2,3,4]

def fizzbuzz(n:int):
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FIZZBUZZ")
        elif i % 5 == 0:
            print("BUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        else:
            print(i)

def fizzbuzz(n:int):
    i = 1
    while( i <= n):
        if i % 15 == 0:
            print("FIZZBUZZ")
        elif i % 5 == 0:
            print("BUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        else:
            print(i)
        i += 1


fizzbuzz(100)


'''



'''



class Rule:
    def __init__(self):
        self.priority = None        
        
    def validate(self, input:str) -> bool:
        return False

class SaidAlexa(Rule):
    def __init__(self):
        self.priority = 0   

    def validate(self, input:str) -> bool:
        return input[0:7].lower() == "alexa "

class BadWords(Rule):
    def __init__(self):
        self.priority = 200     
    
    def validate(self, input:str) -> bool:
        return self.containsProfanity()

    def containsProfanity(self):
        return False;


rules = [SaidAlexa()]

for i in rules:
    if i.validate:
        pass
    else:
        print("This doesn't succeed")


print(rules[0])


class GeoLocation:
    def __init__(self, longitude:float, latitude:float):
        self.longitude = longitude
        self.latitude = latitude


g = GeoLocation()