from collections import deque
from node import Node
from prettyprint import prettyPrint

class Solver:
    def generalSearch(self, problem, queueingFunction, heuristicFunction):
        # Initialize queue
        frontier = deque()

        # Add initial state to queue
        initialNode = Node(problem.initial, None, None, 0)
        frontier.append(initialNode)

        # Trace variables
        maxQueue = 0

        # A lookup table
        reached = {str(problem.initial) : initialNode}

        while len(frontier) != 0:
            if maxQueue < len(frontier):
                maxQueue = len(frontier)

            node = frontier.popleft()
            print('\n' + prettyPrint(node.state))

            if problem.isGoal(node.state):
                print('\nGoal!!')
                print('\nTo solve this problem the search algorithm expanded a total of x nodes.')
                print(f'The maximum number of nodes in the queue at any one time was {maxQueue}.')
                print(f'The depth of the goal node was {node.pathCost}.')
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
