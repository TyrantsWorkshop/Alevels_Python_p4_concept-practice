## implement a linked list using an array of nodes with data and pointer fields.
## write functions to display the list and search for a data item in the list.
## create a menu to display the list, find an item or exit.

class ListNode:
    def __init__(self,Udata,Upointer):
        self.data = Udata
        self.Pointer = Upointer

LinkedList = [ListNode(50,2),ListNode(20,3),ListNode(60,-1),ListNode(40,0),ListNode(10,1),ListNode(0,6),ListNode(0,7),ListNode(0,-1)]

def OutputList(LinkedList,CurrentPointer):
        while(CurrentPointer != -1):
            print(LinkedList[CurrentPointer].data)
            CurrentPointer = LinkedList[CurrentPointer].Pointer

def findItem(LinkedList,CurrentPointer):
    dataItem = int(input("enter your DATA TO BE SEARCHED"))
    while(CurrentPointer != -1):
        if LinkedList[CurrentPointer].data == dataItem:
            position = LinkedList[CurrentPointer].Pointer
            print(position)
        else:
            print("-1")
    
        
        
    
    


StartPointer = 4
FreeListPtr = 5
Choice = 0
while Choice != 3:
    if Choice == 1:
        OutputList(LinkedList,StartPointer)
    elif Choice == 2:
        findItem(LinkedList,StartPointer)
            
    print("1:display the list")
    print("2:find item")
    print("3:exit")
    Choice = int(input("enter your choice"))
    while Choice <1 or Choice>2:
        print("invalid choice")
        Choice = int(input("enter your choice"))
                    
