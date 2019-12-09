from classes.graph import Graph
from classes.stack import Stack
from classes.weightedGraph import WeightedGraph
from classes.directedGraph import DirectedGraph
from classes.weightedDigraph import WeightedDigraph

def build_directed_graph_from_file(path):
    file = open(path, "r")
    lines = [line.rstrip('\n') for line in file]
    file.close()

    graph_size = int(lines[0])
    edges_size = int(lines[1])
    edges = lines[2:]

    if len(edges) != edges_size:
        print("Podano niewłaściwą liczbę krawędzi - %d" % len(edges))
        return

    directed_graph = DirectedGraph(graph_size)

    for edge in edges:
        edge = edge.split()
        if len(edge) != 2:
            print("\n\nNie utworzono grafu skierowanego")
            print("Nieprawidłowa linijka: ", edge)
            return
        vertex_from = int(edge[0]) - 1
        vertex_to = int(edge[1]) - 1
        directed_graph.addEdge(vertex_from, vertex_to)

    directed_graph.toString()
    return directed_graph


def build_weighted_digraph_from_file(path):
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


def build_weighted_graph_from_file(path):
    file = open(path, "r")
    lines = [line.rstrip('\n') for line in file]
    file.close()

    graph_size = int(lines[0])
    edges_size = int(lines[1])
    edges = lines[2:]

    if len(edges) != edges_size:
        print("Podano niewłaściwą liczbę krawędzi - %d" % len(edges))
        return

    weighted_graph = WeightedGraph(graph_size)

    for edge in edges:
        edge = edge.split()
        if len(edge) != 3:
            print("\n\nNie utworzono grafu z wagami krawędzi")
            print("Nieprawidłowa linijka: ", edge)
            return
        vertex_from = int(edge[0]) - 1
        vertex_to = int(edge[1]) - 1
        vertex_weight = int(edge[2])
        weighted_graph.addEdge(vertex_from, vertex_to, vertex_weight)

    weighted_graph.toString()
    return weighted_graph


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


def spanning_tree(graph, starting_vertex=1):

    if graph.getType() != 'graph':
        print("Niewłaściwy graf")
        return

    if not is_connected(graph):
        print("Graf nie jest spójny")
        return

    size = graph.getSize()
    matrix = graph.getAdjacencyMatrix()

    visited = [False for i in range(size)]
    stack = Stack()
    tree_edges = []

    for i in range(size):
        print(matrix[i])

    tree_edges = dfs_spanning_tree(starting_vertex, matrix, stack, visited, tree_edges)
    print("\nDrzewo spinające DFS ", tree_edges)

    return


def dfs_spanning_tree(current_vertex, matrix, stack, visited, tree_edges):

    connections = matrix[current_vertex - 1]

    if not visited[current_vertex - 1]:
        visited[current_vertex - 1] = True
        stack.push(current_vertex)

    print("Stos: ", stack)
    print("Odwiedzone: ", visited)
    print("Krawędzie: ", tree_edges)

    #current_vertex - 1, bo indexy są od 0, a ja numeruję wierzchołki od 1

    for i in range(len(connections)):
        if i != current_vertex - 1 and connections[i] == 1 and not visited[i]:
            tree_edges.append([current_vertex, i + 1])
            return dfs_spanning_tree(i + 1, matrix, stack, visited, tree_edges)
    stack.pop()

    if stack.is_empty():
        print("\n\nOdwiedzone: ", visited)
        return tree_edges

    return dfs_spanning_tree(stack.last_element(), matrix, stack, visited, tree_edges)


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
        #print("Odwiedzenie ", current_vertex, ", odwiedzone: ", visited)
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


def kruskal(wgraph):

    if wgraph.getType() != 'weighted graph':
        print('Niewłaściwy graf, powinien być graf ważony')
        return

    if not is_connected(wgraph):
        print("Graf nie jest spójny")
        return

    edges_weighted_asc = wgraph.getEdgesByWeightsAsc()
    print("Krawędzie wagami rosnąco: ", edges_weighted_asc)
    size = wgraph.getSize()

    copy_edges_weighted_asc = [row[:] for row in edges_weighted_asc]
    vertexes_connections = [[i + 1] for i in range(size)]

    edges = []
    out_weight = 0

    while len(copy_edges_weighted_asc) >= 1:
        edge = copy_edges_weighted_asc.pop(0)
        vertex_from = edge[0]
        vertex_from_index = vertex_from - 1
        vertex_to = edge[1]
        vertex_to_index = vertex_to - 1
        weight = edge[2]

        if vertex_to in vertexes_connections[vertex_from_index]:
            print("Wierzchołki ", vertex_from, " i ", vertex_to, "po dodaniu utworzą cykl")
            continue

        if vertex_from in vertexes_connections[vertex_to_index]:
            print("Wierzchołki ", vertex_from, " i ", vertex_to, "po dodaniu utworzą cykl")
            continue

        tab_to = vertexes_connections[vertex_from_index]
        print("Tablica wierzchołków do przyłączenia: ", tab_to)
        for elem in tab_to:
            elem_index = elem - 1
            if vertex_to not in vertexes_connections[elem_index]:
                vertexes_connections[elem_index].append(vertex_to)
                vertexes_connections[vertex_to_index].append(elem)
                print("Dodaj ", vertex_to, " do ", elem, " i ", elem, " do ", vertex_to)

        tab_to = vertexes_connections[vertex_to_index]
        print("Tablica wierzchołków do przyłączenia: ", tab_to)
        for elem in tab_to:
            elem_index = elem - 1
            if vertex_from not in vertexes_connections[elem_index]:
                vertexes_connections[elem_index].append(vertex_from)
                vertexes_connections[vertex_from_index].append(elem)
                print("Dodaj ", vertex_from, " do ", elem, " i ", elem, " do ", vertex_from)

        edges.append([vertex_from, vertex_to])
        out_weight += weight

        if len(vertexes_connections[vertex_to_index]) == size or len(vertexes_connections[vertex_from_index]) == size:
            print("\nPołączenia :", vertexes_connections)
            print("\nDrzewo spinające: ", edges)
            print("Waga: ", out_weight)
            return

    print("\nPołączenia :", vertexes_connections)
    print("\nDrzewo spinające: ", edges)
    print("Waga: ", out_weight)

    return


def kosaraju(digraph):

    if digraph.getType() != "directed graph":
        print('Niewłaściwy graf, powinien być graf skierowany')
        return

    size = digraph.getSize()
    matrix = digraph.getAdjacencyMatrix()

    stack_dfs = Stack()
    visited = [False for i in range(size)]
    stack_post_order = Stack()
    components = []

    post_order = dfs_post_order(3, matrix, stack_dfs, stack_post_order, visited, size)
    print("Post order: ", post_order.get_items())

    transposition_matrix = digraph.getTransposition()
    visited_bool = [False for i in range(size)]

    while not post_order.is_empty():
        #usuń wierzchołek z post order
        vertex = post_order.pop()
        print("Vertex", vertex)
        #kontynuuj gdy już odwiedzony
        if visited_bool[vertex - 1]:
            continue
        else:
            #sprawdź do ilu wierzchołków można od niego dojść w grafie transponowanym
            visited = dfs_components(vertex, transposition_matrix, stack_dfs, [], visited_bool)
            print("Odwiedzone: ", visited)
            if len(visited) > 1:
                to_add = [vertex]
                for elem in reversed(post_order.get_items()):
                    if elem in visited:
                        post_order.remove(elem)
                        to_add.append(elem)
                components.append(to_add)
            else:
                components.append([vertex])

    print("Silnie składowe: ", components)

    return components


def dfs_post_order(current_vertex, matrix, stack_dfs, stack_post_order, visited, size):

    connections = matrix[current_vertex - 1]

    if not visited[current_vertex - 1]:
        visited[current_vertex - 1] = True
        stack_dfs.push(current_vertex)

    for i in range(len(connections)):
        if i != current_vertex - 1 and connections[i] == 1 and not visited[i]:
            return dfs_post_order(i + 1, matrix, stack_dfs, stack_post_order, visited, size)
    if not stack_dfs.is_empty():
        stack_post_order.push(stack_dfs.pop())

    if stack_dfs.is_empty():
        if current_vertex > 1:
            return dfs_post_order(current_vertex - 1, matrix, stack_dfs, stack_post_order, visited, size)

        return stack_post_order

    return dfs_post_order(stack_dfs.last_element(), matrix, stack_dfs, stack_post_order, visited, size)


def djikstra_tree(digraph, starting_vertex=1):

    if not is_connected(digraph):
        print("Graf nie jest spojny")
        return

    size = digraph.getSize()
    matrix = digraph.getAdjacencyMatrix()

    if digraph.getType() != 'weighted digraph':
        print('Niewłaściwy graf, powinien być graf skierowany')
        return

    if has_negative_weights(matrix):
        print("Graf zawiera ujemne funkcje wagowe")
        return


    vertexes = [i + 1 for i in range(size)]
    tree = []

    distances = [[float("inf") for i in range(len(matrix))]]
    distances[0][starting_vertex - 1] = 0

    print(distances)
    print(vertexes)

    djikstra(vertexes, distances, matrix, tree)

    print("Drzewo najkrotszych sciezek: ", tree)
    return tree


def djikstra(vertexes, distances, matrix, tree):

    while len(vertexes) > 0:

        if len(distances) > 0:
            distances.append(list(distances[-1]))

        min_distance = float("inf")

        #znajdz wierzcholek o najmniejszej wartosci z tablicy odleglosci
        for vertex in vertexes:
            if distances[-1][vertex - 1] < min_distance:
                min_distance = distances[-1][vertex - 1]
                min_distance_vertex = vertex

        if min_distance_vertex not in vertexes:
            return tree

        #usun znaleziony wierzcholek z tablicy wierzcholkow nieodwiedzonych
        vertexes.remove(min_distance_vertex)

        for vertex in vertexes:
            #gdy odleglosc nie jest policzona(nieskonczonosc) i istnieje polaczenie pomiędzy wierzcholkiem o najmniejszej wartosci a sprawdzanym
            if distances[-1][vertex - 1] == float("inf") and matrix[min_distance_vertex - 1][vertex - 1] != 0:
                #odleglosc do wierzcholka o najmniejszej wartości jest już policzona
                if distances[-1][min_distance_vertex - 1] != float("inf"):
                    distances[-1][vertex - 1] = distances[-1][min_distance_vertex - 1] + matrix[min_distance_vertex - 1][vertex - 1]
                else:
                    distances[-1][vertex - 1] = matrix[min_distance_vertex - 1][vertex - 1]

                tree.append([min_distance_vertex, vertex])

            else:
                #istnieje polaczenie pomiędzy wierzcholkiem o najmniejszej wartosci a sprawdzanym
                if matrix[min_distance_vertex - 1][vertex - 1] != 0:
                    current_distance = distances[-1][vertex - 1]
                    new_distance = distances[-1][min_distance_vertex - 1] + matrix[min_distance_vertex - 1][vertex - 1]

                    #usuniecie zbednej krawedzi z drzewa odleglosci
                    #krawedz do usuniecia -> gdy istnieje krawędz prowadzaca do sprawdzanego wierzcholka (vertex) już dodana do drzewa
                    if current_distance > new_distance:
                        previous_edges_second_elements = [edge[1] for edge in tree]
                        if vertex in previous_edges_second_elements:
                            index = previous_edges_second_elements.index(vertex)
                            tree.pop(index)

                        tree.append([min_distance_vertex, vertex])

                    distances[-1][vertex - 1] = min(current_distance, new_distance)


    print("Odległości: ")
    for row in distances:
        print(row)

    return tree


def has_negative_weights(matrix):
    for row in matrix:
        for elem in row:
            if elem < 0:
                return True
    return False