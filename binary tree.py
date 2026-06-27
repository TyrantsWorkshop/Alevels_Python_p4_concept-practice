## implement a binary tree using an array of tree nodes with left pointer, data and right pointer fields.
## write functions to insert a node and traverse the tree using in-order traversal.
## create a menu to add an item, traverse in-order or exit.

class TreeNode:
    def __init__(self,LPointer,UData,RPointer):
        self.Data=UData
        self.LeftPointer=LPointer
        self.RightPointer=RPointer

def InOrder(Tree,RootNode):
    if Tree[RootNode].LeftPointer != -1:
        InOrder(Tree,Tree[RootNode].LeftPointer)
    print(str(Tree[RootNode].Data))
    if Tree[RootNode].RightPointer != -1:
        InOrder(Tree,Tree[RootNode].RightPointer)
        #print(str(Tree[RootNode].Data))

def InsertNode(Tree):
    global RootPointer
    global FreePtr
    Item = int(input("enter data to be inserted"))
    if FreePtr != -1:
        NewNode = TreeNode(-1,Item,-1)
        NewNodePtr = FreePtr
        FreePtr = Tree[FreePtr].LeftPointer
        Tree[NewNodePtr] = NewNode
        if RootPointer == -1:
            RootPointer = NewNodePtr
        else:
            CurrentPointer = RootPointer
            #PreviousNodePtr = -1
            while(CurrentPointer != -1):
                PreviousNodePtr = CurrentPointer
                if Tree[CurrentPointer].data> Item:
                    TurnedLeft = True
                    CurrentPointer = Tree[CurrentPointer].LeftPointer
                else:
                    TurnedLeft = False
                    CurrentPointer = Tree[CurrentPointer].RightPointer
            if TurnedLeft ==True:
                Tree[PreviousNodePtr].LeftPointer = NewNodePtr
            else:
                Tree[PreviousNodePtr].RightPointer = NewNodePtr

Tree = [TreeNode(1,0,-1),TreeNode(2,0,-1),TreeNode(3,0,-1),TreeNode(4,0,-1)]
RootPointer = -1
FreePtr = 0
Choice = 0
while Choice != 3:
    if Choice == 1:
        InsertNode(Tree)
    elif Choice ==2:
        InOrder(Tree,RootPointer)
    print("1:add an item")
    print("2:traverse the tree inorder")
    print("3:exit")
    Choice = int(input("enter a choice"))
    while Choice<1 or Choice>3 :
        print("invalid choice")
        Choice = int(input("enter your choice"))

                
                
