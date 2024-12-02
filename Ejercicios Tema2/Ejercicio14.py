def printAsMatrix(matrix):
    for row in matrix:
        for element in row:
            print(row, end="\t")
        print()
        
        
def printAsMatrixRangeVersion(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()        
        
if __name__ == "__main__":
    matrizEjA = [[1, 2, 3], [4, 5, 6], [7 ,8 ,9]]
    matrizEjB = [[9, 8, 7], [6, 5, 4], [3 ,2 ,1]]
    printAsMatrix(matrizEjA)
    printAsMatrixRangeVersion(matrizEjB)