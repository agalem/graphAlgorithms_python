from classes.graph import Graph


def searchCycle(matrix):
    size = len(matrix)
    graph = Graph(size)
    graph.buildFromMatrix(matrix)
    min_graph_degree = graph.findMinGraphDegree()

    if min_graph_degree < 2:
        print("Za niski minimalny stopień grafu")
        return
    else:
        vertexes = []
        cycle = DFS(matrix, 0, vertexes, min_graph_degree)

    print("Cykl: ", cycle)
    return


def DFS(matrix, currentVertex, vertexes, searchedLength):
    print(currentVertex)
    vertexes.append(currentVertex)
    print("Wierzchołki: ", vertexes)

    vertex_connections = matrix[currentVertex]
    for i in range(len(vertex_connections)):
        print(vertex_connections)
        if vertex_connections[i] == 1:
            print("Połączenia z: ", i)
            if i in vertexes:
                if len(vertexes) - vertexes.index(i) <= searchedLength:
                    continue
                else:
                    vertexes = vertexes[vertexes.index(i):]
                    return vertexes
            else:
                return DFS(matrix, i, vertexes, searchedLength)
    return vertexes
