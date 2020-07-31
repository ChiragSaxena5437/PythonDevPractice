

"""Sorting n numbers stored in array A by first finding the smallest element
of A and exchanging it with the element in A[1]. Then find the second smallest
element of A, and exchange it with A[2]. Continue in this manner for the first n1
elements of A. Write pseudocode for this algorithm, which is known as selection
sort
inputarr=list(map(int, input().split()))

sortedarr = []
i=0
def fmin(inputarr):
    return min(inputarr)

for i in range (0, inputarr.__len__()):
   sortedarr.append(fmin(inputarr))
   inputarr.remove(fmin(inputarr))
print(sortedarr)"""

def fmin(inputarr, j):
    k=0
    temp=0
    for k in range (0, inputarr.__len__()):
        
        temp=inputarr[k]
        
        if (inputarr[k]<temp):
            temp=inputarr[k]
            inputarr[k]=temp
       
    return temp
##debug 
##problem all the values are being substituted by  randomunclassified unchecked number


inputarr=list(map(int, input().split()))
i = 0
for i in range (0, inputarr.__len__()):
    j=i
    inputarr[i] = fmin(inputarr,j)
    i=i+1
    
print(inputarr)


