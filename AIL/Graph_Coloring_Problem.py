def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex: ",
              i, " Color: ", colorArray[i])

def isSafe(graph, colorArray):
    for i in range(4):
        for j in range(i + 1, 4):
            if (graph[i][j] and colorArray[j] == colorArray[i]):
                return False
    return True

def graphColoringAlgorithm(graph, m, i, colorArray):
    if (i == 4):
        if (isSafe(graph, colorArray)):
            printConfiguration(colorArray)
            return True
        return False
    for j in range(1, m + 1):
        colorArray[i] = j
        if (graphColoringAlgorithm(graph, m, i + 1, colorArray)):
            return True
        colorArray[i] = 0
    return False

if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ]
    m = 3

    colorArray = [0 for i in range(4)]
    if (graphColoringAlgorithm(graph, m, 0, colorArray)):
        print("Coloring is possible!")
    else:
        print("Coloring is not possible!")
