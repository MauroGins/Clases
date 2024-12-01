"""

*             *         0   13    0  
 *           *          1   11    -1      
  *         *           2   9     -2
   *       *            3   7     -3
    *     *             4   5       -4
     *   *              5   3       -5
      * *               6   1       -6   0  0 1 0
       *                7   0       -7   1  1 0 1



"""
altura=1
altura = int(input("altura minima 2"))

espacio=" "
asterisco ="*"

if not altura < 2 :
        
    for fila in range(altura+1):
        linea=""
        ancho = altura *2
        
        for col in range(ancho+1):
            if fila==col or col == ancho-fila:
                linea+=asterisco
            else:
                linea += espacio
            
        linea += "\n"
        print(linea , end="")

