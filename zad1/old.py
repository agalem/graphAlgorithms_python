def findc3CyclesByMultiplication(adjMatrix):
    resultMatrix = multiplyMatrixes(adjMatrix, adjMatrix)
    resultMatrixThree = multiplyMatrixes(resultMatrix, adjMatrix)
    size = len(resultMatrixThree)
    repetitiveCyclesSum = 0
    for i in range(size):
        repetitiveCyclesSum += resultMatrixThree[i][i] / 2
    result = repetitiveCyclesSum / 3.0
    print("Cykle z mnożenia macierzy: ", int(result))
    print("\n\nMacierz po mnożeniu dla cykli C3:\n")
    for row in resultMatrixThree:
        for value in row:
            print('{0:5}'.format(value), end=' ')
        print()
    print("Rozmiar macierzy: [ %d x %d ]\n" % (len(resultMatrixThree), len(resultMatrixThree[0])))
    return

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


def modifyVisitedMatrix(visitedMatrix, cyclePath):
    size = 3
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            else:
                visitedMatrix[cyclePath[i]][cyclePath[j]] = 1

    '''visitedMatrix[cyclePath[0]][cyclePath[1]] = 1
    visitedMatrix[cyclePath[1]][cyclePath[0]] = 1
    visitedMatrix[cyclePath[1]][cyclePath[2]] = 1
    visitedMatrix[cyclePath[2]][cyclePath[1]] = 1
    visitedMatrix[cyclePath[2]][cyclePath[0]] = 1
    visitedMatrix[cyclePath[0]][cyclePath[2]] = 1'''

    return visitedMatrix