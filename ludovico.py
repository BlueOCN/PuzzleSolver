import utils

def main():
    initialState = [1,2,4,7,11,6,12,3,5,10,14,8,9,0,13,15]
    goalState = [1,2,4,7,11,6,12,3,5,10,14,8,9,13,15,0]
    print(utils.computeH(initialState, goalState))
    print(utils.getHeuristicValue(initialState, goalState))

if __name__ == "__main__":
    main()