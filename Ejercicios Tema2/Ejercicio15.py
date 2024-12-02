# Multiplicación de matrices

# La multiplicación de matrices se puede realizar de dos maneras: multiplicación de matrices de la
# forma A * B y multiplicación de matrices de la forma B * A.

def matrixProduct(matrixA,matrixB) -> list:
    # Verificar si las matrices pueden ser multiplicadas
    if len(matrixA[0]) != len(matrixB):
        return None
    # Inicializar la matriz resultante con ceros
    matrixProduct = []
    for i in range(len(matrixA)):
        row = []
        for j in range(len(matrixB[0])):
            product = 0
            for k in range(len(matrixA[i])):
                product += matrixA[i][k] * matrixB[k][j]
            row.append(row)
        matrixProduct.append(row)
    return matrixProduct


if __name__=="__main__":
    matrizEjA = [[1, 2], [4, 5]]
    matrizEjB = [[9, 8], [6, 5]]
    print(matrixProduct(matrizEjA,matrizEjB))