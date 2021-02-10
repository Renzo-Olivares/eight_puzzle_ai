import random

class Node:
    def __init__(self, state, parent, action, pathCost):
        self.state = state; # The state to which the node corresponds.
        self.parent = parent; # The node in the tree that generated this node.
        self.action = action; # The action that was applied to the parent's state to generate this node.
        self.pathCost = pathCost; # The total cost of the path from the initial state to this node. In mathematical formulas, we use g(node) as a synonym for path-cost.
    
    def __lt__(self, other):
        # Overload the less than operator. This function is called when there needs to be a tie break.
        return random.choice([self,other])
