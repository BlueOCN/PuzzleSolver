import utils
from Node import Node

def main():
    initial_state, goal_state = utils.readFile("Datos.txt")
    utils.printPuzzle(initial_state)
    E1 = utils.moveDown(initial_state)
    utils.printPuzzle(E1)
    E2 = utils.moveUp(E1)
    utils.printPuzzle(E2)
    # bestFirstSearch(initial_state,goal_state)

    # ----
    # initial_state, goal_state = readFile("Datos.txt")
    # E0 = state(initial_state)
    # EF = state(goal_state)
    # path, steps = bestFirstSearch(E0,EF)
    # print(path)   # Lista de estados
    # print(steps)  # Lista de pasos
    

if __name__ == "__main__":
    main()