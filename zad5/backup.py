from classes.stack import Stack
from classes.graph import Graph
from classes.weightedDigraph import WeightedDigraph

def build_graph_from_file(path):
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
        if len(edge) != 2:
            print("\n\nNie utworzono grafu")
            print("Nieprawidłowa linijka: ", edge)
            return
        vertex_from = int(edge[0]) - 1
        vertex_to = int(edge[1]) - 1
        graph.addEdge(vertex_from, vertex_to)

    graph.toString()
    return graph


def build_bipartite_graph_from_file(path):
    file = open(path, "r")
    lines = [line.rstrip('\n') for line in file]
    file.close()

    graph_size = int(lines[0])
    edges_size = int(lines[1])
    edges = lines[2:]
    vertexes_left = []
    vertexes_right = []

    if len(edges) != edges_size:
        print("Podano niewłaściwą liczbę krawędzi - %d" % len(edges))
        return

    graph = WeightedDigraph(graph_size)

    # dodaj źródło
    graph.addVertex()
    source_index = graph_size

    #dodaj ujście
    graph.addVertex()
    sink_index = graph_size + 1

    for edge in edges:
        edge = edge.split()
        if len(edge) != 2:
            print("\n\nNie utworzono grafu")
            print("Nieprawidłowa linijka: ", edge)
            return
        vertex_from = int(edge[0]) - 1
        if vertex_from not in vertexes_left:
            vertexes_left.append(vertex_from)
        graph.addEdge(source_index, vertex_from, 1)

        vertex_to = int(edge[1]) - 1
        if vertex_to not in vertexes_right:
            vertexes_right.append(vertex_to)
        graph.addEdge(vertex_from, vertex_to, 1)
        graph.addEdge(vertex_to, sink_index, 1)

    graph.add_vertexes_left(vertexes_left)
    graph.add_vertexes_right(vertexes_right)

    graph.toString()
    return graph

def is_connected(graph):
    size = graph.getSize()
    matrix = graph.getAdjacencyMatrix()

    stack = Stack()
    visited_bool = [False for i in range(size)]
    components = []
    components_amount = 0

    for vertex in range(size):
        if visited_bool[vertex]:
            continue
        else:
            visited = []
            visited = dfs_components(vertex + 1, matrix, stack, visited, visited_bool)
            components.append(visited)
            components_amount += 1

    print("\nComponents: ", components, "\nComponents amount: ", components_amount)

    if components_amount > 1:
        print("Graf nie jest spójny\n")
        output = False
    else:
        print("Graf jest spójny\n")
        output = True

    return output


def dfs_components(current_vertex, matrix, stack, visited, visited_bool):
    connections = matrix[current_vertex - 1]

    if not visited_bool[current_vertex - 1]:
        # print("Odwiedzenie ", current_vertex, ", odwiedzone: ", visited)
        visited_bool[current_vertex - 1] = True
        visited.append(current_vertex)
        stack.push(current_vertex)

    for i in range(len(connections)):
        if i != current_vertex - 1 and connections[i] != 0 and not visited_bool[i]:
            return dfs_components(i + 1, matrix, stack, visited, visited_bool)
    stack.pop()

    if stack.is_empty():
        return visited

    return dfs_components(stack.last_element(), matrix, stack, visited, visited_bool)


def is_bipartite(matrix, size, colored_verticles):
    colors = [0 for i in range(size)]
    queue = []

    for vertex in range(size):
        if colors[vertex] != 0:
            continue
        colors[vertex] = 1
        queue.append(vertex)
        while queue:
            queue_vertex = queue.pop(0)
            connections = matrix[queue_vertex]
            for index, value in enumerate(connections):
                if value == 1:
                    if colors[index] != 0:
                        continue
                    if colors[index] == colors[queue_vertex]:
                        # print("Index; ", index, " Vertex: ", queue_vertex)
                        print("Nie jest dwudzielny")
                        colored_verticles.append(colors)
                        return False
                    colors[index] = colors[queue_vertex] * -1
                    queue.append(index)
    print("Jest dwudzielny")
    colored_verticles.append(colors)
    return True

def build_bipartite_graph(matrix, size, vertexes_left, vertexes_right):
    # modyfikacja grafu na podstawie kolorowania
    directed_graph = WeightedDigraph(size)
    # dodanie źródła
    directed_graph.addVertex()
    source_index = size
    # dodanie ujścia
    directed_graph.addVertex()
    sink_index = size + 1

    for vertex in vertexes_left:
        # dodawanie krawędzi od źródła do wierzchołków po lewej
        directed_graph.addEdge(source_index, vertex - 1, 1)
        print("Dodawanie krawędzi ", source_index + 1, vertex)
        vertex_connections = matrix[vertex - 1]
        for index, value in enumerate(vertex_connections):
            if value != 0:
                # łączenie wierzchołków po lewej stronie z tymi po prawej
                directed_graph.addEdge(vertex - 1, index, 1)
                print("Dodawanie krawędzi ", vertex, index + 1)
    for vertex in vertexes_right:
        # dodawanie krawędzi od wierzchołków po prawej do ujścia
        directed_graph.addEdge(vertex - 1, sink_index, 1)
        print("Dodawanie krawędzi ", vertex, sink_index + 1)

    return directed_graph


def find_max_match(graph):

    # wprowadzenie zwykłego grafu
    if graph.getType() == "graph":

        if not is_connected(graph):
            print("Podany graf nie jest spójny")
            return

        matrix = graph.getAdjacencyMatrix()
        size = graph.getSize()

        colors = []
        #kolorowanie
        if not is_bipartite(matrix, size, colors):
            colors = colors[0]
            print(colors)
            return

        colors = colors[0]
        print(colors)

        vertexes_left = []
        vertexes_right = []
        for index, value in enumerate(colors):
            if value == 1:
                vertexes_left.append(index + 1)
            else:
                vertexes_right.append(index + 1)
        print("\nWierzchołki z lewej: ", vertexes_left)
        print("Wierzchołki z prawej: ", vertexes_right)
        print()

        directed_graph = build_bipartite_graph(matrix, size, vertexes_left, vertexes_right)
        dir_matrix = directed_graph.getAdjacencyMatrix()
        dir_size = directed_graph.getSize()
    # wprowadzenie grafu już podzielonego
    else:
        directed_graph = graph
        dir_matrix = directed_graph.getAdjacencyMatrix()
        dir_size = directed_graph.getSize()
        vertexes_right = directed_graph.get_vertexes_right()
        vertexes_left = directed_graph.get_vertexes_left()

    # assigned = [-1 for i in range(dir_size)]
    # count = 0

    # for vertex in vertexes_left:
    #     vertex -= 1
    #     visited = [False for i in range(dir_size)]
    #     if find_matching(matrix, vertex, visited, assigned):
    #         count += 1
    # print(count)

    for row in dir_matrix:
        print(row)

    source = dir_size - 1
    sink = dir_size
    parents = [-1 for i in range(dir_size)]
    max_flow = 0
    max_matching = [-1 for i in range(dir_size)]

    while BFS_maximum_flow(dir_matrix, source, sink, parents):
        min_path_flow = float("Inf")

        # szukamy minimalną wartość w ścieżce przepływu
        vertex = sink - 1
        while vertex != source - 1:
            min_path_flow = min(min_path_flow, dir_matrix[parents[vertex]][vertex])
            vertex = parents[vertex]

        max_flow += min_path_flow

        vertex = sink - 1
        while vertex != source - 1:
            ver_parent = parents[vertex]
            # zapisywanie skojarzeń
            max_matching[vertex] = ver_parent
            # zmianiamy wartości w macierzy sąsiedztwa
            dir_matrix[ver_parent][vertex] -= min_path_flow
            dir_matrix[vertex][ver_parent] += min_path_flow
            vertex = parents[vertex]

        print("Parents: ", parents)
        print("Max matching list: ", max_matching)

    print("Maksymalny przepływ: ", max_flow)

    # budowanie maksymalnego skojarzenia na podstawie wartości z tablicy parents na indeksach wierzchołków po prawej
    max_matching_edges = []
    for vertex in vertexes_right:
        vertex_from = max_matching[vertex - 1] + 1
        if vertex_from not in vertexes_left:
            continue
        vertex_to = vertex
        max_matching_edges.append([vertex_from, vertex_to])

    sorted_max_matching_edges = sorted(max_matching_edges, key = lambda x: x[0])

    print("\n")
    print("Maksymalne skojarzenie: ", sorted_max_matching_edges)

    return sorted_max_matching_edges


def BFS_maximum_flow(matrix, s, t, parent):
    size = len(matrix)
    visited = [False for i in range(size)]

    source = s - 1
    sink = t - 1

    queue = [source]
    visited[source] = True

    print("\nPrzejście BFS:")

    while queue:
        vertex = queue.pop(0)

        for index, value in enumerate(matrix[vertex]):
            if not visited[index] and value > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = vertex
                print("Rodzic: ", vertex, " Wierzchołek: ", index)
                if visited[sink]:
                    return True

    return False



def find_matching(matrix, v, visited, assigned):
    connections = matrix[v]
    for index, value in enumerate(connections):
        if value == 1 and not visited[index]:
            visited[index] = True
            if assigned[index] == -1 or find_matching(matrix, assigned[index], visited, assigned):
                assigned[index] = v
                print("Przypisania:\n", assigned)
                print([v, index], "\n")
                return True
    return False
