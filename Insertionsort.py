"""
1 for j = 2 to A.length
2   key = A[j]
3   // Insert A[j] into the sorted sequence A[1],, j.
4   i = j - 1
5   while i > 0 and A[i] > key
6       A[i+1] = A[i]
7       i = i - 1
8 A[i + 1]= key

imagine a card deck

"""

inputkeys= list(map(int,input().split()))
j=1
key = 0

for j in range (0, inputkeys.__len__()):
    key = inputkeys[j]
    ##sortedarr.append(inputkeys[j])
    i=j-1
    
    while (i > 0 and inputkeys[i]>key):
        inputkeys[i+1] = inputkeys[i]
        i=i-1
    inputkeys[i+1] = key
print(inputkeys)