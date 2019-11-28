from methods import *

def main():
    g = build_graph_from_file('input.txt')

    spanning_tree_dfs(g)
    is_connected(g)

    wg = build_weighted_graph_from_file('input2.txt')
    wg.getEdgesByWeightsAsc()
    kruskal(wg)

    dg = build_directed_graph_from_file("input3.txt")
    kosaraju(dg)

    return


if __name__ == '__main__':
    main()
