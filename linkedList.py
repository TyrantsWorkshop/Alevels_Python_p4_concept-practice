## implement a linked list using an array of nodes with data and pointer fields.
## write functions to add a node in sorted order, delete a node and display the list.
## create a menu to add, delete, display or exit.

class ListNode:
    def __init__(self,Udata,Upointer):
        self.data = Udata
        self.Pointer = Upointer
def OutputList(LinkedList,CurrentPointer):
        while(CurrentPointer != -1):
            print(LinkedList[CurrentPointer].data)
            CurrentPointer = LinkedList[CurrentPointer].Pointer

def AddNode(LinkedList,CurrentPointer):
        global StartPointer
        global FreeListPtr
        item = int(input("enter data to be inserted"))
        if FreeListPtr != -1:
            NewNode = ListNode(item, -1)
            NewNodePtr = FreeListPtr
            FreeListPtr = LinkedList[FreeListPtr].Pointer
            LinkedList[NewNodePtr] = NewNode
            PreviousNodePtr = -1
            while (CurrentPointer != -1) and LinkedList[CurrentPointer].data < item:
                PreviousNodePtr = CurrentPointer
                CurrentPointer = LinkedList[CurrentPointer].pointer
            if PreviousNodePtr == -1:
                LinkedList[NewNodePtr].Pointer = CurrentPointer
                StartPointer = NewNodePtr
            else :
                LinkedList[NewNodePtr].Pointer = LinkedList[PreviousNodePtr].Pointer
                LinkedList[PreviousNodePtr].Pointer = NewNodePtr

def DeleteNode(LinkedList,CurrentPointer):
        global StartPointer
        global FreeListPtr
        DeleteItem = int(input("enter data to be deleted"))
        while (CurrentPointer != -1) and LinkedList[CurrentPointer].data != DeleteItem:
            PreviousNodePtr = CurrentPointer
            CurrentPointer = LinkedList[CurrentPointer].Pointer
        if CurrentPointer != -1:
            if CurrentPointer == StartPointer:
                StartPointer = LinkedList[StartPointer].Pointer
            else:
                LinkedList[PreviousNodePtr].Pointer = LinkedList[CurrentPointer].Pointer
            LinkedList[CurrentPointer].Pointer = FreeListPtr
            FreeListPtr = CurrentPointer

LinkedList = [ListNode(-1,1),ListNode(-1,2),ListNode(-1,3),ListNode(-1,4),ListNode(-1,-1)]

StartPointer = -1
FreeListPtr = 0
Choice = 0
while Choice != 4:
    if Choice == 1:
        AddNode(LinkedList,StartPointer)
    elif Choice == 2:
        DeleteNode(LinkedList,StartPointer)
    elif Choice == 3:
        OutputList(LinkedList,StartPointer)
    print("1:add an item")
    print("2:delete an item")
    print("3:display the list")
    print("4:exit")
    Choice = int(input("enter your choice"))
    while Choice <1 or Choice>4:
        print("invalid choice")
        Choice = int(input("enter your choice"))
                    
        
