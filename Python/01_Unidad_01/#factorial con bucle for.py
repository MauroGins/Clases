#factorial con bucle for

n=int(input("dame numero"))
factorial = 1
for i in range(1,n+1):  # mientras i sea menor que 1 (i=1, i<n+1,i++)
    factorial = factorial * i 
    print("--------------")
    print(factorial)
