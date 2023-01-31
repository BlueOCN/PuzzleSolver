import Node
from AlgorithmKey import AlgorithmKey
import utils
import NodeUtils
from time import time

def lol():
    # initialState = [1,2,4,7,11,6,12,3,5,10,14,8,0,9,13,15]
    # goalState = [1,2,4,7,11,6,12,3,5,10,14,0,9,13,15,8]
    initialState, goalState = utils.readFile("Datos.txt")
    utils.printPuzzle(initialState)
    utils.printPuzzle(goalState)
    node1 = Node.Node(initialState, goalState, AlgorithmKey.MIN)
    startingTime = time()
    try:
        node1.run()
    except ValueError as e:
        print(e)
        print("Time: " + str(time() - startingTime) + " seconds")
    #if node1._nodeAnalyzer.addChilds():
    #    for child in node1._childs:
    #        child._nodeAnalyzer.addChilds()

    #print(node1)

    #for child in node1._childs:
    #    print(child)

    # NodeUtils.printTree(node1)



    # print(NodeUtils.NodeUtils().getDict())

    print("Dict size: ", len(NodeUtils.NodeUtils().getDict()))

    # for _,v in NodeUtils.NodeUtils().getDict().items():
    #     print(v.getStrRepresentation())

    #### Soluciones encontradas / Soluciones no encontradas
    print("Test 10")
    initialState, goalState = utils.readFile("Datos.txt")
    times = list()
    for solution in range(0,10):
        utils.printPuzzle(utils.generate_random_state())
        utils.printPuzzle(goalState)
        node1 = Node.Node(initialState, goalState, AlgorithmKey.MIN)
        startingTime = time()
        try:
            node1.run()
        except ValueError as e:
            print(e)
            print("Time: " + str(time() - startingTime) + " seconds")
            times.append(time() - startingTime)
    print("End Test")
            

if __name__ == "__main__":
    lol()
