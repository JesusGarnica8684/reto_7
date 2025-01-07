# Diseñar una función que permita calcular una aproximación de la función seno alrededor 
# de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. 
# Nota: use math para traer la función seno y mostrar la diferencia entre el valor real 
# y la aproximación.

import math

def factorial (n : int) -> int: #funcion para calcular el factorial
    zahl: int = 1
    for i in range(1, n+1):
        zahl *= i
    return zahl

if __name__=="__main__":
    num = int(input("Ingrese cuantos términos de la serie de Maclaurin que desea calcular: "))
    rad = int(input("Ingrese los radianes de la función seno: ")) #radianes
    senx : float = math.sin(rad) #funcion seno en radianes
    suma : float = 0 #valor inicial de la variable donde se guardara la sumatoria de los terminos de la serie

    for i in range (0, num+1):# por medio del ciclo for se hara la sumatoria 
        indx : int = (2*i)+1 
        ndor : float = rad**(indx)
        dnom : float = factorial(indx)
        div : float = ndor/dnom
        expo : float = (-1)**i
        mult : float = expo*div #termino n de la serie Maclaurin
        print ("Termino ", i, " de la serie de Maclaurin: ", mult)
        suma += mult #sumatoria de los terminos para el valor aproximado

    print ("\nFunción seno de ", rad," radianes: ", senx)
    print ("Valor aproximado: ", suma)
    print (senx, "-", suma,"=", senx-suma) #diferencia del valor real y aproximado 
