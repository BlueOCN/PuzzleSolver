from AlgorithmKey import AlgorithmKey
from NodeCounter import NodeCounter
import NodeAnalyzer
import utils
import NodeMoves
import NodeUtils

class Node:

    algorithmMin = lambda x, y: True if x <= y else False
    algorithmMax = lambda x, y: True if x >= y else False

    def __init__(self, actualState:list, goalState:list, algorithmKey:AlgorithmKey, _parent = None, moveToThisNode:NodeMoves = None):
        self._index:int = NodeCounter().getCounter()
        self._name:str = NodeCounter().getNextNodeName()
        self._actualState:list = actualState[:]
        self._goalState:list = goalState[:]
        self._algorithmKey:AlgorithmKey = algorithmKey
        self._moveToThisNode:NodeMoves.NodeMoves = moveToThisNode
        self._childs:Node = None

        self._parent:Node = _parent
        if self._parent is not None:
            if not isinstance(self._parent, Node):
                raise TypeError("parent must be a Node instance")
            if moveToThisNode is None:
                raise ValueError("moveToThisNode can't be None")
        self._nodeAnalyzer = NodeAnalyzer.NodeAnalyzer(self, goalState, moveToThisNode)

        if self._parent is not None:
            if algorithmKey == AlgorithmKey.MIN:
                self._gN = self._parent._gN + 1
            elif algorithmKey == AlgorithmKey.MAX:
                self._gN = self._parent._gN - 1
        else:
            self._gN = 0
        
        self._hN = self._nodeAnalyzer.getHeuristicValue()
        self._fN = self._gN + self._hN

        
        if self.isCurrentStateGoal(): 
            NodeUtils.printActionTrace(self)
            NodeUtils.printNodeTrace(self)
            print("\n------- Goal State Reached -------\n")
            NodeUtils.printMappedActionTrace(self)
            quit()
            # raise ValueError("Goal State Reached")

        NodeUtils.NodeUtils().addNode(self)
        NodeUtils.NodeUtils().sortList()
        
        
    def whoRuns(self):
        nodeReachingBefore = self.isReachedByShorterPath()
        if nodeReachingBefore is not None:
            nodeReachingBefore.run()
        else:
            self.run()
        


    def isReachedByShorterPath(self) -> bool:
        return NodeUtils.NodeUtils().nodeExists(self)

    def run(self):
        self._nodeAnalyzer.addChilds()
        for child in self._childs:
            if self._algorithmKey == AlgorithmKey.MIN:
                if Node.algorithmMin(child._fN, self._fN):
                    child.whoRuns()
            elif self._algorithmKey == AlgorithmKey.MAX:
                if Node.algorithmMax(child._fN, self._fN):
                    child.whoRuns()
        NodeUtils.NodeUtils().removeNode(self)
        NodeUtils.NodeUtils().sortList()
        openNodeList = NodeUtils.NodeUtils().getOpenList()
        if self._parent is None:
            while len(openNodeList) > 0:
                openNodeList.pop().run()
                openNodeList = NodeUtils.NodeUtils().getOpenList()
        #print("Node: " + self._name + " finished")

        

                
    
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
        parentStringRepresentation = self._parent.getSimpleStrRepresentation()
        parentStringRepresentation = parentStringRepresentation.split("\n")
        parentStringRepresentation = "\n\t".join(parentStringRepresentation)
        return parentStringRepresentation
    
    def getChildsStrRepresentation(self):
        if self._childs is None:
            return "None"
        childsStringRepresentation = ""
        for child in self._childs:
            childStringRepresentation = child.getSimpleStrRepresentation()
            childStringRepresentation = childStringRepresentation.split("\n")
            childStringRepresentation = "\n\t".join(childStringRepresentation)
            childsStringRepresentation += childStringRepresentation
        return childsStringRepresentation

    def isCurrentStateGoal(self):
        return self._actualState == self._goalState

    def getSimpleStrRepresentation(self):
        return "[\n  Node Class\n  Index: "+str(self._index)+"\n  Name: "+self._name+"\n  Actual State: "+utils.getPuzzleStringRepresentation(self._actualState)+"\n]"
    
    def getStrRepresentation(self):
        return "[\n  Node Class\n  Index: "+str(self._index)+"\n  Name: "+self._name+"\n  g(n): "+str(self._gN)+"\n  h(n): "+str(self._hN)+"\n  f(n): "+str(self._fN)+"\n  Actual State: "+utils.getPuzzleStringRepresentation(self._actualState)+"\n]"
    
    def __str__(self) -> str:
        return "[\n  Node Class\n  Index: "+str(self._index)+"\n  Name: "+self._name+"\n  g(n): "+str(self._gN)+"\n  h(n): "+str(self._hN)+"\n  f(n): "+str(self._fN)+"\n  Actual State: "+utils.getPuzzleStringRepresentation(self._actualState)+"\n  Parent: "+self.getRelativeStrRepresentation(parent=True)+"\n  Node Analyzer:"+str(self._nodeAnalyzer)+"\n  Childs: "+self.getRelativeStrRepresentation(childs=True)+"\n]"

def test():
    node = Node("A")
    print(node)
    node1 = Node("B")
    print(node1)
    node2 = Node("C", node)
    print(node2)
    node3 = Node("D", node)
    print(node3)
    print(node3.getParent())

if __name__ == "__main__":
    test()