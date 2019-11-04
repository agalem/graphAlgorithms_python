from classes.graph import Graph
from graphProcedures import *

def main():
    g = buildGraphFromFile('input.txt')
    g.toString()
    g.printAllDegrees()
    g.findMinGraphDegree()
    g.findMaxGraphDegree()
    g.findOddAndEvenVertexDegreesAmount()

    g.writeToCsv()

    hasC3Cycle(g.getAdjacencyMatrix())
    hasC3CycleByMatrixMultipication(g.getAdjacencyMatrix())
    isGraphSeries([7, 6, 5, 4, 4, 3, 2, 1])


if __name__ == '__main__':
    main()