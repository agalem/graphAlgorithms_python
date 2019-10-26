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
    size = 3
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            else:
                visitedMatrix[cyclePath[i]][cyclePath[j]] = 1
    return visitedMatrix