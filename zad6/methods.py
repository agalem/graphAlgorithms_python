import copy
from classes.stack import Stack
from classes.multigraph import Multigraph

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

    graph = Multigraph(graph_size)

    for edge in edges:
        edge = edge.split()
        if len(edge) != 2:
            print("\n\nNie utworzono grafu")
            print("Nieprawidłowa linijka: ", edge)
            return
        vertex_from = int(edge[0]) - 1
        vertex_to = int(edge[1]) - 1
        graph.add_edge(vertex_from, vertex_to)

    graph.toString()
    return graph


def is_connected(graph):
    adj_list = graph.get_adjacency_list()
    size = len(adj_list)

    stack = Stack()
    visited_bool = [False for i in range(size)]
    components = []
    components_amount = 0

    for vertex in range(size):
        if visited_bool[vertex]:
            continue
        else:
            visited = []
            visited = dfs_components(vertex + 1, adj_list, stack, visited, visited_bool)
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


def dfs_components(current_vertex, adj_list, stack, visited, visited_bool):
    connections = adj_list[current_vertex - 1]

    if not visited_bool[current_vertex - 1]:
        # print("Odwiedzenie ", current_vertex, ", odwiedzone: ", visited)
        visited_bool[current_vertex - 1] = True
        visited.append(current_vertex)
        stack.push(current_vertex)

    for i in connections:
        if i != current_vertex - 1 and not visited_bool[i]:
            return dfs_components(i + 1, adj_list, stack, visited, visited_bool)
    stack.pop()

    if stack.is_empty():
        return visited

    return dfs_components(stack.last_element(), adj_list, stack, visited, visited_bool)


def euler_cycle(graph, initial_vertex=1):
    size = graph.get_size()
    adj_list = graph.get_adjacency_list()
    initial_vertex -= 1

    if not graph.all_vertexes_even_degree():
        return

    print("Wszystkie wierzchołki są parzystego stopnia")

    copy_adjList = [x[:] for x in adj_list]
    copy_graph = copy.copy(graph)
    print_list(copy_graph)
    answer = []
    fleury(initial_vertex, copy_graph, answer)

    return


def fleury(current_vertex, graph, answer):
    adj_list = graph.get_adjacency_list()
    connections = adj_list[current_vertex]
    vertex_degree = get_vertex_degree(current_vertex, connections)
    print(vertex_degree)

    print("Aktualny wierzchołek: ", current_vertex + 1)

    if vertex_degree > 0:
        # dodanie pętli do odpowiedzi i usunięcie z
        if is_loop(current_vertex, connections):
            answer.append([current_vertex + 1, current_vertex + 1])
            graph.remove_edge(current_vertex, current_vertex)
            return fleury(current_vertex, graph, answer)

        elif get_vertex_degree(current_vertex, connections) == 1:
            connection = connections[0]
            answer.append([current_vertex + 1, connection + 1])
            print('current_vertex: ',current_vertex)
            graph.remove_vertex(current_vertex)
            # TODO błąd w tym miejscu
            return fleury(connection, graph, answer)

        else:
            for value in connections:
                print("Current ", current_vertex)

                new_graph_copy = copy.copy(graph)
                new_graph_copy.remove_edge(current_vertex, value)

                if is_connected(new_graph_copy):
                    answer.append([current_vertex + 1, value + 1])
                    graph.remove_edge(current_vertex, value)
                    print_list(graph)
                    return fleury(value, graph, answer)
        return

    print(answer)
    return answer


def get_vertex_degree(vertex, connections):
    degree = 0
    for value in connections:
        if value == vertex:
            degree += 2
        else:
            degree += 1
    return degree


def is_loop(vertex, connections):
    for value in connections:
        if value == vertex:
            return True
    return False


def print_list(graph):
    adj_list = graph.get_adjacency_list()
    vertexes_nums = graph.get_vertexes_list()

    print("\n\nLista sąsiedztwa:\n")
    for index, row in enumerate(adj_list):
        print(vertexes_nums[index] + 1, end=': ')
        for value in row:
            print('{0:5}'.format(value + 1), end=' ')
        print()
    return
