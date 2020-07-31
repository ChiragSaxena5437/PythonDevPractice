"""A linked list is a sequence of data elements, which
are connected together via links. Each data element 
contains a connection to another data element in form
 of a pointer. 
 Python does not have linked lists in its standard 
 library. """

class Node:
     def __init__(self, dataval=None):
         self.dataval = dataval
         self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
#Link First Node to Second Node
e2.nextval=e3