class WeightedGraph:
    def __init__(self, size):
        self.size = size
        self.adjMatrix = [[0 for i in range(size)] for i in range(size)]
        self.vertexes_nums = [i for i in range(size)]

    def buildFromMatrix(self, matrix):
        self.adjMatrix = matrix
        return self

    def addEdge(self, v1, v2):
        if self.isVertexInvalid(v1) or self.isVertexInvalid(v2):
            return
        if self.doesEdgeExist(v1, v2):
            print("Podana krawędź już istnieje")
            return
        if v1 == v2:
            self.adjMatrix[v1][v2] = 1
            return
        self.adjMatrix[v1][v2] += 1
        self.adjMatrix[v2][v1] += 1
        return

    def removeEdge(self, v1, v2):
        if self.isVertexInvalid(v1) or self.isVertexInvalid(v2):
            return
        if not self.doesEdgeExist(v1, v2):
            print("Podana krawędź nie istnieje")
            return
        if v1 == v2:
            self.adjMatrix[v1][v2] = 0
            return
        self.adjMatrix[v1][v2] -= 1
        self.adjMatrix[v2][v1] -= 1
        return

    def addVertex(self):
        self.size += 1
        for row in self.adjMatrix:
            row.append(0)
        self.adjMatrix.append([0 for i in range(self.size)])
        self.vertexes_nums.append(self.vertexes_nums[-1] + 1)
        return

    def removeVertex(self, v):
        if self.isVertexInvalid(v):
            return
        # self.removeEdgesAssociatedToVertex(v)
        # self.removeRowFromMatrix(v)
        # self.removeColumnFromMatrix(v)
        # self.size -= 1
        # self.vertexes_nums.remove(v)
        vertex_index = self.vertexes_nums.index(v)
        self.removeEdgesAssociatedToVertex(vertex_index)
        self.removeRowFromMatrix(vertex_index)
        self.removeColumnFromMatrix(vertex_index)
        self.size -= 1
        self.vertexes_nums.remove(v)
        return

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

    def areAllVertexesEvenDegree(self):
        for vertex in range(self.size):
            degree = self.findVertexDegree(vertex)
            if degree % 2 != 0:
                return False
        return True

    def getAdjacencyMatrix(self):
        return self.adjMatrix

    def getSize(self):
        return self.size

    def getVertexesList(self):
        return self.vertexes_nums

    def getType(self):
        return "weighted graph"

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
