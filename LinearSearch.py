"""
Input: A sequence of n numbers A =a1, a2, . . . . aNi 
and a value v.
Output: An index i such that v = A[i] or the special 
value NIL if v does not appear in A.
Write pseudocode for linear search, which scans through
the sequence, looking for v. Using a loop invariant, 
prove that your algorithm is correct. Make sure that
your loop invariant fulfills the three necessary 
properties.
"""

# python code for linear search 
#I Guess with complexity O(n)
# Asthe loop runs n times that is the no of elements in the input array

#add funtionality multiple elements found:resolved
# "NIL" feature still dont Work:resolved
def LSearch (inputa, element):
    i= 0
    for i in range (0, inputa.__len__()):
        if (inputa[i] == element):
           return i

inputa = list(map(int, input("Enter the input array : ").split()))
a= True
while(a):
    
    element = int(input("Enter the element to search for linearly : "))
    
    check=LSearch(inputa, element)
    if (check==None):
        print("NIL")
    else:
         print("Index of the element in the array", LSearch(inputa, element))
    flag = int(input("Enter one to continue zero to exit:"))
    if (flag == 1):
        a=True
    else :
        a=False
   
    

