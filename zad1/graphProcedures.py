def findC3Cycles(adjMatrix):
    size = len(adjMatrix)
    visitedMatrix = [[0 for i in range(size)] for i in range(size)]
    cycles = 0
    for rowNum in range(size):
        for columnNum in range(size):
            if rowNum == columnNum:
                continue
            elif adjMatrix[rowNum][columnNum] == 1 and visitedMatrix[rowNum][columnNum] == 0:
                cyclePath = checkIfCycle(adjMatrix, rowNum, columnNum)
                if len(cyclePath) == 3:
                    cycles += 1
                    visitedMatrix = modifyVisitedMatrix(visitedMatrix, cyclePath)
    print("Cykle: ", cycles)
    return

def hasC3Cycle(adjMatrix):
    size = len(adjMatrix)
    for rowNum in range(size):
        for colmnNum in range(size):
            if rowNum == colmnNum:
                continue
            elif adjMatrix[rowNum][colmnNum] == 1:
                cyclePath = checkIfCycle(adjMatrix, rowNum, colmnNum)
                if len(cyclePath) == 3:
                    print("Zawiera podgraf izomorficzny do cyklu C3")
                    return True
    print("Nie zawiera podgrafu izomorficznego do cyklu C3")
    return False

def isGraphSeries(series):
    initialSum = sumListElements(series)
    if not isEven(initialSum):
        print("Nie jest ciągiem grafowym")
        return False
    return checkGraphSeries(series)

def checkGraphSeries(series):



def isEven(num):
    if num % 2 == 0:
        return True
    return False


def sumListElements(list):
    size = len(list)
    sum = 0
    for i in range(size):
        sum += int(list[i])
    return sum

def sumListElementsMinusOne(list):
    size = len(list)
    sum = 0
    for i in range(size):
        if int(list[i]) == 0:
            continue
        else:
            sum += int(list[i] - 1)
    return sum

def hasC3CycleByMatrixMultipication(adjMatrix):
    resultMatrix = multiplyMatrixes(multiplyMatrixes(adjMatrix, adjMatrix), adjMatrix)
    size = len(resultMatrix)
    for i in range(size):
        if resultMatrix[i][i] > 0:
            print("Zawiera podgraf izomorficzny do cyklu C3")
            return True
    print("Nie zawiera podgrafu izomorficznego do cyklu C3")
    return False

def findc3CyclesByMultiplication(adjMatrix):
    resultMatrix = multiplyMatrixes(adjMatrix, adjMatrix)
    resultMatrixThree = multiplyMatrixes(resultMatrix, adjMatrix)
    size = len(resultMatrixThree)
    repetitiveCyclesSum = 0
    for i in range(size):
        repetitiveCyclesSum += resultMatrixThree[i][i] / 2
    result = repetitiveCyclesSum / 3.0
    print("Cykle z mnożenia macierzy: ", int(result))
    print("\n\nMacierz sąsiedztwa:\n")
    for row in resultMatrixThree:
        for value in row:
            print('{0:5}'.format(value), end=' ')
        print()
    print("Rozmiar macierzy: [ %d x %d ]\n" % (len(resultMatrixThree), len(resultMatrixThree[0])))
    return

def checkIfCycle(adjMatrix, firstVertex, secondVertex):
    visited = [firstVertex, secondVertex]
    size = len(adjMatrix)
    for index in range(size):
        if index == firstVertex or index == secondVertex:
            continue
        elif adjMatrix[secondVertex][index] == 1:
            if adjMatrix[index][firstVertex] == 1:
                visited.append(index)
                print('Visited :', visited)
                return visited
    return visited

def modifyVisitedMatrix(visitedMatrix, cyclePath):
    #size = 3
    #for i in range(size):
    #    for j in range(size):
    #       if i == j:
    #           continue
    #       else:
    #           visitedMatrix[cyclePath[i]][cyclePath[j]] = 1
    visitedMatrix[cyclePath[0]][cyclePath[1]] = 1
    visitedMatrix[cyclePath[1]][cyclePath[0]] = 1
    visitedMatrix[cyclePath[1]][cyclePath[2]] = 1
    visitedMatrix[cyclePath[2]][cyclePath[1]] = 1
    visitedMatrix[cyclePath[2]][cyclePath[0]] = 1
    visitedMatrix[cyclePath[0]][cyclePath[2]] = 1
    return visitedMatrix

def multiplyMatrixes(mat1, mat2):
    zip_mat2 = zip(*mat2)
    zip_mat2 = list(zip_mat2)
    return [[sum(elem_a*elem_b for elem_a, elem_b in zip(row_a, col_b))
             for col_b in zip_mat2] for row_a in mat1]