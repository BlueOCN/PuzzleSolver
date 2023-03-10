class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class NodeCounter(metaclass=SingletonMeta):
    def __init__(self):
        self.counter = 0

    def getNextNodeName(self):
        string = "E" + str(self.counter)
        self.incrementCounter()
        return string

    def getCounter(self):
        return self.counter

    def incrementCounter(self):
        self.counter += 1

    def decrementCounter(self):
        self.counter -= 1

    def resetCounter(self):
        self.counter = 0


def test():
    nodeCounter1 = NodeCounter()
    nodeCounter1.incrementCounter()
    nodeCounter1.incrementCounter()
    nodeCounter1.incrementCounter()
    nodeCounter2 = NodeCounter()
    nodeCounter2.incrementCounter()
    nodeCounter3 = NodeCounter()
    nodeCounter3.incrementCounter()
    nodeCounter3.incrementCounter()
    print(nodeCounter1.getCounter())
    print(nodeCounter2.getCounter())

if __name__ == "__main__":
    test()