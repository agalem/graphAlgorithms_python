from classes.graph import Graph
from graphProcedures import *

def main():
    g = buildGraphFromFile('input.txt')
    g.addVertex()
    g.removeVertex(3)
    g.toString()
    g.printAllDegrees()
    g.findMinGraphDegree()
    g.findMaxGraphDegree()
    g.findOddAndEvenVertexDegreesAmount()

    g.writeToCsv()

    hasC3Cycle(g.getAdjacencyMatrix())
    hasC3CycleByMatrixMultipication(g.getAdjacencyMatrix())
    isGraphSeries([4,4,4,4])


if __name__ == '__main__':
    main()