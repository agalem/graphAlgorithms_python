from classes.graph import Graph

seriesHistory = []


def isGraphSeries(series):
    initialSum = sumListElements(series)
    if not isEven(initialSum):
        print("Nie jest ciągiem grafowym")
        return False
    seriesHistory.append(series)
    return checkGraphSeries(series)


def checkGraphSeries(series):
    series.sort(reverse=True)
    amountToDecrease = series[0]
    seriesToCheck = series[1:]
    if len(seriesToCheck) < amountToDecrease:
        print("długośc")
        return False
    else:
        newSeries = modifyListElements(seriesToCheck, amountToDecrease)
        sum = sumListElements(newSeries)
        if sum % 2 != 0:
            print("Nie jest to ciąg grafowy")
            seriesHistory.clear()
            return False
        elif sum == 0:
            seriesHistory.append(newSeries)
            seriesHistory.reverse()
            print("Historia: ", seriesHistory)
            print("Jest to ciąg grafowy")
            buildGraphMatrix(seriesHistory)
            return True
        else:
            seriesHistory.append(newSeries)
            checkGraphSeries(newSeries)
    seriesHistory.clear()
    return False


def modifyListElements(list, amount):
    for i in range(amount):
        if int(list[i] <= 0):
            continue
        list[i] = int(list[i] - 1)
    return list


def isEven(num):
    if num % 2 == 0:
        return True
    return False


def sumListElements(list):
    size = len(list)
    sum = 0
    for i in range(size):
        sum += int(list[i])
    return sum


def buildGraphMatrix(history):
    graphSize = len(history[0])
    historySize = len(history)
    graph = Graph(graphSize)
    matrix = graph.getAdjacencyMatrix()
    degrees_indexes = graph.getAllDegreesWithIndexes()

    for i in range(1, historySize):
        connections_amount = history[i][0]
        print("Ilość połączeń do dodania: ", connections_amount)
        print("Historia: ", history[i])
        graph.addVertex()
        for j in range(1, connections_amount + 1):
            searched_vertex_degree = history[i][j] - 1
            print("Szukany stopień: ", searched_vertex_degree)

            # get index of a first vertex of searched degree from a degrees_indexes dictionary
            vertex_index = list(degrees_indexes.keys())[list(degrees_indexes.values()).index(searched_vertex_degree)]
            last_vertex_index = graph.getLastVertexIndex()

            # add an edge between found vertex of a given degree and the last vertex
            graph.addEdge(vertex_index, last_vertex_index)
            degrees_indexes = graph.getAllDegreesWithIndexes()

    print("\nMacierz sąsiedztwa:")
    for row in matrix:
        for value in row:
            print('{0:5}'.format(value), end=' ')
        print()
    return graph.getAdjacencyMatrix()


def hasC3Cycle(adjMatrix):
    size = len(adjMatrix)
    for rowNum in range(size):
        for colmnNum in range(size):
            if rowNum == colmnNum:
                continue
            elif adjMatrix[rowNum][colmnNum] == 1:
                cyclePath = checkIfCycle(adjMatrix, rowNum, colmnNum)
                if len(cyclePath) == 3:
                    print("Zawiera podgraf izomorficzny do cyklu C3")
                    return True
    print("Nie zawiera podgrafu izomorficznego do cyklu C3")
    return False

def hasC3CycleByMatrixMultipication(adjMatrix):
    resultMatrix = multiplyMatrixes(multiplyMatrixes(adjMatrix, adjMatrix), adjMatrix)
    size = len(resultMatrix)
    for i in range(size):
        if resultMatrix[i][i] > 0:
            print("Zawiera podgraf izomorficzny do cyklu C3")
            return True
    print("Nie zawiera podgrafu izomorficznego do cyklu C3")
    return False


# checks if there is a connection between second vertex and first vertex which comes through another vertex
def checkIfCycle(adjMatrix, firstVertex, secondVertex):
    visited = [firstVertex, secondVertex]
    size = len(adjMatrix)
    for index in range(size):
        if index == firstVertex or index == secondVertex:
            continue
        elif adjMatrix[secondVertex][index] == 1:
            if adjMatrix[index][firstVertex] == 1:
                visited.append(index)
                print('Visited :', visited)
                return visited
    return visited


def multiplyMatrixes(mat1, mat2):
    zip_mat2 = zip(*mat2)
    zip_mat2 = list(zip_mat2)
    return [[sum(elem_a*elem_b for elem_a, elem_b in zip(row_a, col_b))
             for col_b in zip_mat2] for row_a in mat1]


def buildGraphFromFile(path):
    file = open(path, "r")
    lines = [line.rstrip('\n') for line in file]
    file.close()

    graph_size = int(lines[0])
    edges_size = int(lines[1])
    edges = lines[2:]

    if len(edges) != edges_size:
        print("Podano niewłaściwą liczbę krawędzi - %d" % len(edges))
        return

    graph = Graph(graph_size)

    for edge in edges:
        edge = edge.split()
        vertex_from = int(edge[0])
        vertex_to = int(edge[1])
        graph.addEdge(vertex_from, vertex_to)

    print(graph.getAdjacencyMatrix())
    return graph