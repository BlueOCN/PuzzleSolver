from NodeCounter import NodeCounter

class Node:
    def __init__(self, actualState:list, _parent = None):
        self._index = NodeCounter().getCounter()
        self._name = NodeCounter().getNextNodeName()
        self._actualState = actualState[:]
        
        self._parent:Node = _parent
        if self._parent is not None:
            self._parent.addChild(self)
        
        self._childs:Node = None
    
    def getIndex(self):
        return self._index

    def getName(self):
        return self._name

    def getActualState(self):
        return (self._actualState)[:]
    
    def getParent(self):
        return self._parent
    
    def getChilds(self):
        return self._childs

    def addChild(self, child):
        if self._childs is None:
            self._childs = []
        self._childs.append(child)

    def getRelativeStrRepresentation(self, parent:bool = False, childs:bool = False):
        if parent:
            return self.getParentStrRepresentation()
        if childs:
            return self.getChildsStrRepresentation()
        raise ValueError("parent and childs can't be both False on getRelativeStrRepresentation in Node Class")


    def getParentStrRepresentation(self):
        if self._parent is None:
            return "None"
        parentStringRepresentation = str(self._parent)
        parentStringRepresentation = parentStringRepresentation.split("\n")
        for i in range(len(parentStringRepresentation)):
            parentStringRepresentation[i] = "\t"+parentStringRepresentation[i]
        parentStringRepresentation = "\n".join(parentStringRepresentation)
        return parentStringRepresentation
    
    def getChildsStrRepresentation(self):
        if self._childs is None:
            return "None"
        childsStringRepresentation = ""
        for child in self._childs:
            childStringRepresentation = str(child)
            childStringRepresentation = childStringRepresentation.split("\n")
            for i in range(len(childStringRepresentation)):
                childStringRepresentation[i] = "\t"+childStringRepresentation[i]
            childStringRepresentation = "\n".join(childStringRepresentation)
            childsStringRepresentation += childStringRepresentation
        return childsStringRepresentation

    def __str__(self) -> str:
        return "[\n  Node Class\n  Index: "+str(self._index)+"\n  Name: "+self._name+"\n  Actual State: "+str(self._actualState)+"\n  Parent: "+self.getRelativeStrRepresentation(parent=True)+"\n  Childs: "+self.getRelativeStrRepresentation(childs=True)+"\n]"
    


def main():
    node = Node("A")
    print(node)
    node1 = Node("B")
    print(node1)
    node2 = Node("C")
    print(node2)
    # node3 = Node("D", node)
    # print(node3)
    # print(node3.getParent())

if __name__ == "__main__":
    main()