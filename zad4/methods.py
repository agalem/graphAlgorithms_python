from classes.stack import Stack
from classes.weightedDigraph import WeightedDigraph

def build_network_from_file(path):
    file = open(path, "r")
    lines = [line.rstrip('\n') for line in file]
    file.close()

    graph_size = int(lines[0])
    edges_size = int(lines[1])
    edges = lines[2:]

    if len(edges) != edges_size:
        print("Podano niewłaściwą liczbę krawędzi - %d" % len(edges))
        return

    weighted_digraph = WeightedDigraph(graph_size)

    for edge in edges:
        edge = edge.split()
        if len(edge) != 3:
            print("\n\nNie utworzono grafu z wagami krawędzi")
            print("Nieprawidłowa linijka: ", edge)
            return
        vertex_from = int(edge[0]) - 1
        vertex_to = int(edge[1]) - 1
        vertex_weight = int(edge[2])
        weighted_digraph.addEdge(vertex_from, vertex_to, vertex_weight)

    weighted_digraph.toString()
    return weighted_digraph

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

    output = digraph_connections(components, matrix)

    if output:
        print("Sieć jest spójna")
    else:
        print("Sieć nie jest spójna")

    return output

def digraph_connections(components, matrix):

    size = len(matrix)
    initial = components[0]
    components.pop(0)
    for block in components:
        for elem in block:
            connections = matrix[elem - 1]
            for index, value in enumerate(connections):
                if value != 0 and index + 1 in initial:
                    initial.append(elem)
    return len(initial) == size

def dfs_components(current_vertex, matrix, stack, visited, visited_bool):

    connections = matrix[current_vertex - 1]

    if not visited_bool[current_vertex - 1]:
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


def has_negative_flow(matrix):
    output = False

    for row in matrix:
        for value in row:
            if value < 0:
                output = True
                return output

    return output


def has_reversed_edge(matrix):
    size = len(matrix)
    edges = []
    visited = [False for i in range(size)]

    for rowNum in range(size):
        for colNum in range(size):
            if matrix[rowNum][colNum] != 0 and matrix[colNum][rowNum] != 0 and \
                    (not visited[rowNum] or not visited[colNum]):
                edges.append([rowNum + 1, colNum + 1])
                visited[rowNum] = True
                visited[colNum] = True
    return edges


def has_loop(matrix):
    size = len(matrix)
    output = False

    for i in range(size):
        if matrix[i][i] != 0:
            output = True
            return output

    return output


def maximum_flow(graph):
    matrix = graph.getAdjacencyMatrix()
    size = graph.getSize()

    sources = find_source(matrix, size)
    sinks = find_sink(matrix, size)

    if not is_connected(graph):
        print("Podana sieć nie jest spójna")
        return

    if has_negative_flow(matrix):
        print("Jedna z krawędzi ma ujemną przepustowość")
        return

    if has_loop(matrix):
        print("W sieci występuje pętla")
        return

    # sieć ma krawędzie przeciwnie skierowane
    edges = has_reversed_edge(matrix)
    if len(edges) > 0:
        print("Graf zawiera krawędź skierowaną przeciwnie")
        print(edges)

        for edge in edges:
            vertex_from = edge[0]
            vertex_from_index = vertex_from - 1
            vertex_to = edge[1]
            vertex_to_index = vertex_to - 1
            edge_weight = matrix[vertex_from_index][vertex_to_index]

            graph.addVertex()
            new_vertex = graph.getSize()
            new_vertex_index = new_vertex - 1
            print("Dodano nowy wierzchołek ", vertex_from, new_vertex, vertex_to)

            graph.removeEdge(vertex_from_index, vertex_to_index)
            graph.addEdge(vertex_from_index, new_vertex_index, edge_weight)
            graph.addEdge(new_vertex_index, vertex_to_index, edge_weight)

        for row in graph.getAdjacencyMatrix():
            print(row)

        matrix = graph.getAdjacencyMatrix()
        size = graph.getSize()

    # sieć ma kilka źródeł
    if len(sources) > 1:
        print("Sieć ma kilka źródeł: ", sources)
        print("Dodano superźródło")
        graph.addVertex()
        new_source_index = graph.getSize() - 1

        for source in sources:
            print("Łączenie ", new_source_index + 1, " i ", source)
            graph.addEdge(new_source_index, source - 1, float("Inf"))
        for row in graph.getAdjacencyMatrix():
            print(row)

        source = new_source_index + 1
    else:
        source = sources[0]

    # sieć ma kilka ujść
    if len(sinks) > 1:
        print("Sieć ma kilka ujść: ", sinks)
        print("Dodano superujście")
        graph.addVertex()
        new_sink_index = graph.getSize() - 1

        for sink in sinks:
            print("Łączenie ", new_sink_index + 1, " i ", sink)
            graph.addEdge(sink - 1, new_sink_index, float("Inf"))
        for row in graph.getAdjacencyMatrix():
            print(row)

        sink = new_sink_index + 1
    else:
        sink = sinks[0]

    print("Source: ", source, ", Sink: ", sink)

    parents = [-1 for i in range(size)]
    max_flow = 0

    while BFS_maximum_flow(matrix, source, sink, parents):
        min_path_flow = float("Inf")

        # szukamy minimalną wartość w ścieżce przepływu
        vertex = sink - 1
        while vertex != source - 1:
            min_path_flow = min(min_path_flow, matrix[parents[vertex]][vertex])
            vertex = parents[vertex]

        max_flow += min_path_flow

        # zmianiamy wartości w macierzy sąsiedztwa
        vertex = sink - 1
        while vertex != source - 1:
            ver_parent = parents[vertex]
            matrix[ver_parent][vertex] -= min_path_flow
            matrix[vertex][ver_parent] += min_path_flow
            vertex = parents[vertex]

    print("Maksymalny przepływ: ", max_flow)

    return max_flow


def BFS_maximum_flow(matrix, s, t, parent):
    size = len(matrix)
    visited = [False for i in range(size)]

    source = s - 1
    sink = t - 1

    queue = [source]
    visited[source] = True

    while queue:
        vertex = queue.pop(0)

        for index, value in enumerate(matrix[vertex]):
            if not visited[index] and value > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = vertex
                if visited[sink]:
                    return True

    return False


def analyze_graph(graph):

    matrix = graph.getAdjacencyMatrix()
    size = graph.getSize()

    sources = find_source(matrix, size)
    sinks = find_sink(matrix, size)

    if not is_connected(graph):
        print("Podana sieć nie jest spójna")
        return

    if has_negative_flow(matrix):
        print("Jedna z krawędzi ma ujemną przepustowość")
        return

    if has_loop(matrix):
        print("W sieci występuje pętla")
        return

    # sieć ma krawędzie przeciwnie skierowane
    edges = has_reversed_edge(matrix)
    if len(edges) > 0:
        print("Graf zawiera krawędź skierowaną przeciwnie")
        print(edges)

        for edge in edges:
            vertex_from = edge[0]
            vertex_from_index = vertex_from - 1
            vertex_to = edge[1]
            vertex_to_index = vertex_to - 1
            edge_weight = matrix[vertex_from_index][vertex_to_index]

            graph.addVertex()
            new_vertex = graph.getSize()
            new_vertex_index = new_vertex - 1
            print("Dodano nowy wierzchołek ", vertex_from, new_vertex, vertex_to)

            graph.removeEdge(vertex_from_index, vertex_to_index)
            graph.addEdge(vertex_from_index, new_vertex_index, edge_weight)
            graph.addEdge(new_vertex_index, vertex_to_index, edge_weight)

        for row in graph.getAdjacencyMatrix():
            print(row)

        matrix = graph.getAdjacencyMatrix()
        size = graph.getSize()

    # sieć ma kilka źródeł
    if len(sources) > 1:
        print("Sieć ma kilka źródeł: ", sources)
        print("Dodano superźródło")
        graph.addVertex()
        new_source_index = graph.getSize() - 1

        for source in sources:
            print("Łączenie ", new_source_index + 1, " i ", source)
            graph.addEdge(new_source_index, source - 1, float("Inf"))
        for row in graph.getAdjacencyMatrix():
            print(row)

        source = new_source_index + 1
    else:
        source = sources[0]

    # sieć ma kilka ujść
    if len(sinks) > 1:
        print("Sieć ma kilka ujść: ", sinks)
        print("Dodano superujście")
        graph.addVertex()
        new_sink_index = graph.getSize() - 1

        for sink in sinks:
            print("Łączenie ", new_sink_index + 1, " i ", sink)
            graph.addEdge(sink - 1, new_sink_index, float("Inf"))
        for row in graph.getAdjacencyMatrix():
            print(row)

        sink = new_sink_index + 1
    else:
        sink = sinks[0]

    print("Source: ", source, ", Sink: ", sink)

    parents = [-1 for i in range(size)]
    vertex_mark = [0 for i in range(size)]
    vertex_mark[source - 1] = float("Inf")

    max_flow = 0
    min_cuts = []
    augmenting_paths = []

    while BFS_augmenting_path(matrix, source, sink, parents, vertex_mark):

        path_flow = vertex_mark[sink - 1]
        max_flow += path_flow

        vertex = sink - 1
        path = []

        print(vertex_mark)

        # odtwarzanie ścieżki powiększającej
        while vertex != source - 1:
            ver_parent = parents[vertex]
            matrix[ver_parent][vertex] -= path_flow
            path.append(vertex + 1)
            vertex = parents[vertex]

        path.append(source)

        # minimalny przekrój
        for i in range(len(path) - 1):
            next_vertex = path[i] - 1
            previous_vertex = path[i + 1] - 1
            if matrix[previous_vertex][next_vertex] == 0:
                min_cuts.append([previous_vertex + 1, next_vertex + 1])
                break

        augmenting_paths.append(path[::-1])

        vertex_mark = [0 for i in range(size)]
        vertex_mark[source - 1] = float("Inf")

    print("Maksymalny przepływ: ", max_flow)
    print("Ścieżki rozszerzające: ", augmenting_paths)
    print("Minimalny przekrój: ", min_cuts)

    return


def BFS_augmenting_path(matrix, s, t, parents, vertex_mark):
    size = len(matrix)
    visited = [False for i in range(size)]

    source = s - 1
    sink = t - 1

    queue = [source]
    visited[source] = True

    while queue:
        vertex = queue.pop(0)

        for index, value in enumerate(matrix[vertex]):
            if not visited[index] and value > 0:
                queue.append(index)
                visited[index] = True
                parents[index] = vertex

                vertex_mark[index] = min(matrix[vertex][index], vertex_mark[vertex])

                if visited[sink]:
                    return True

    return False


def find_source(matrix, size):
    sources = []

    for colNum in range(size):
        sum = 0
        for rowNum in range(size):
            sum += matrix[rowNum][colNum]
        if sum == 0:
            sources.append(colNum + 1)

    return sources


def find_sink(matrix, size):
    sinks = []

    for rowNum in range(size):
        sum = 0
        for colNum in range(size):
            sum += matrix[rowNum][colNum]
        if sum == 0:
            sinks.append(rowNum + 1)

    return sinks

