#wap to estimate runtime of all the functions you have used so far 

import time as t
from file_downloder import download_file
url=r"https://github.com/upessocs/B1B2/blob/main/fileOrganizerGui/Organizer.zip"
file_name='organizer.zip'
startTime = float(t.time ())
print(startTime)
download_file(url,file_name)
endTime = float(t.time ())
print(endTime)
runTimeInSeconds = endTime - startTime
print(f"\n the time taken to execute the function is {runTimeInSeconds*100000} mirroSeconds") 


# till now we have done this work manual
# now we will do it automatically

def timeFunction(url,file_name):
    startTime = t.time()
    res = (1,2)

