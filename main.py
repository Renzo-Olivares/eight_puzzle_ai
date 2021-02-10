from problem import Problem

goalOne = [[1,2,3], [4,5,6], [7,8,0]]
goalTwo = [[0,1,2], [3,4,5], [6,7,8]]
goalOneAlternate = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]
goalTwoAlternate = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
goalFailure = [[1,2,3], [4,5,0], [6,7,8]]
goalFailureAlternate = [[0,1,2,3], [10,5,6,7], [8,9,4,11], [12,13,14,15]]

def main():
    problem = Problem([[1,2,3], [4,5,6], [7,8,0]])
    print(problem.isGoal(goalFailureAlternate))
    print(problem.actions([[2,3,4], [6,1,7], [8,0,5]]))
    print(problem.result([[1,2,3], [4,0,6], [7,8,5]], 'down'))

if __name__ == "__main__":
    main()