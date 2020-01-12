import networkx as nx
import matplotlib.pyplot as plt

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


    nodes = [i + 1 for i in range(graph_size)]
    print(nodes)

    G = nx.Graph()
    G.add_nodes_from(nodes)

    for edge in edges:
        edge = edge.split()
        if len(edge) != 2:
            print("\n\nNie utworzono grafu")
            print("Nieprawidłowa linijka: ", edge)
            return
        vertex_from = int(edge[0])
        vertex_to = int(edge[1])
        G.add_edge(vertex_from, vertex_to)

    print(list(G.edges))

    return G

def check_planarity(graph):

    checking_output = nx.algorithms.planarity.check_planarity(graph)
    is_planar = checking_output[0]

    if is_planar:
        pos = nx.planar_layout(graph)

        nx.draw(graph, pos=pos, with_labels=True)
        plt.show()
    else:
        print("Graf nie jest planarny")
        return False

    return True