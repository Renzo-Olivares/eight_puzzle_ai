from problem import Problem
from solver import Solver
from heuristics import Heuristics
from prettyprint import prettyPrint
import random

depthZero = [[1,2,3], [4,5,6], [7,8,0]]
depthTwo = [[1,2,3], [4,5,6], [0,7,8]]
depthFour = [[1,2,3], [5,0,6], [4,7,8]]
depthSeven = [[4,1,2], [5,3,0], [7,8,6]]
depthEight = [[1,3,6], [5,0,2], [4,7,8]]
depthTwelve = [[1,3,6], [5,0,7], [4,8,2]]
depthSixteen = [[1,6,7], [5,0,3], [4,8,2]]
depthSixteen2 = [[1,5,2], [4,8,7], [6,3,0]]
depthTwenty = [[7,1,2], [4,8,5], [6,3,0]]
depthTwentyFour = [[0,7,2], [4,6,1], [3,5,8]]
hardPuzzle = [[8,6,7], [2,5,4], [3,0,1]]
hardPuzzle2 = [[6,4,7], [8,5,0], [3,2,1]]
randomTest = [[1,2,3], [4,8,0], [7,6,5]]
targetPuzzle = [[1,2,3], [4,0,6], [7,5,8]]
unsolvablePuzzle = [[1,0,3], [2,4,5], [6,7,8]]
defaultPuzzles = [depthZero, depthTwo, depthFour, depthSeven, depthEight, depthTwelve, depthSixteen, depthSixteen2, depthTwenty, depthTwentyFour, randomTest, targetPuzzle, hardPuzzle, hardPuzzle2, unsolvablePuzzle]

def main():
    # Setup
    solver = Solver()
    problem = None
    heuristics = Heuristics()
    selectedBoard = None
    solution = None

    # Trace
    open('trace.txt', 'w').close()
    open('solution.txt', 'w').close()
    trace = open('trace.txt', 'a')
    solutionTrace = open('solution.txt', 'a')

    # Text line UI
    print("Welcome to Renzo's 8-puzzle solver.")
    print('Type "1" to use a default puzzle, or "2" to enter your own puzzle.')
    trace.write("Welcome to Renzo's 8-puzzle solver.")
    puzzleSelection = input('')

    if puzzleSelection == '2':
        print('\n\t Enter your puzzle, use a zero to represent the blank')
        row1 = input('\t Enter the first row, use space or tabs between numbers      ').split()
        row2 = input('\t Enter the second row, use space or tabs between numbers     ').split()
        row3 = input('\t Enter the third row, use sgit add pace or tabs between numbers      ').split()
        row1 = [int(i) for i in row1]
        row2 = [int(i) for i in row2]
        row3 = [int(i) for i in row3]
        selectedBoard = [row1, row2, row3]
    else:
        selectedBoard = random.choice(defaultPuzzles)
        print('\n' + prettyPrint(selectedBoard))

    problem = Problem(selectedBoard)

    trace.write('\n\nPuzzle: \n' + prettyPrint(selectedBoard) + '\n')

    print('\n \t Enter your choice of algorithm')
    print('\t 1. Uniform Cost Search')
    print('\t 2. A* with the Misplaced Tile Heuristic')
    print('\t 3. A* with the Manhattan Distance Heuristic')
    algorithmSelection = input('\n\t ')

    if algorithmSelection == '1':
        trace.write('\nUniform Cost Search\n')
        trace.close()
        solution = solver.generalSearch(problem, solver.bestFirstSearchQueueingFunction, heuristics.h0)
    elif algorithmSelection == '2':
        trace.write('\nA* with the Misplaced Tile Heuristic\n')
        trace.close()
        solution = solver.generalSearch(problem, solver.bestFirstSearchQueueingFunction, heuristics.h1)
    elif algorithmSelection == '3':
        trace.write('\nA* with the Manhattan Distance Heuristic\n')
        trace.close()
        solution = solver.generalSearch(problem, solver.bestFirstSearchQueueingFunction, heuristics.h2)

    # Writing solution to file and command line.
    print('The solution path:\n')
    solutionPath = []

    if solution != 'failure':
        while True:
            solutionPath.append(solution.state)
            if solution.parent is None:
                break
            else:
                solution = solution.parent
    else:
        print('\nfailure')
        solutionTrace.write('failure')
        solutionTrace.close()
        exit()

    solutionPath.reverse()

    for board in solutionPath:
        solutionTrace.write(prettyPrint(board) + '\n\n')
        print(prettyPrint(board) + '\n')
    
    solutionTrace.close()

if __name__ == "__main__":
    main()