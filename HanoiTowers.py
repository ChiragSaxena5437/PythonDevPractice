"""
Puzzle
There are three sticks with n discs sorted by size on
one of the sticks. The goal is to move all n discs to
another stick subject to two constraints: move one disc
at a time and don’t place a larger disc on a smaller one.

Solution 
(research)we can use inducion and thus recursion 
also we can use direct formula for calculating the moves required by the hanaoi towers
"""

##using direct formula

def Nummoves(numdiscs):
    return (2**numdiscs)-1

print("This system takes no. hanoi towers as three") 
numdiscs =int(input("Enter the number of discs in hanoi tower to be transported into another tower :"))
print("No. of minimum moves required : ", Nummoves(numdiscs))