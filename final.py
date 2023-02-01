import Node
from AlgorithmKey import AlgorithmKey
import utils
import NodeUtils
from time import time
import NodeCounter

def final():
    # Datos0.txt, ..., Datos4.txt comprende los 5 casos de prueba
    # Que se utilizaron para la generación de los datos de la tabla del reporte
    # Insertar dentro de utils.readFile el nombre del archivo a leer
    initialState, goalState = utils.readFile("Datos0.txt")
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
    finally:
        NodeUtils.printMappedActionTrace(node1)

if __name__ == "__main__":
    final()