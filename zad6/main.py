from methods import *

def main():
    graph = build_graph_from_file("input.txt")
    is_connected(graph)
    euler_cycle(graph)

    return


if __name__ == '__main__':
    main()