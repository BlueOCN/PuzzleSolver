import Node
from AlgorithmKey import AlgorithmKey
import utils
import NodeUtils

def lol():
    # initialState = [1,2,4,7,11,6,12,3,5,10,14,8,0,9,13,15]
    # goalState = [1,2,4,7,11,6,12,3,5,10,14,0,9,13,15,8]
    initialState, goalState = utils.readFile("Datos.txt")
    utils.printPuzzle(initialState)
    utils.printPuzzle(goalState)
    node1 = Node.Node(initialState, goalState, AlgorithmKey.MIN)
    node1.run()
    #if node1._nodeAnalyzer.addChilds():
    #    for child in node1._childs:
    #        child._nodeAnalyzer.addChilds()

    #print(node1)

    #for child in node1._childs:
    #    print(child)

    # NodeUtils.printTree(node1)



    print(NodeUtils.NodeUtils().getDict())

    for _,v in NodeUtils.NodeUtils().getDict().items():
        print(v.getStrRepresentation())
    

if __name__ == "__main__":
    lol()
