import threading
import sys
import random


def Histogram(threadName,list, array):
    for a in array:
        list[a] = list[a] + 1
        print("Thread "+ threadName+" : ", list[a])

values_range = 10
samples = 100

list = []
for i in range(values_range):
    list.append(0)

array = []
for i in range(samples):
    array.append(random.randint(0,values_range-1))

t1 = threading.Thread(target=Histogram, args=('th1',list, array[0:int(samples/2)]))
t2 = threading.Thread(target=Histogram, args=('th2',list, array[int(samples/2):samples]))

t1.start()
t2.start()

t1.join()
t2.join()


sys.stdout.write("\nObserved histogram\n")

for i in range(values_range):
    sys.stdout.write( "%d =\t %d\n\r" % (i, list[i]))