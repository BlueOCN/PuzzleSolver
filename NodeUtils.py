def printActionTrace(node, path = []):
    if node._parent == None:
        return
    printActionTrace(node._parent, path.append(node._parentMoveToThisNode))
    print(path.reverse())