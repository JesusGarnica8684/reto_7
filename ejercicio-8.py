# Diseñar una función que permita calcular una aproximación de la función exponencial alrededor
# de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. 
# Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y 
# la aproximación.
import math

def factorial (n : int) -> int: #funcion para calcular el factorial
    zahl: int = 1
    for i in range(1, n+1):
        zahl *= i
    return zahl

if __name__=="__main__":
    num = int(input("Ingrese cuantos términos de la serie de Taylor que desea calcular: "))
    pot = int(input("Ingrese la potencia de la función exponencial: ")) #potencia a la que se eleva e
    fexp : float = math.exp(pot) #funcion exponencial
    suma : float = 0 #valor inicial de la variable donde se guardara la sumatoria de los terminos de la serie

    for i in range (0, num):# por medio del ciclo for se hara la sumatoria 
        ndor : float = pot**i #numerador del termino
        dnom : float = factorial(i) #denominador del termino
        div : float = ndor/dnom #termino n de la serie de Taylor
        print ("Termino ", i, " de la serie de Taylor: ", div)
        suma += div #sumatoria de los terminos para el valor aproximado

    print ("\nFunción exponencial base e en ", pot,": ", fexp)
    print ("Valor aproximado: ", suma)
    print (fexp, "-", suma,"=", fexp-suma) #diferencia del valor real y aproximado 
