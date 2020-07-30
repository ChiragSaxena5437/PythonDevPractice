"""
Given an integer X and integers A0, A1,.... AN-1 which are presorted and already in memory.
find i such that Ai = X return i=-1 if X is not in the input.

Clearly, all the work done inside the loop takes O(1) per iteration, so the analysis
requires determining the number of times around the loop. The loop starts with high -
low = N − 1 and finishes with high - low ≥ −1. Every time through the loop the value
high - low must be at least halved from its previous value; thus, the number of times
around the loop is at most [log(N − 1)] + 2.

"""
def BinarySearch( InputArray, element):
    low = 0
    high = InputArray.__len__() 

    while (low <= high):
        mid=int((low+high)/2)
        if(InputArray[mid]<element):
            low=mid+1
        elif(InputArray[mid]>element):
            high=mid-1
        else:
            return mid
    
    return -1

UnsortedInput = list(map(int, input().split()))
element = int(input("Enter the element to be searched"))
InputArray=sorted(UnsortedInput)
print("Sorted array", InputArray)
result = BinarySearch(InputArray, element)

if (result==-1):
    print("not Found")
else:
    print(result)