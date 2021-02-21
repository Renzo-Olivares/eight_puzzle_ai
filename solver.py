import heapq
from node import Node
from prettyprint import prettyPrint

class Solver:
    def generalSearch(self, problem, queueingFunction, heuristicFunction):
        # Source: Derived from general search algorithm given in class[2], and Best-First-Search pseudocode given in Artificial Intelligence: A Modern Approach [1]
        # Initialize queue
        frontier = []

        # Add initial state to queue
        initialNode = Node(problem.initial, None, None, 0)
        heapq.heappush(frontier,(initialNode.pathCost + heuristicFunction(initialNode.state), initialNode))

        # Trace variables
        trace = open('trace.txt', 'a')
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
                print(prettyPrint(node.state))
                print(f'\nTo solve this problem the search algorithm expanded a total of {nodeCount} nodes.')
                print(f'The maximum number of nodes in the queue at any one time was {maxQueue}.')
                print(f'The depth of the goal node was {node.pathCost}.\n')
                trace.write('\nGoal!!')
                trace.write('\n' + prettyPrint(node.state) + '\n')
                trace.write(f'\nTo solve this problem the search algorithm expanded a total of {nodeCount} nodes.')
                trace.write(f'\nThe maximum number of nodes in the queue at any one time was {maxQueue}.')
                trace.write(f'\nThe depth of the goal node was {node.pathCost}.')
                trace.close()
                return node
                
            nodeCount += 1

            print(f'\nThe best state to expand with a g(n) = {node.pathCost} and h(n) = {heuristicFunction(node.state)} is...')
            print(prettyPrint(node.state) + '\tExpanding this node...')
            trace.write(f'\nThe best state to expand with a g(n) = {node.pathCost} and h(n) = {heuristicFunction(node.state)} is...')
            trace.write('\n' + prettyPrint(node.state) + '\tExpanding this node...\n')
            
            queueingFunction(frontier, self.expand(node, problem), reached, heuristicFunction)
        
        return 'failure'

    def expand(self, node, problem):
        # Source: Derived from pseudocode found in [1]
        s = node.state

        for action in problem.actions(s):
            stateCopy = [row[:] for row in s]
            sNew = problem.result(stateCopy, action)
            cost = node.pathCost + problem.actionCost(s, action, sNew)
            yield Node(sNew, node, action, cost)

    def bestFirstSearchQueueingFunction(self, frontier, expandedNodes, reached, h):
        # Source: Derived from pseudocode found in [1]
        for child in expandedNodes:
            s = str(child.state)

            if s not in reached or child.pathCost < reached[s].pathCost:
                reached[s] = child
                heapq.heappush(frontier, (child.pathCost + h(child.state), child))

# Sources
#[1] Artificial Intelligence: A Modern Approach (by Stuart Russell and Peter Norvig, 2020, Pearson, 0-13-461099-7)
#[2] Blind Search and Heuristic Search Class Slides (by Dr. Eamonn Keogh) 