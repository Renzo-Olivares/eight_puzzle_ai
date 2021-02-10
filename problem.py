class Problem:
    def __init__(self, initial):
        self.initial = initial # The problem's initial state.

    def isGoal(self, state):
        # Check if given state is a goal state.
        goalArr = []

        for i in range(len(state)):
            for j in range(len(state[i])):
                goalArr.append(state[i][j])

        # if goalArr[0] == 0:
        #     firstPossibility = goalArr[1:]
        #     firstPossibility.sort()

        #     if firstPossibility == goalArr[1:]:
        #         return True
        if goalArr[len(goalArr) - 1] == 0:
            secondPossibility = goalArr[:len(goalArr) - 1]
            secondPossibility.sort()

            if secondPossibility == goalArr[:len(goalArr) - 1]:
                return True
        else:
            return False

    def actions(self, state):
        # Returns the actions available to the state.
        actions = []

        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    # Check up direction.
                    if i - 1 >= 0:
                        actions.append('up')
                    # Check down direction.
                    if i + 1 <= len(state) - 1:
                        actions.append('down')
                    # Check right direction.
                    if j + 1 <= len(state[i]) - 1:
                        actions.append('right')
                    # Check left direction.
                    if j - 1 >= 0:
                        actions.append('left')
                    
                    return actions
                else:
                    continue

    def result(self, state, action):
        # A transitional model, returns the state that results from doing action a on state s.
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    save = None

                    if action == 'up':
                        save = state[i - 1][j]
                        state[i - 1][j] = 0
                    elif action == 'down':
                        save = state[i + 1][j]
                        state[i + 1][j] = 0
                    elif action == 'right':
                        save = state[i][j + 1]
                        state[i][j + 1] = 0
                    elif action == 'left':
                        save = state[i][j - 1]
                        state[i][j - 1] = 0

                    state[i][j] = save

                    return state
                else:
                    continue

    def actionCost(self, state, action, newState):
        # Returns the numeric cost of applying action a on state s to reach state s'.
        return 1