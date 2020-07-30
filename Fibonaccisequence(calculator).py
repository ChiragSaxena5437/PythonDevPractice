import timeit
from time import time
start_time = time()
start = timeit.default_timer()
n=int(input("Enter the no. till fibonacci sequence is required :" ))
print("0 1 1",end=" ")
a=1
for i in range(4,n+1):
    a=round(a*1.61)
    print(a,end=" ")
stop = timeit.default_timer()
execution_time = stop - start
end_time = time()
time_taken = end_time - start_time
print(time_taken)
print("Program Executed in "+str(execution_time)) 
##3.0185336"""
"""

import timeit
from time import time
start_time = time()
start = timeit.default_timer()
n=int(input("Enter the no. till fibonacci sequence is required :"))
a=0
print(a,end=" ")
b=1
print(b,end=" ")
for i in range(3,n+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
stop = timeit.default_timer()
execution_time = stop - start
end_time = time()
time_taken = end_time - start_time
print(time_taken)
print("Program Executed in "+str(execution_time)) 
##time mentioned fo rcalculating 100 numbers of the fibonacci sequence == 2.5332461"""
