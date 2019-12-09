from methods import *

def main():
    graph = build_network_from_file('input3.txt')
    maximum_flow(graph)
    graph2 = build_network_from_file('input.txt')
    analyze_graph(graph2)

    return

if __name__ == '__main__':
    main()
