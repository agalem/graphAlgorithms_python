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


def bfs_color(matrix, colors, vertex=0):
    size = len(matrix)
    visited = [False for i in range(size)]
    queue = [vertex]
    visited[vertex] = True
    colors[vertex] = True

    while queue:
        vertex = queue.pop(0)
        # print(vertex + 1, end=" ")

        # sprawdzanie sąsiadów
        for index, value in enumerate(matrix[vertex]):
            if not visited[index] and value > 0:
                # sąsiad ma ten sam kolor
                if colors[vertex] == colors[index]:
                    print("Nie jest dwudzielny")
                    return False
                # wierzchołek już pokolorowany
                if colors[index] != -1:
                    continue
                # pokolorowanie wierzchołka przeciwnym kolorem
                colors[index] = not colors[vertex]
                queue.append(index)
                visited[index] = True

    print("Jest dwudzielny")
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
    # łączenie wierzchołków
    for vertex in vertexes_left:
        directed_graph.addEdge(source_index, vertex - 1, 1)
        vertex_connections = matrix[vertex - 1]
        for index, value in enumerate(vertex_connections):
            if value != 0:
                directed_graph.addEdge(vertex - 1, index, 1)
    for vertex in vertexes_right:
        directed_graph.addEdge(vertex - 1, sink_index, 1)

    return directed_graph


def max_match(graph):
    if not is_connected(graph):
        print("Podany graf nie jest spójny")
        return

    matrix = graph.getAdjacencyMatrix()
    size = graph.getSize()
    colors = [-1 for i in range(size)]

    bfs_color(matrix, colors)
    print(colors)

    vertexes_left = []
    vertexes_right = []
    for index, value in enumerate(colors):
        if value:
            vertexes_left.append(index + 1)
        else:
            vertexes_right.append(index + 1)
    print("Wierzchołki z lewej: ", vertexes_left)
    print("Wierzchołki z prawej: ", vertexes_right)

    directed_graph = build_bipartite_graph(matrix, size, vertexes_left, vertexes_right)
    dir_matrix = directed_graph.getAdjacencyMatrix()
    dir_size = directed_graph.getSize()

    assigned = [-1 for i in range(dir_size)]
    count = 0

    for vertex in vertexes_left:
        vertex -= 1
        visited = [False for i in range(dir_size)]
        if find_matching(matrix, vertex, visited, assigned):
            count += 1
    print(count)
    return

# TODO użyć metody największego przepływu


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
