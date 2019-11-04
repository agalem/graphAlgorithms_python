from classes.graph import Graph
from cycleProcedures import *


def main():
    g = buildGraphFromFile('input.txt')
    g.toString()

    searchCycle(g.getAdjacencyMatrix())
    #findJordanCenter(g.getAdjacencyMatrix())



if __name__ == '__main__':
    main()