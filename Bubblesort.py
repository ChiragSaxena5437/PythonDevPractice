
inputarr =list(map(int, input().split()))

for i in range (len(inputarr)-1, 0, -1):
    for j in range (i):
        if (inputarr[j]>inputarr[j+1]):
            a=inputarr[j]
            inputarr[j]  = inputarr[j+1]
            inputarr[j+1]= a 

    
print(inputarr)   

"""
def bubblesort(list):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

inputarr =list(map(int, input().split()))
bubblesort(inputarr)
print(inputarr)"""