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


def main():
    nodeCounter = NodeCounter()
    nodeCounter.incrementCounter()
    nodeCounter.incrementCounter()
    nodeCounter.incrementCounter()
    print(nodeCounter.getCounter())
    nodeCounter1 = NodeCounter()
    print(nodeCounter1.getCounter())

if __name__ == "__main__":
    main()