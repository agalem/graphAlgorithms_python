
# def djikstra2(current_vertex, value_to_add, matrix, tree, distances, vertexes, starting_vertex):
#
#     if current_vertex not in vertexes:
#         print("Wierzchołek jest już sprawdzony")
#         return
#
#     if len(distances) >= 1:
#         distances.append(list(distances[-1]))
#
#     vertexes.remove(current_vertex)
#
#     connections = matrix[current_vertex - 1]
#     min_distance = float("inf")
#     min_distance_vertex = 0
#
#     for i in range(len(connections)):
#         if i == current_vertex - 1 or i == starting_vertex - 1:
#             continue
#         if connections[i] != 0:
#             current_distance = distances[-1][i]
#             distance_to_vertex = connections[i] + value_to_add
#
#             # update wierzchołka jeżeli dana trasa jest krotsza i dodanie krawędzi do drzewa (oraz usunięcie wcześniejszej)
#             if current_distance > distance_to_vertex:
#                 distances[-1][i] = distance_to_vertex
#
#                 previous_edges_second_elements = [edge[1] for edge in tree]
#
#                 if i + 1 in previous_edges_second_elements:
#                     index = previous_edges_second_elements.index(i + 1)
#                     tree.pop(index)
#
#                 tree.append([current_vertex, i + 1])
#
#                 print("Vertex from ", current_vertex, " Vertex to: ", i+1, " Current, ", current_distance, ", new distance: ", distance_to_vertex)
#
#     # wybierz wierzchołek o najmniejszej odległości
#     for elem in vertexes:
#         if distances[-1][elem - 1] < min_distance:
#             min_distance = distances[-1][elem - 1]
#             min_distance_vertex = elem
#
#     if len(vertexes) > 0:
#         return djikstra(min_distance_vertex, min_distance, matrix, tree, distances, vertexes, starting_vertex)
#
#     print(vertexes)
#     print(distances)
#     print(tree)
#
#     return distances
