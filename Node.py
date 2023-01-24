from NodeCounter import NodeCounter

class Node:
    def __init__(self, actualState:list, _parent = None):
        self._index = NodeCounter().getCounter()
        self._name = NodeCounter().getNextNodeName()
        self._actualState = actualState[:]
        self._parent:Node = _parent
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

    def __str__(self) -> str:
        return "Node Class \nIndex: ".join(str(self._index)).join("\nName: ").join(self._name).join("\nActual State: ").join(str(self._actualState)).join("\nParent: ").join(str(self._parent)).join("\nChilds: ").join(str(self._childs))
    


def main():
    node = Node("A")
    print(node)
    node1 = Node("B")
    print(node1)
    node2 = Node("C")
    print(node2)
    node3 = Node("D", node)
    print(node3)
    print(node3.getParent())

if __name__ == "__main__":
    main()