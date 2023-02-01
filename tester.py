import Node
from AlgorithmKey import AlgorithmKey
import utils
import NodeUtils
from time import time
import NodeCounter

def lol(num:int) -> float:
    # initialState = [1,2,4,7,11,6,12,3,5,10,14,8,0,9,13,15]
    # goalState = [1,2,4,7,11,6,12,3,5,10,14,0,9,13,15,8]
    initialState, goalState = utils.readFile("Datos"+str(num)+".txt")
    utils.printPuzzle(initialState)
    utils.printPuzzle(goalState)
    node1 = Node.Node(initialState, goalState, AlgorithmKey.MIN)
    startingTime = time()
    try:
        node1.run()
    except ValueError as e:
        execTime = time() - startingTime
        print(e)
        print("Time: " + str(execTime) + " seconds")
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


def test10Times():
    #### Soluciones encontradas / Soluciones no encontradas
    print("Test 10")
    initialState, goalState = utils.readFile("Datos.txt")
    times = list()
    for _ in range(0,10):
        utils.printPuzzle(utils.generate_random_state())
        utils.printPuzzle(goalState)
        node1 = Node.Node(initialState, goalState, AlgorithmKey.MIN)
        startingTime = time()
        try:
            node1.run()
        except ValueError as e:
            execTime = time() - startingTime
            print(e)
            print("Time: " + str(execTime) + " seconds")
            times.append(execTime)
        finally:
            NodeCounter.NodeCounter().resetCounter()
            NodeUtils.NodeUtils().reset()
    print("Average time: ", sum(times)/len(times))
    print("Max time: ", max(times))
    print("Min time: ", min(times))
    print("All times: ", times)
    print("End Test")

if __name__ == "__main__":
    lol(0)
    #test10Times()