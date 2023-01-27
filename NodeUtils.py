

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class NodeUtils(metaclass=SingletonMeta):

    def __init__(self):
        self._dict = dict()
        self._list = list()
    
    def addNode(self, node):
        self._dict[node.getName()] = node
        self._list.append(node)

    def addNodes(self, nodes:list):
        for node in nodes:
            self.addNode(node)

    def removeNode(self, node):
        self._list = list(filter(lambda x: x._name != node._name, self._list))
    
    def nodeExists(self, node):
        comparingNode = self.getNode(node.getName())
        if comparingNode is not None:
            if comparingNode._actualState == node._actualState:
                return comparingNode
        return None

    def getNode(self, nodeName):
        try:
            return self._dict[nodeName]
        except KeyError:
            return None
    
    def getDict(self):
        return self._dict
    
    def getList(self):
        return self._list
    
    def sortList(self):
        self._list.sort(key=lambda node: node._fN)
        self._list.reverse()

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

def printTree(node, tree = "\n\n\n") -> str:
    if node._childs is None:
        return ""
    tree += "---> "+node.getName()+"\n"
    for child in node._childs:
        tree += " |\n |---> "+child.getName()+"\n"
        printTree(child, tree)
    print(tree)