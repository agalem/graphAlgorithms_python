from methods import *


def main():
    graph = build_graph_from_file("input4.txt")
    find_max_match(graph)

    return


if __name__ == '__main__':
    main()