import heapq
from node import Node
from prettyprint import prettyPrint

class Solver:
    def generalSearch(self, problem, queueingFunction, heuristicFunction):
        # Initialize queue
        frontier = []

        # Add initial state to queue
        initialNode = Node(problem.initial, None, None, 0)
        heapq.heappush(frontier,(initialNode.pathCost + heuristicFunction(initialNode.state), initialNode))

        # Trace variables
        maxQueue = 0
        nodeCount = 0

        # A lookup table
        reached = {str(problem.initial) : initialNode}

        while len(frontier) != 0:
            if maxQueue < len(frontier):
                maxQueue = len(frontier)

            node = heapq.heappop(frontier)[1]

            if problem.isGoal(node.state):
                print('\nGoal!!')
                print(f'\nTo solve this problem the search algorithm expanded a total of {nodeCount} nodes.')
                print(f'The maximum number of nodes in the queue at any one time was {maxQueue}.')
                print(f'The depth of the goal node was {node.pathCost}.')
                return node
                
            nodeCount += 1

            print(f'\nThe best state to expand with a g(n) = {node.pathCost} and h(n) = {heuristicFunction(node.state)} is...')
            print(prettyPrint(node.state) + '\tExpanding this node...')
            
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
            
            if str(s) not in reached or child.pathCost < reached[str(s)].pathCost:
                reached[str(s)] = child
                heapq.heappush(frontier, (child.pathCost + h(child.state), child))
