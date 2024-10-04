# write a function that takes one input parameter (0) and evaluates an expression a=n*10 for all values between 0 to n

import time
n = 10000000
def testfn(n):
    for i in range (0,n):
        a = i*10
# estimate execution time of this function for n

startTime = time.time()
print(startTime)
testfn(n)
endTime = time.time()
print(endTime)
print(f"for n = {n} execution time is {endTime-startTime} seconds")