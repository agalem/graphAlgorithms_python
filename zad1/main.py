from classes.graph import Graph
from graphProcedures import *

def main():
    g = Graph(9)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(0, 3)
    g.addEdge(0, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(6, 7)
    g.addEdge(6, 8)
    g.addEdge(7, 8)
    g.toString()
    g.printAllDegrees()
    g.findMinGraphDegree()
    g.findMaxGraphDegree()
    g.findOddAndEvenVertexDegreesAmount()

    findC3Cycles(g.getAdjacencyMatrix())
    findc3CyclesByMultiplication(g.getAdjacencyMatrix())
    hasC3Cycle(g.getAdjacencyMatrix())
    hasC3CycleByMatrixMultipication(g.getAdjacencyMatrix())
    isGraphSeries([6, 5, 4, 3, 2, 2, 2, 2])


if __name__ == '__main__':
    main()