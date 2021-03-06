import pandas
import numpy


class Graph(object):
    def __init__(self, size):
        self.size = size
        self.adjMatrix = [[0 for i in range(size)] for i in range(size)]

    def buildFromMatrix(self, matrix):
        self.adjMatrix = matrix
        if not self.isSimpleGraph:
            print("Podany graf nie jest grafem prostym")
            return
        elif not self.isSymetric:
            print("Podany graf nie jest grafem nieskierowanym")
            return
        return self

    def isSimpleGraph(self):
        for i in range(self.size):
            vertex_edges = 0
            vertex_row = self.adjMatrix[i]
            for j in range(self.size):
                if vertex_row[j] == 1:
                    if i == j:
                        return False
                    vertex_edges = vertex_edges + 1
            if vertex_edges == 0:
                return False
        return True

    def isSymetric(self):
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    continue
                elif self.adjMatrix[i][j] != self.adjMatrix[j][i]:
                    return False
        return True

    def addEdge(self, v1, v2):
        if self.isVertexInvalid(v1) or self.isVertexInvalid(v2):
            return
        if self.doesEdgeExist(v1, v2):
            print("Podana krawędź już istnieje")
            return
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        return self.getAdjacencyMatrix()

    def removeEdge(self, v1, v2):
        if self.isVertexInvalid(v1) or self.isVertexInvalid(v2):
            return
        if not self.doesEdgeExist(v1, v2):
            print("Podana krawędź nie istnieje")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        return self.getAdjacencyMatrix()

    def addVertex(self):
        self.size += 1
        for row in self.adjMatrix:
            row.append(0)
        self.adjMatrix.append([0 for i in range(self.size)])
        return self.getAdjacencyMatrix()

    def removeVertex(self, v):
        if self.isVertexInvalid(v):
            return
        self.removeEdgesAssociatedToVertex(v)
        self.removeRowFromMatrix(v)
        self.removeColumnFromMatrix(v)
        self.size -= 1
        return self.getAdjacencyMatrix()

    def removeEdgesAssociatedToVertex(self, v):
        for index in range(self.size):
            if self.adjMatrix[v][index] == 1:
                self.removeEdge(v, index)

    def removeRowFromMatrix(self, rowNum):
        del self.adjMatrix[rowNum]

    def removeColumnFromMatrix(self, colNum):
        for row in self.adjMatrix:
            del row[colNum]

    def findVertexDegree(self, v):
        degree = 0
        for index in range(self.size):
            if self.doesEdgeExist(v, index):
                if index == v:
                    degree += 2
                else:
                    degree += 1
        return degree

    def findMinGraphDegree(self):
        vertexDegree = self.findVertexDegree(0)
        if vertexDegree == 0:
            print("Minimalny stopień grafu: %d" % vertexDegree)
            return vertexDegree
        else:
            for vertexNum in range(1, self.size):
                currentVertexDegree = self.findVertexDegree(vertexNum)
                if currentVertexDegree == 0:
                    print("Minimalny stopień grafu: %d" % vertexDegree)
                    return vertexDegree
                elif currentVertexDegree < vertexDegree:
                    vertexDegree = currentVertexDegree
        print("Minimalny stopień grafu: %d" % vertexDegree)
        return vertexDegree
    
    def findMaxGraphDegree(self):
        vertexDegree = self.findVertexDegree(0)
        for vertexNum in range(1, self.size):
            currentVertexDegree = self.findVertexDegree(vertexNum)
            if currentVertexDegree > vertexDegree:
                vertexDegree = currentVertexDegree
        print("Maksymalny stopień grafu: %d" % vertexDegree)
        return vertexDegree

    def findOddAndEvenVertexDegreesAmount(self):
        degrees = dict(
            even=0,
            odd=0
        )
        all_degrees = self.getAllDegrees()
        for degree in all_degrees:
            if degree % 2 == 0:
                degrees['even'] += 1
            else:
                degrees['odd'] += 1
        print("Wierzchołki parzystego stopnia: %d, nieparzystego: %d" % (degrees['even'], degrees['odd']))
        return degrees

    def getAllDegrees(self):
        degrees = []
        for vertexNum in range(self.size):
            vertexDegree = self.findVertexDegree(vertexNum)
            degrees.append(vertexDegree)
        degrees.sort(reverse=True)
        return degrees

    def printAllDegrees(self):
        all_degrees = self.getAllDegrees()
        print("Stopnie: ", all_degrees)

    def getAllDegreesWithIndexes(self):
        degrees_indexes = {}
        for vertexNum in range(self.size):
            vertexDegree = self.findVertexDegree(vertexNum)
            degrees_indexes[vertexNum] = vertexDegree
        return degrees_indexes

    def getLastVertexIndex(self):
        return self.size - 1

    def getAdjacencyMatrix(self):
        return self.adjMatrix

    def isVertexInvalid(self, v):
        if not isinstance(v, int):
            print("Numery wierzchołków to liczby całkowite")
            return True
        if v < 0 or v >= self.size:
            print("Podany wierzchołek %d nie istnieje. Numery wierzchołków są w zakresie 0 - %d" % (v, self.size - 1))
            return True
        return False

    def doesEdgeExist(self, v1, v2):
        if self.adjMatrix[v1][v2] == 1:
            return True
        return False

    def toString(self):
        print("\n\nMacierz sąsiedztwa:\n")
        for row in self.adjMatrix:
            for value in row:
                print('{0:5}'.format(value), end=' ')
            print()
        print("Rozmiar macierzy: [ %d x %d ]\n" % (len(self.adjMatrix), len(self.adjMatrix[0])))
        return

    # saves adjacency matrix to csv file
    def writeToCsv(self):
        dfStringList = []
        for row in self.adjMatrix:
            dfStringList.append(', '.join(map(str, row)))
        dfString = '; '.join(map(str, dfStringList))
        numpyMatrix = numpy.matrix(dfString)
        dataframe = pandas.DataFrame(numpyMatrix)
        print(dataframe)
        dataframe.to_csv('./graph.csv')