import copy
from classes.stack import Stack
from classes.multigraph import Multigraph
from classes.weightedGraph import WeightedGraph

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

    graph = WeightedGraph(graph_size)

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


def euler_cycle(graph, initial_vertex=1):
    size = graph.getSize()
    matrix = graph.getAdjacencyMatrix()
    initial_vertex -= 1
    vertexes_numbers = graph.getVertexesList()
    print(vertexes_numbers)


    # if not graph.areAllVertexesEvenDegree():
    #     return

    answer = []

    fleury(0, matrix, graph, answer)
    fleury(1, matrix, graph, answer)
    fleury(3, matrix, graph, answer)
    fleury(3, matrix, graph, answer)
    fleury(4, matrix, graph, answer)


    print(answer)
    return

def fleury(current_vertex, matrix, graph, answer):

    print('current_vertex: ', current_vertex)

    vertexes_list = graph.getVertexesList()
    print('vertexes_list: ', vertexes_list)

    vertex_index = vertexes_list.index(current_vertex)
    print("vertex_index: ", vertex_index)

    vertex_connections = matrix[vertex_index]
    print('vertexes_connections: ', vertex_connections)

    vertex_degree = get_vertex_degree(vertex_index, vertex_connections)
    print("vertex_degree: ", vertex_degree)

    if is_loop(vertex_index, vertex_connections):
        answer.append([current_vertex, current_vertex])
        graph.removeEdge(vertex_index, vertex_index)
        print("Pętla")
        print_matrix(graph)

    elif vertex_degree == 1:
        for index, value in enumerate(vertex_connections):
            if value == 1:
                connection = index
                answer.append([current_vertex, connection])
        graph.removeVertex(current_vertex)

    else:
        for index, value in enumerate(vertex_connections):
            if value == 1:
                neighbour = index
                copy_graph = copy.deepcopy(graph)
                copy_graph.removeEdge(vertex_index, neighbour)
                print("Usuwanie ", current_vertex, neighbour)
                if is_connected(copy_graph):
                    answer.append([current_vertex, neighbour])
                    graph.removeEdge(vertex_index, neighbour)
                    break

    return answer


def get_vertex_degree(vertex, connections):
    degree = 0
    for index, elem in enumerate(connections):
        if elem == 1:
            if index == vertex:
                degree += 2
            else:
                degree += 1
    return degree


def is_loop(vertex, connections):
    for index, elem in enumerate(connections):
        if index == vertex and elem == 1:
            return True
    return False


def print_matrix(graph):
    matrix = graph.getAdjacencyMatrix()
    print("\nMacierz sąsiedztwa:\n")
    for index, row in enumerate(matrix):
        print(index, end=': ')
        for value in row:
            print('{0:5}'.format(value), end=' ')
        print()
    return
