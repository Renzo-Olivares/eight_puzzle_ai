from collections import deque

def generalSearch(problem, queueingFunction):
    # Initialize queue
    frontier = deque()

    # Add initial state to queue
    initialNode = Node(problem.initialState, None, None, 0)
    frontier.append(initialNode)

    # A lookup table
    reached = {problem.initialState : initialNode}

    while len(frontier) != 0:
        node = frontier.popLeft()

        if problem.isGoal(node.state):
            return node
        
        queueingFunction(frontier, expand(node, problem), reached)
    
    return 'failure'

def expand(node, problem):
    s = node.state
    for action in problem.actions(s):
        sNew = problem.result(s, action)
        cost = node.pathCost + problem.actionCost(s, action, sNew)
        yield Node(sNew, node, action, cost);

def bestFirstSearchQueueingFunction(frontier, expandedNodes, reached):
    for child in expandedNodes:
        s = child.state
        if s not in reached or child.pathCost < reached[s].pathCost:
            reached[s] = child
            frontier.append(child)
