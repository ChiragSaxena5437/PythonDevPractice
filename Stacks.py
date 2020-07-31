"""
LIFO
Imagine stacking utencils or books               
"""
def Push(inputarray, element):
    inputarray.append(element)

def Pop(inputarray):
    lastin = inputarray[inputarray.__len__()-1]
    inputarray.remove(lastin)
    return lastin
##While functionality still dont work 
##Maybe Visual Studio Code??
flag = True
while(flag):
    inputarray = list(map(int, input("Enter the array to implement stack on : " ).split()))
    func       = list(map(str, input("Enter the function to be implemented : "  ).split()))
    if (func[0]=="push"):
        element =int(func[1])
        Push(inputarray, element)
    elif(func[0] == "pop"):
        PoppedE= Pop(inputarray)
        print("Poped Element", PoppedE)
    a=input("Enter 1 to continue")
    if (a==1):
        flag = True
        continue
    else:
        flag=False
        break
    
print(inputarray)