def printActionTrace(node, path = list()) -> list:
    if node._parent is None:
        return path
    path.append(node._moveToThisNode)
    path = printActionTrace(node._parent, path)
    if path is not None:
        path.reverse()
        print("Solution Path: "+str(path))

def printNodeTrace(node, path = list()) -> list:
    if node._parent is None:
        path.append(node._name)
        return path
    path.append(node._name)
    path = printNodeTrace(node._parent, path)
    if path is not None:
        path.reverse()
        print("Solution Path: "+str(path))