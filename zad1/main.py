from classes.graph import Graph
from graphProcedures import *

def main():
    g = Graph(8)
    g.addEdge(0, 2)
    g.addEdge(0, 7)
    g.addEdge(7, 5)
    g.addEdge(5, 2)
    g.addEdge(2, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(2, 6)
    g.addEdge(4, 6)
    g.addEdge(5, 6)
    g.addEdge(1, 0)
    g.toString()
    g.getAllDegrees()
    g.findMinGraphDegree()
    g.findMaxGraphDegree()
    g.findOddAndEvenVertexDegreesAmount()

    findC3Cycles(g.getAdjacencyMatrix())

if __name__ == '__main__':
    main()