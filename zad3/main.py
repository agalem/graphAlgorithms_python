from methods import *

def main():
    g = build_graph_from_file('input.txt')

    print("Drzewo spinające dfs")
    spanning_tree_dfs(g)

    print("Czy spójny")
    #is_connected(g)

    wg = build_weighted_graph_from_file('input4.txt')
    #wg.getEdgesByWeightsAsc()

    print("Kruskal")
    kruskal(wg)

    dg = build_directed_graph_from_file("input3.txt")

    print("Kosaraju")
    kosaraju(dg)


    djikstra_tree(wg, 1)

    return


if __name__ == '__main__':
    main()
