import random

PUZZLE_SIZE = 4
debbug = 0


def readFile(path: str) -> tuple[list, list]:
    '''Lee un archivo txt y extrae el estado inicial y el estado objetivo'''
    initial_state = list()
    goal_state = list()

    fh = open(path, "r")

    for index, file in enumerate(fh):
        for number in file.strip().split(','):
            if (index < PUZZLE_SIZE):
                initial_state.append(int(number))
            else:
                goal_state.append(int(number))
    if debbug:
        print("Initial State and Goal State")
        print(initial_state, len(initial_state))
        print(goal_state, len(goal_state))
        print()

    # fh.close()

    return initial_state, goal_state


def getCoordinate(index: int) -> tuple[int, int]:
    '''Regresa la posición de un número en la matriz del puzzle. (fila, columna)'''
    return index//PUZZLE_SIZE, index % PUZZLE_SIZE


def getIndex(coordinate: tuple) -> int:
    '''Regresa el indice de una lista que corresponde a la coordenada en la matriz del puzzle. (0-16)'''
    if coordinate[0]*PUZZLE_SIZE+coordinate[1] < PUZZLE_SIZE**2 and coordinate[0]*PUZZLE_SIZE+coordinate[1] >= 0:
        return coordinate[0]*PUZZLE_SIZE+coordinate[1]
    print("Coordinate {p} does not exist.".format(p=coordinate))

    if coordinate[0]*PUZZLE_SIZE+coordinate[1] < 0:
        return 0
    return -1

def getNextMoves(coordinate: tuple)->list:
    next_moves = list()
    print(coordinate[0],coordinate[1])
    print(coordinate[0]-1,coordinate[1])
    print(coordinate[0]+1,coordinate[1])
    print(coordinate[0],coordinate[1]-1)
    # Si la coordenada está en el primer renglón no se puede mover hacia arriba
    # Si la coordenada está en el último renglón no se puede mover hacia abajo
    # Si la coordenada está en la primer columna no se puede mover hacia la izquierda
    # Si la coordenada está en la última columna no se puede mover hacia la derecha
    pass

def moveLeft(state: list) -> list:
    '''Encuentra el índice del número 0.
    Encuentra el índice del número a la izquierda del cero.
    Si el índice de la columna es igual a 0 entonces no se puede mover.
    Almacena el número en el indice correspondiente al cero.
    Almacena un cero en el índice correspondiente al número a la izquierda del cero.
    Regresa una lista con el número 0 desplazado una casilla hacia la izquierda.
    '''
    number_index = int()
    # Encontrar el índice del número cero
    space_index = state.index(0)
    # Encontrar el índice del número a la izquierda del cero
    # Si el índice de la clumna es igual a 0 entonces no se puede mover
    if getCoordinate(space_index)[1] > 0:
        number_index = getIndex(getCoordinate(space_index-1))
        # Almacenar el número en el indice correspondiente al cero
        next_state = state[:]
        next_state[space_index] = next_state[number_index]
        # Almacenar un cero en el índice correspondiente al número a la izquierda del cero
        next_state[number_index] = 0
        if debbug:
            print("Left shifted space")
            print(getCoordinate(space_index), "->",
                  getCoordinate(number_index))
            print(state, len(state), "O")
            print(next_state, len(next_state), "L")
            print()
        return next_state
    if debbug:
        print("Left shifted space")
        print(getCoordinate(space_index), "->", getCoordinate(space_index))
        print(state, len(state), "O")
        print(state, len(state), "L")
        print()
    return state


def moveRight(state: list) -> list:
    '''
    Regresa una lista con el número 0 desplazado una casilla hacia la derecha.
    Encuentra el índice del número 0.
    Encuentra el índice del número a la derecha del cero.
    Si el índice de la columna es igual a 3 entonces no se puede mover.
    Almacena el número en el indice correspondiente al cero.
    Almacena un cero en el índice correspondiente al número a la derecha del cero.
    '''
    number_index = int()
    # Encontrar el índice del número cero
    space_index = state.index(0)
    # Encontrar el índice del número a la izquierda del cero
    # Si el índice de la clumna es igual a 0 entonces no se puede mover
    if getCoordinate(space_index)[1] < PUZZLE_SIZE-1:
        number_index = getIndex(getCoordinate(space_index+1))
        # Almacenar el número en el indice correspondiente al cero
        next_state = state[:]
        next_state[space_index] = next_state[number_index]
        # Almacenar un cero en el índice correspondiente al número a la izquierda del cero
        next_state[number_index] = 0
        if debbug:
            print("Right shifted space")
            print(getCoordinate(space_index), "->",
                  getCoordinate(number_index))
            print(state, len(state), "O")
            print(next_state, len(next_state), "L")
            print()
        return next_state
    if debbug:
        print("Right shifted space")
        print(getCoordinate(space_index), "->", getCoordinate(space_index))
        print(state, len(state), "O")
        print(state, len(state), "L")
        print()
    return state


def moveUp(state: list) -> list:
    '''
    Regresa una lista con el número 0 desplazado una casilla hacia arriba.
    Encuentra el índice del número 0.
    Encuentra el índice del número a arriba del cero.
    Si el índice del renglón es igual a 0 entonces no se puede mover.
    Almacena el número en el indice correspondiente al cero.
    Almacena un cero en el índice correspondiente al número arriba del cero.
    '''
    number_index = int()
    # Encontrar el índice del número cero
    space_index = state.index(0)
    # Encontrar el índice del número arriba del cero
    # Si el índice del renglón es igual a 0 entonces no se puede mover
    if getCoordinate(space_index)[0] > 0:
        number_index = getIndex(getCoordinate(space_index-4))
        # Almacenar el número en el indice correspondiente al cero
        next_state = state[:]
        next_state[space_index] = next_state[number_index]
        # Almacenar un cero en el índice correspondiente al número a la izquierda del cero
        next_state[number_index] = 0
        if debbug:
            print("Up shifted space")
            print(getCoordinate(space_index), "->",
                  getCoordinate(number_index))
            print(state, len(state), "O")
            print(next_state, len(next_state), "L")
            print()
        return next_state
    if debbug:
        print("Up shifted space")
        print(getCoordinate(space_index), "->", getCoordinate(space_index))
        print(state, len(state), "O")
        print(state, len(state), "L")
        print()
    return state


def moveDown(state: list) -> list:
    '''
    Regresa una lista con el número 0 desplazado una casilla hacia abajo.
    Encuentra el índice del número 0.
    Encuentra el índice del número a abajo del cero.
    Si el índice del renglón es igual a 3 entonces no se puede mover.
    Almacena el número en el indice correspondiente al cero.
    Almacena un cero en el índice correspondiente al número abajo del cero.
    '''
    number_index = int()
    # Encontrar el índice del número cero
    space_index = state.index(0)
    # Encontrar el índice del número arriba del cero
    # Si el índice del renglón es igual a 0 entonces no se puede mover
    if getCoordinate(space_index)[0] < PUZZLE_SIZE-1:
        number_index = getIndex(getCoordinate(space_index+4))
        # Almacenar el número en el indice correspondiente al cero
        next_state = state[:]
        next_state[space_index] = next_state[number_index]
        # Almacenar un cero en el índice correspondiente al número a la izquierda del cero
        next_state[number_index] = 0
        if debbug:
            print("Down shifted space")
            print(getCoordinate(space_index), "->",
                  getCoordinate(number_index))
            print(state, len(state), "O")
            print(next_state, len(next_state), "L")
            print()
        return next_state
    if debbug:
        print("Down shifted space")
        print(getCoordinate(space_index), "->", getCoordinate(space_index))
        print(state, len(state), "O")
        print(state, len(state), "L")
        print()
    return state


def printPuzzle(state: list) -> None:
    '''Imprime en la terminal el estado del puzzle'''
    print()
    print("\t{a}\t{b}\t{c}\t{d}".format(
        a=state[0], b=state[1], c=state[2], d=state[3]))
    print("\t{a}\t{b}\t{c}\t{d}".format(
        a=state[4], b=state[5], c=state[6], d=state[7]))
    print("\t{a}\t{b}\t{c}\t{d}".format(
        a=state[8], b=state[9], c=state[10], d=state[11]))
    print("\t{a}\t{b}\t{c}\t{d}".format(
        a=state[12], b=state[13], c=state[14], d=state[15]))
    print()

def getPuzzleStringRepresentation(state: list) -> str:
    '''Regresa una cadena con el estado del puzzle'''
    return "\n\t{a}\t{b}\t{c}\t{d}\n\t{e}\t{f}\t{g}\t{h}\n\t{i}\t{j}\t{k}\t{l}\n\t{m}\t{n}\t{o}\t{p}".format(
        a=state[0], b=state[1], c=state[2], d=state[3],
        e=state[4], f=state[5], g=state[6], h=state[7],
        i=state[8], j=state[9], k=state[10], l=state[11],
        m=state[12], n=state[13], o=state[14], p=state[15])

#################################################################

def manhattan_distance(P1: tuple, P2: tuple) -> float:
    '''The sum of the absolute differences of the Cartesian differences.
    This distance is also known as city block distance, 
    Manhattan distance, or Taxicab.'''
    sum = 0
    if (len(P1) != len(P2)):
      print("Dimensions between P1{p1} and P2{p2} are not equal".format(p1=P1,p2=P2),end=" -> ")
      return None
    for i in range(len(P1)):
        sum = sum+abs(P1[i]-P2[i])
    return float(sum)

def euclidian_distance(P1: tuple, P2: tuple) -> float:
    '''The length of a line segment between the two points.
    Associated with a norm called the Euclidean norm,
    defined as the distance of each vector from the origin.'''
    sum = 0
    if (len(P1) != len(P2)):
      print("Dimensions between P1{p1} and P2{p2} are not equal".format(p1=P1,p2=P2),end=" -> ")
      return None
    for i in range(len(P1)):
        sum = sum+(P1[i]-P2[i])**2
    return float(pow(sum,0.5))

def cosine_distance(P1: tuple, P2: tuple) -> float:
    '''The resulting similarity ranges from −1 meaning exactly opposite,
    to 1 meaning exactly the same, with 0 indicating orthogonality
    or decorrelation, while in-between values indicate intermediate similarity
    or dissimilarity.'''
    sumA = 0
    sumB = 0
    sumAB = 0
    if (len(P1) != len(P2)):
      print("Dimensions between P1{p1} and P2{p2} are not equal".format(p1=P1,p2=P2),end=" -> ")
      return None
    for i in range(len(P1)):
        sumA = sumA + (P1[i]**2)
        sumB = sumB + (P2[i]**2)
        sumAB = sumAB + P1[i]*P2[i]
    return float((sumAB)/((sumA**0.5)*(sumB**0.5)))

def hamming_distance(P1: tuple, P2: tuple) -> float:
    '''The Hamming Distance finds the sum of corresponding elements that differ between two vectors.
    The greater the Hamming Distance is, the more the two vectors differ.
    Inversely, the smaller the Hamming Distance, the more similar the two vectors are.'''
    sum = 0
    if (len(P1) != len(P2)):
      print("Dimensions between P1{p1} and P2{p2} are not equal".format(p1=P1,p2=P2),end=" -> ")
      return None
    for i in range(len(P1)):
        sum = sum + abs(P1[i]-P2[i])
    return float(sum/len(P1))

def computeG(node):
    '''Number of movements done since the initial state.'''
    # Add to Node a level atribute
    # return node._level
    return 0

def computeH(state: list, goal_state)->int:
    '''Number of misplaced cells.'''
    g = PUZZLE_SIZE**2
    for index, number in enumerate(state):
        if number == goal_state[index]:
            g -= 1
    if debbug:
        print("g(n):",g)
    return g

def computeF(state: list, goal_state)->int:
    '''Node value'''
    if debbug:
        print("f(n):",computeH()+computeG(state, goal_state))
    return computeH(state, goal_state)+computeG(state)


def getBestPath(closed: list) -> tuple[list, list]:
    '''Returns the best path based on the closed states.'''
    pass


def getHeuristicValue(actualstate:list, goalState:list) -> int:
    '''Returns the heuristic value of a given state'''
    acum = 0
    for i in range(0, len(actualstate)):
        if actualstate[i] == goalState[i]:
            acum += 1
    return acum


def generateChildren(node: list) -> list:
    '''Returns the Children of a given state'''
    # get the position of the 0
    space_index = node.index(0)
    space_position = getCoordinate(space_index)
    print(space_position, space_index)
    print(getNextMoves(space_position))
    # if movements available generate a list of movements


    printPuzzle(node)
    # printPuzzle(moveUp(node))
    pass


def giveState(child, open: list) -> list:
    '''Give the state (child) on open the shorter path'''
    pass

def removeState(child, statelist: list)->list:
    '''Remove the state from a state list'''
    pass


def isChildNotOpenClosed(child, open: list, closed: list) -> bool:
    '''Returns True if the child is in open or closed.
    Returns False otherwise.'''
    pass


def isChildOpen(child, open: list) -> bool:
    '''Returns True if the child is in open.
    Returns False otherwise.'''
    pass


def isChildClosed(child, closed: list) -> bool:
    '''Returns True if the child is in closed.
    Returns False otherwise.'''
    pass


def isChildShortPath(child) -> bool:
    '''Returns True if the child was reached by a shorter path.
    Returns False otherwise.'''
    pass


def reOrder(open: list) -> list:
    '''Re order states on open by heuristic merit (best leftmost) '''
    pass


def bestFirstSearch(start, goal) -> tuple[list, list]:
    open = [start]
    closed = list()

    # While open != [] do
    while len(open) != 0:
        # Remove leftmost state from open, call it x
        x = open.pop()
        print(x)
        # If x = goal then return the path from start to x
        if x == goal:
            return getBestPath(closed)      # Falta
        else:
            # Generate children of X
            x_node = generateChildren(x)
            print(x_node)
        #     # For each child of x do
        #     for child in x_node:

        #         # If the child is not on open or closed
        #         if isChildNotOpenClosed(child, open, closed):
        #             print("Child is open or closed")
        #             # Assign the child a heuristic value
        #             child.fn = getHeuristicValue()
        #             # Add the child to open
        #             open.append(child)

        #         # If the child is already open
        #         elif isChildOpen(child, open):
        #             print("Child is open")
        #             # If the child was reached by a shorter path
        #             if isChildShortPath(child):
        #                 print("Child was reached by a shorter path")
        #                 # Then give the state on open the shorter path
        #                 open = giveState(child, open)

        #         # If the child is already closed
        #         elif isChildClosed(child, closed):
        #             print("Child is closed")
        #             # If the child was reached by a shorter path
        #             if isChildShortPath(child):
        #                 print("Child was reached by a shorter path")
        #                 # Remove the state from closed
        #                 removeState(closed,child)
        #                 # Add the child to open
        #                 open.append(child)

        #         # Put x on closed
        #         closed.append(x)
        #         # Re order states on open by heuristic merit (best leftmost)
        #         open = reOrder(open)

    return None

def compute_manhattan_distance1(node1: list, node2: list) -> float:
    pos_n1 = getCoordinate(node1.index(0))
    pos_n2 = getCoordinate(node2.index(0))
    return manhattan_distance(pos_n1,pos_n2)

def compute_manhattan_distance2(node1: list, node2: list)->float:
    min = 0.0
    for index, number in enumerate(node1):
        p1 = getCoordinate(number)
        p2 = getCoordinate(node2[index])
        d = manhattan_distance(p1, p2)
        if d < min:
            min = d
    return (PUZZLE_SIZE*PUZZLE_SIZE)-min

def generate_random_state()-> list:
    '''Generates a random state.'''
    state = list()
    while True:
        if len(state) == 16:
            break
        number = random.randint(0,15)
        if state.count(number) == 0:
            state.append(number)
    return state


def test():
    initial_state, goal_state = readFile("Datos.txt")
    # printPuzzle(initial_state)
    # printPuzzle(goal_state)
    # Remplaza g(n)
    # print(computeH(initial_state, goal_state), compute_manhattan_distance1(initial_state, goal_state))
    # Remplaza h(n)     
    # print(computeH(initial_state, goal_state), compute_manhattan_distance2(initial_state, goal_state))
    print(generate_random_state())

if __name__ == "__main__":
    test()