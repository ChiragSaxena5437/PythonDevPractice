

## Stack Implementation  using python and functions
from time import time
"""start_time = time()

def Push(S,x):
    S.append(x)
def Pop(S,x,n):
    S.pop(n-1)
    
S=[]
n=int(input("Enter the value of the length of stack = "))
for i in range(0,n):
    x=input("Enter the value to be  pushed in stack = ")
    Push(S, x)

print(S)

q=int(input("Enter the value of indixes to pop the stack upto"))
for i in range(0,q):
    
    Pop(S, x, n)
    n=n-1
print(S)
end_time = time()
time_taken = end_time - start_time
print(time_taken)"""


def StackEmpty(S,top):
    if top==0:
        return True
    else:
        return  False
def Push(S,x,top):
    top = top+1
    S[top] = x
def Pop(S,top):
    if StackEmpty(S, top):
        print("Error underflow")
    else:
        top = top-1
        return S[top+1]
S=[]
top=0
n=int(input("Enter the Size of the stack"))
for i in range(0,n):
    x=input("Enter the value to be  pushed in stack = ")
    Push(S, x, top)
Pop(S, top)
print(S)


