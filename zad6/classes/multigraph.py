class Multigraph:
    def __init__(self, size):
        self.size = size
        self.adj_list = [[] for i in range(size)]
        self.vertexes_numbers = [i for i in range(size)]
        self.last_vertex_removed = 0

    def add_edge(self, v1, v2):
        if self.is_vertex_invalid(v1) or self.is_vertex_invalid(v2):
            return
        if v1 == v2:
            self.adj_list[v1].append(v2)
        else:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
        return

    def remove_edge(self, v1, v2):
        if self.is_vertex_invalid(v1) or self.is_vertex_invalid(v2):
            return
        if not self.does_edge_exist(v1, v2):
            print("Podana krawędź nie istnieje")
            return
        if v1 == v2:
            self.adj_list[v1].remove(v2)
        else:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
        return

    def remove_one_edge(self, v1, v2):
        if self.is_vertex_invalid(v1) or self.is_vertex_invalid(v2):
            return
        if not self.does_edge_exist(v1, v2):
            print("Podana krawędź nie istnieje ", v1, v2)
            return
        self.adj_list[v1].remove(v2)
        return

    def add_vertex(self):
        self.size += 1
        self.adj_list.append([])
        if self.last_vertex_removed >= self.size:
            self.vertexes_numbers.append(self.last_vertex_removed + 1)
        else:
            self.vertexes_numbers.append(self.size)
        return

    def remove_vertex(self, v):
        print("Przekazany wierzchołek: ", v)
        vertex_index = self.vertexes_numbers.index(v)
        if self.is_vertex_invalid(v):
            return
        if not self.does_vertex_exist(vertex_index):
            return
        self.remove_edges_associated_to_vertex(vertex_index)
        del self.adj_list[vertex_index]
        self.vertexes_numbers.remove(v)
        self.last_vertex_removed = v
        return

    def remove_edges_associated_to_vertex(self, v):
        for value in list(self.adj_list[v]):
            self.remove_one_edge(self.vertexes_numbers.index(value), v)

    def all_vertexes_even_degree(self):
        for i in range(self.size):
            vertex_degree = self.find_vertex_degree(i)
            if vertex_degree % 2 != 0:
                print("Wierzchołek ", i + 1, " nie jest parzystego stopnia. Połączenia: ")
                for value in self.adj_list[i]:
                    print('{0:5}'.format(value + 1), end=' ')
                return False
        return True

    def find_vertex_degree(self, v):
        degree = 0
        for vertex in  self.adj_list[v]:
            if vertex == v:
                degree += 2
            else:
                degree += 1
        return degree

    def does_vertex_exist(self, v):
        if 0 <= v < self.get_size():
            return True
        print("Podany wierzchołek nie istnieje")
        return False

    def does_edge_exist(self, v1, v2):
        # print("v1: ", v1,", v2:  ", v2, " Lista: ", self.adj_list[v1])
        if v2 in self.adj_list[v1]:
            return True
        return False

    def is_vertex_invalid(self, v):
        if not isinstance(v, int):
            print("Numery wierzchołków to liczby całkowite")
            return True
        if v < 0 or v >= self.size:
            print("Podany wierzchołek %d nie istnieje. Numery wierzchołków są w zakresie 0 - %d" % (v, self.size - 1))
            return True
        return False


    def get_size(self):
        return self.size

    def get_adjacency_list(self):
        return self.adj_list

    def get_vertexes_list(self):
        return self.vertexes_numbers

    def toString(self):
        print("\n\nLista sąsiedztwa:\n")
        for index, row in enumerate(self.adj_list):
            print(self.vertexes_numbers[index] + 1, end=': ')
            for value in row:
                print('{0:5}'.format(value + 1), end=' ')
            print()
        return
