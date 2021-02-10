from problem import Problem
from solver import Solver
from heuristics import Heuristics

depthZero = [[1,2,3], [4,5,6], [7,8,0]]
depthTwo = [[1,2,3], [4,5,6], [0,7,8]]
depthFour = [[1,2,3], [5,0,6], [4,7,8]]
depthEight = [[1,3,6], [5,0,2], [4,7,8]]
depthTwelve = [[1,3,6], [5,0,7], [4,8,2]]
depthSixteen = [[1,6,7], [5,0,3], [4,8,2]]
depthTwenty = [[7,1,2], [4,8,5], [6,3,0]]
depthTwentyFour = [[0,7,2], [4,6,1], [3,5,8]]

def main():
    solver = Solver()
    problem = Problem(depthSixteen)
    heuristics = Heuristics()
    print((solver.generalSearch(problem, solver.bestFirstSearchQueueingFunction, heuristics.h0)).state)

if __name__ == "__main__":
    main()