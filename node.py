import random

class Node:
    def __init__(self, state, parent, action, pathCost):
        self.state = state; # From Artificial Intelligence: A Modern Approach: "The state to which the node corresponds"[1].
        self.parent = parent; # From Artificial Intelligence: A Modern Approach: "The node in the tree that generated this node"[1].
        self.action = action; # From Artificial Intelligence: A Modern Approach: "The action that was applied to the parent's state to generate this node"[1].
        self.pathCost = pathCost; # From From Artificial Intelligence: A Modern Approach: "The total cost of the path from the initial state to this node. In mathematical formulas, we use g(node) as a synonym for path-cost"[1].
    
    def __lt__(self, other):
        # Overload the less than operator. This function is called when there needs to be a tie break.
        return random.choice([self,other])

# Sources
# Comments are from textbook [1], code is my own.
#[1] Artificial Intelligence: A Modern Approach (by Stuart Russell and Peter Norvig, 2020, Pearson, 0-13-461099-7)
