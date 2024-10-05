# write a function that takes one input parameter (0) and evaluates an expression a=n*10 for all values between 0 to n

import time
ns = [1234243,12342345,46785687,3456567]
#n = 10000000

def testfn(n):
    for i in range (0,n):
        a = i*10
# estimate execution time of this function for n

def wrapper(func):
    def wrapped( *args, **kwargs):
        
        startTime = time.time()
        func(*args, **kwargs)

        endTime = time.time()
        print(f"for n = {n} execution time is {endTime-startTime} seconds")
    return wrapped

@wrapped  #decorater
def testfn(n):
    for i in range(0,n):
        a = i*10

def random(n):
    n**n
random(n)

n = 100000

wrapped_fn = wrapper(testfn, n)
wrapped_fn(n)

#useful while using fast API for webserver scraping