class WeightedDigraph:
    def __init__(self, size):
        self.size = size
        self.adjMatrix = [[0 for i in range(size)] for i in range(size)]
        self.vertexes_left = []
        self.vertexes_right = []

    def add_vertexes_left(self, vertexes_list):
        self.vertexes_left = vertexes_list
        return

    def add_vertexes_right(self, vertexes_list):
        self.vertexes_right = vertexes_list
        return

    def get_vertexes_left(self):
        return self.vertexes_left

    def get_vertexes_right(self):
        return self.vertexes_right

    def buildFromMatrix(self, matrix):
        self.adjMatrix = matrix
        return self

    def addEdge(self, v1, v2, weight):
        if self.isVertexInvalid(v1) or self.isVertexInvalid(v2):
            return
        if self.doesEdgeExist(v1, v2):
            print("Podana krawędź już istnieje")
            return
        self.adjMatrix[v1][v2] = weight
        return self.getAdjacencyMatrix()

    def removeEdge(self, v1, v2):
        if self.isVertexInvalid(v1) or self.isVertexInvalid(v2):
            return
        if not self.doesEdgeExist(v1, v2):
            print("Podana krawędź nie istnieje")
            return
        self.adjMatrix[v1][v2] = 0
        return self.getAdjacencyMatrix()

    def getEdgesByWeightsAsc(self):
        matrix_copy = [row[:] for row in self.adjMatrix]
        edgesList = []

        for i in range(self.size):
            vertex_connections = matrix_copy[i]
            for j in range(self.size):
                weight = vertex_connections[j]
                if weight != 0:
                    edgesList.append([i + 1, j + 1, weight])
                    matrix_copy[i][j] = 0
                    matrix_copy[j][i] = 0

        sorted_edgesList = sorted(edgesList, key=lambda x: x[2])

        return sorted_edgesList

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
            if self.adjMatrix[v][index] != 0:
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

    def getAdjacencyMatrix(self):
        return self.adjMatrix

    def getSize(self):
        return self.size

    def getType(self):
        return "weighted digraph"

    def isVertexInvalid(self, v):
        if not isinstance(v, int):
            print("Numery wierzchołków to liczby całkowite")
            return True
        if v < 0 or v >= self.size:
            print("Podany wierzchołek %d nie istnieje. Numery wierzchołków są w zakresie 0 - %d" % (v, self.size - 1))
            return True
        return False

    def doesEdgeExist(self, v1, v2):
        if self.adjMatrix[v1][v2] != 0:
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
