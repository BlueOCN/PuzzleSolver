import Node

def lol():
    initialState = [1,2,4,7,11,6,12,3,5,10,14,8,9,0,13,15]
    goalState = [1,2,4,7,11,6,12,3,5,10,14,8,9,13,15,0]
    node1 = Node.Node(initialState, goalState)
    if node1._nodeAnalyzer.addChilds():
        for child in node1._childs:
            child._nodeAnalyzer.addChilds()

    print(node1)

    for child in node1._childs:
        print(child)

if __name__ == "__main__":
    lol()
