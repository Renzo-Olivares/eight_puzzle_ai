class Problem:
    def __init__(self, initial):
        self.initial = initial # The problem's initial state.

    def isGoal(state):
        # Check if given state is a goal state.
        pass

    def actions(node):
        # Returns the actions available to the agent.
        pass

    def result(node, action):
        # A transitional model, returns the state that results from doing action a on state s.
        pass

    def actionCost(node, action, newNode):
        # Returns the numeric cost of applying action a on state s to reach state s'.
        pass