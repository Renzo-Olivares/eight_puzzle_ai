def prettyPrint(state):
    prettyGrid = ''

    for i in range(len(state)):
        if i > 0:
            prettyGrid += '\n'
        for j in range(len(state[i])):
            if j != len(state[i]):
                prettyGrid += str(state[i][j]) + ' '
            else:
                prettyGrid += str(state[i][j])
    
    return prettyGrid
