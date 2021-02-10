class Heuristics:
    def h0(self, state):
        # Uniform Cost Search: No heuristic.
        return 0
        
    def h1(self, state):
        # Misplaced Tile Heuristic: The number of misplaced tiles (blank not included).
        pass

    def h2(self, state):
        # Manhattan Distance Heuristic: The sum of the distances of the tiles from their goal positions.
        pass