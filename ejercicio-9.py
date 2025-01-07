# Diseñar una función que permita calcular una aproximación de la función seno alrededor 
# de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. 
# Nota: use math para traer la función seno y mostrar la diferencia entre el valor real 
# y la aproximación.

import math

def factorial (n : int) -> int:
    zahl : int  = 1
    for i in range(1, num+1):
        fact : int = i*zahl #operacion de factorial
        zahl = fact #reasignacion de valores
    return fact

if __name__=="__main__":
    num = int(input("Ingrese cuantos términos de la serie de Taylor que desea calcular: "))
    deg = int(input("Ingrese la potencia de la función exponencial: ")) #potencia 
    sum : float = 0

    for i in range (0, num+1):# por medio del ciclo for se hara la sumatoria 
        ndor : float = deg**(2*i+1)
        dnom : float = factorial((2*i+1))
        div : float = ndor/dnom
        expo : float = (-1)**i
        mult : float = expo*div 
        sum = sum + mult 
        print ("Termino ", i, " de la serie de Taylor: ", sum)
    print (math.sin(deg), "~", sum)
