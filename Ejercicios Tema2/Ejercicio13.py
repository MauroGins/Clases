from Ejercicio14 import printAsMatrix

def matricesDimension(matrizA,matrizB) -> bool:
    if len(matrizA) != len(matrizB):
        return False
    for i in range(len(matrizA)):
        if len(matrizA[i]) != len(matrizB[i]):
            return False
    return True

def sumaMatrices(matrizA,matrizB) -> list:
    """
    Esta función suma dos matrices de igual tamaño y devuelve la matriz resultante.
    """
    if (matrizA) !=  (matrizB) or len(matrizA[0]) != len(matrizB[0]): # Se puede usar esto y no tener que definir matrizDimension o coger la siguiente linea
    # necesitando el def matricesDimension
        
#if not matricesDimension(matrizA,matrizB):
#       return None
        
        matrizSuma = []
        for i in range(len(matrizA)):
            fila=[]
            for j in range(len(matrizA[i])):
                fila.append(matrizA[i][j]+matrizB[i][j])
            matrizSuma.append(fila)
        return matrizSuma


if __name__=="__main__":
    matrizEjA = [[1, 2, 3], [4, 5, 6], [7 ,8 ,9]]
    matrizEjB = [[9, 8, 7], [6, 5, 4], [3 ,2 ,1]]
    print(sumaMatrices(matrizEjA,matrizEjB)) # [[10, 10, 10], [10, 10, 10], [10, 10, 10]]