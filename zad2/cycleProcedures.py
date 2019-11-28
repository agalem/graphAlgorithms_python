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
        #print(vertex_connections)
        if vertex_connections[i] == 1:
            print("Połączenia z: ", i)
            if i in vertexes:
                # length of the found path is too short
                continue
                '''if len(vertexes) - vertexes.index(i) <= searchedLength:
                    continue
                else:
                    vertexes = vertexes[vertexes.index(i):]
                    return vertexes'''
            else:
                return DFS(matrix, i, vertexes, searchedLength)
    return vertexes


def findJordanCenter(matrix):

    if not isTree(matrix):
        print("Nie jest to drzewo")
        return

    tree_size = len(matrix)

    if tree_size < 3:
        vertexes = [i for i in range(tree_size)]
        return vertexes

    tree = Graph(tree_size)
    tree.buildFromMatrix(matrix)
    vertexes = [i for i in range(tree_size)]

    vertexes_left_size = len(vertexes)
    # max length of the center is 2
    while vertexes_left_size > 2:
        for vertex in list(vertexes):
            degree = tree.findVertexDegree(vertex)
            print("Wierzchołek: ", vertex, "  Stopien: ", degree)
            if degree == 1:
                print("Liśc: ", vertex)
                tree.removeEdgesAssociatedToVertex(vertex)
                # removing leaves
                vertexes.remove(vertex)
        vertexes_left_size = len(vertexes)

    print("Centrum Jordana: ", vertexes)
    return vertexes


def isTree(matrix):
    size = len(matrix)
    edges = 0
    for i in range(size):
        vertex_row = matrix[i]
        vertex_edges = 0

        for j in range(size):
            if vertex_row[j] == 1:
                if i == j:
                    return False
                else:
                    vertex_edges = vertex_edges + 1

        if vertex_edges == 0:
            return False

        edges = edges + vertex_edges

    edges = int(edges / 2)

    if edges == size - 1:
        return True
    return False


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