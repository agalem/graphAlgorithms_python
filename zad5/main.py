from methods import *


def main():
    graph = build_bipartite_graph_from_file("input3.txt")
    max_match(graph)

    return


if __name__ == '__main__':
    main()