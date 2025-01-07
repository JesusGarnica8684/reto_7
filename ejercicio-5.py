#Calcular el valor de 2 elevado a la potencia n usando ciclos for.

if __name__=="__main__":
    num = int(input("Ingrese la potencia de dos que desea calcular: "))
    zahl : int = 1 
    for i in range(1, num+1):#se genera el ciclo for hasta el exponente ingresado
        cahl : int = 2 * zahl #se inicia por la potencia de 1
        zahl = cahl # se sobreescriben las variables y se 
        #multiplica por dos de nuevo cuantas veces sea necesario
    print("2^", i, "=", cahl)