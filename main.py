from problem import Problem
from solver import Solver
from heuristics import Heuristics
from prettyprint import prettyPrint
import random

depthZero = [[1,2,3], [4,5,6], [7,8,0]]
depthTwo = [[1,2,3], [4,5,6], [0,7,8]]
depthFour = [[1,2,3], [5,0,6], [4,7,8]]
depthEight = [[1,3,6], [5,0,2], [4,7,8]]
depthTwelve = [[1,3,6], [5,0,7], [4,8,2]]
depthSixteen = [[1,6,7], [5,0,3], [4,8,2]]
depthTwenty = [[7,1,2], [4,8,5], [6,3,0]]
depthTwentyFour = [[0,7,2], [4,6,1], [3,5,8]]
random = [[1,2,3], [4,8,0], [7,6,5]]
defaultPuzzles = [depthZero, depthTwo, depthFour, depthEight, depthTwelve, depthSixteen, depthTwenty, depthTwentyFour, random]

def main():
    # Setup
    solver = Solver()
    problem = None
    heuristics = Heuristics()
    selectedBoard = None

    # Text line UI
    print("Welcome to Renzo's 8-puzzle solver.")
    print('Type "1" to use a default puzzle, or "2" to enter your own puzzle.')
    puzzleSelection = input('')

    if puzzleSelection == '2':
        print('\n\t Enter your puzzle, use a zero to represent the blank')
        row1 = input('\t Enter the first row, use space or tabs between numbers      ').split()
        row2 = input('\t Enter the second row, use space or tabs between numbers     ').split()
        row3 = input('\t Enter the third row, use space or tabs between numbers      ').split()
        row1 = [int(i) for i in row1]
        row2 = [int(i) for i in row2]
        row3 = [int(i) for i in row3]
        selectedBoard = [row1, row2, row3]
    else:
        selectedBoard = depthTwenty
        print('\n' + prettyPrint(selectedBoard))

    problem = Problem(selectedBoard)

    print('\n \t Enter your choice of algorithm')
    print('\t 1. Uniform Cost Search')
    print('\t 2. A* with the Misplaced Tile Heuristic')
    print('\t 3. A* with the Manhattan Distance Heuristic')
    algorithmSelection = input('\n\t ')

    if algorithmSelection == '1':
        solver.generalSearch(problem, solver.bestFirstSearchQueueingFunction, heuristics.h0)
    elif algorithmSelection == '2':
        solver.generalSearch(problem, solver.bestFirstSearchQueueingFunction, heuristics.h1)
    elif algorithmSelection == '3':
        solver.generalSearch(problem, solver.bestFirstSearchQueueingFunction, heuristics.h2)

if __name__ == "__main__":
    main()