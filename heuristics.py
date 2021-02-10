class Heuristics:
    def h0(self, state):
        # Uniform Cost Search: No heuristic.
        return 0
        
    def h1(self, state):
        # Misplaced Tile Heuristic: The number of misplaced tiles (blank not included).
        misplacedCount = 0
        goal = self.buildGoal(state)

        # Compare goal state and given state.
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != goal[i][j] and state[i][j] != 0:
                    misplacedCount += 1

        return misplacedCount

    def h2(self, state):
        # Manhattan Distance Heuristic: The sum of the distances of the tiles from their goal positions.
        goal = self.buildGoal(state)

        # Compare goal state and given state.
        # for i in range(len(state)):
        #     for j in range(len(state[i])):
        #         if state[i][j] != goal[i][j] and state[i][j] != 0:
        pass     

    def buildGoal(self, state):
        # Build goal for comparison.
        goal = []
        counter = 1
        temp = [] 

        for i in range(len(state)):
            for j in range(len(state[i])):
                if j == len(state[i]) - 1 and i == len(state) - 1:
                    temp.append(0)
                else:
                    temp.append(counter)
                counter += 1
                if j == len(state[i]) - 1:
                    copy = temp[:]
                    goal.append(copy)
                    temp.clear()
        
        return goal
