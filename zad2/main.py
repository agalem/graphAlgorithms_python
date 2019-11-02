from classes.graph import Graph
from cycleProcedures import *


def main():
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 5)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(3, 1)
    g.addEdge(5, 1)
    g.toString()

    searchCycle(g.getAdjacencyMatrix())


if __name__ == '__main__':
    main()