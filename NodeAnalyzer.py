import Node
import utils
from NodeMoves import NodeMoves
from AlgorithmKey import AlgorithmKey

class NodeAnalyzer:

    def __init__(self, node, goalState:list, parentMoveToThisNode=None) -> None:
        if not isinstance(node, Node.Node):
            raise TypeError("node must be a Node instance")
        if node is None:
            raise ValueError("node can't be None")
        if not isinstance(parentMoveToThisNode, NodeMoves) and parentMoveToThisNode is not None:
            raise TypeError("parentMoveToThisNode must be of NodeMoves type")

        self._node: Node.Node = node
        self._goalState: list = goalState[:]
        self._parentMoveToThisNode: NodeMoves = parentMoveToThisNode

        self._possibleMovements: list = []
        self.analyzePossibleMovements()


    def analyzePossibleMovements(self) -> list:
        if self.isMoveLeftPossible(self._node.getActualState()):
            self._possibleMovements.append(NodeMoves.LEFT)
        if self.isMoveRightPossible(self._node.getActualState()):
            self._possibleMovements.append(NodeMoves.RIGHT)
        if self.isMoveUpPossible(self._node.getActualState()):
            self._possibleMovements.append(NodeMoves.UP)
        if self.isMoveDownPossible(self._node.getActualState()):
            self._possibleMovements.append(NodeMoves.DOWN)

    def isMoveLeftPossible(self, state):
        if self._parentMoveToThisNode == NodeMoves.RIGHT:
            return False
        newState = utils.moveLeft(state)
        if newState == state:
            return False
        return True

    def isMoveRightPossible(self, state):
        if self._parentMoveToThisNode == NodeMoves.LEFT:
            return False
        newState = utils.moveRight(state)
        if newState == state:
            return False
        return True

    def isMoveUpPossible(self, state):
        if self._parentMoveToThisNode == NodeMoves.DOWN:
            return False
        newState = utils.moveUp(state)
        if newState == state:
            return False
        return True

    def isMoveDownPossible(self, state):
        if self._parentMoveToThisNode == NodeMoves.UP:
            return False
        newState = utils.moveDown(state)
        if newState == state:
            return False
        return True

    def addChilds(self) -> bool:
        for movement in self._possibleMovements:
            childNode = None
            if movement == NodeMoves.LEFT:
                childNode = Node.Node(utils.moveLeft(self._node.getActualState()), self._goalState, self._node._algorithmKey, self._node, NodeMoves.LEFT)
            elif movement == NodeMoves.RIGHT:
                childNode = Node.Node(utils.moveRight(self._node.getActualState()), self._goalState, self._node._algorithmKey, self._node, NodeMoves.RIGHT)
            elif movement == NodeMoves.UP:
                childNode = Node.Node(utils.moveUp(self._node.getActualState()), self._goalState, self._node._algorithmKey, self._node, NodeMoves.UP)
            elif movement == NodeMoves.DOWN:
                childNode = Node.Node(utils.moveDown(self._node.getActualState()), self._goalState, self._node._algorithmKey, self._node, NodeMoves.DOWN)
            self._node.addChild(childNode)

        if len(self._node.getChilds()) == 0:
            return False
        return True
    
    def getHeuristicValue(self) -> int:
        if self._node._algorithmKey == AlgorithmKey.MAX:
            return utils.getHeuristicValue(self._node.getActualState(), self._goalState)
        return utils.computeH(self._node.getActualState(), self._goalState)

    def getPossibleMovements(self):
        return self._possibleMovements[:]

    def __str__(self) -> str:
        return "\n  [\n    NodeAnalyzer Class\n    PossibleMovements: " + str(self._possibleMovements)+"\n  ]"
