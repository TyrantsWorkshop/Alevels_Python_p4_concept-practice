## write a program to implement a linked list using an array of node objects with data and nextNode fields.
## write a function to traverse and output all node data values starting from startPointer until -1 is reached.

class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


def outputNodes(LinkedList, startPointer):
    while startPointer != -1:
        print(LinkedList[startPointer].data)
        startPointer = LinkedList[startPointer].nextNode


LinkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), node(0, 6), node(0, 8), node(56, 3),
              node(0, 9), node(0, -1)]
startPointer = 0
emptyList = 5
print(outputNodes(LinkedList, startPointer))

