#Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. 
# Disclaimer: Trate de no utilizar el operador de potencia

if __name__=="__main__":
    base = int(input("Ingrese la base: "))
    pot = int(input("Ingrese la potencia: "))
    zahl : int = 1 
    for i in range(1, pot+1):#se genera el ciclo for hasta el exponente ingresado
        cahl : int = base * zahl #se inicia por la potencia de 1
        zahl = cahl # se sobreescriben las variables y se 
        #multiplica por la base de nuevo cuantas veces indique la potencia
    print(base, "^", i, "=", cahl)