from collections import deque
from node import Node
from heuristics import Heuristics

class Solver:
    def generalSearch(self, problem, queueingFunction, heuristicFunction):
        # Initialize queue
        frontier = deque()

        # Add initial state to queue
        initialNode = Node(problem.initial, None, None, 0)
        frontier.append(initialNode)

        # A lookup table
        reached = {str(problem.initial) : initialNode}

        while len(frontier) != 0:
            node = frontier.popleft()

            if problem.isGoal(node.state):
                return node
            
            queueingFunction(frontier, self.expand(node, problem), reached, heuristicFunction)
        
        return 'failure'

    def expand(self, node, problem):
        s = node.state

        for action in problem.actions(s):
            stateCopy = [row[:] for row in s]
            sNew = problem.result(stateCopy, action)
            cost = node.pathCost + problem.actionCost(s, action, sNew)
            yield Node(sNew, node, action, cost)

    def bestFirstSearchQueueingFunction(self, frontier, expandedNodes, reached, h):
        for child in expandedNodes:
            s = child.state
            
            if str(s) not in reached or child.pathCost + h(s) < reached[str(s)].pathCost + h(reached[str(s)].state):
                reached[str(s)] = child
                frontier.append(child)
