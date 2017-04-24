import time
from itertools import combinations
from performance_info import *

## Time genratiom in timstamp format##
initialTime = time.mktime(time.gmtime()) + 360000
tstamp = [initialTime + t for t in range(0, 400000, 1)]

###Random String generation###
#name = [''.join(x) for x in combinations('qwertyuiopasdfghjklzxcvbnm1234567890', 10)]
name=[''.join(x) for x in combinations('Manoj Kumar12313242342352345345345345',5)]


##Random Serial ID genration ##
SerialID = [''.join(x) for x in combinations('12345678901234667677856775676572345', 7)]
output = set(SerialID)
SerialID = list(output)

## Epoch genration in int ##
timeflag = [int(initialTime) + t * 60 for t in range(0, 400000, 1)]

print(len(tstamp), len(name), len(SerialID), len(output), len(timeflag))

while True:

    a = InsertPerformanceInfo(tflag=timeflag,count=400000)
    a.start()

    b = DeletePerformanceInfo(tflag=timeflag,count=400000)
    b.start()

    c=ReindexPerformanceInfo(count=400000)
    c.start()

    d = VaccumPerformanceInfo(count=400000)
    d.start()