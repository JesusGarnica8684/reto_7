#Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

if __name__=="__main__":
    num = int(input("Ingrese el numero hasta donde quiere que vaya la lista de factoriales: "))
    zahl : int  = 1 #valor inicial del factorial 
    for i in range(1, num+1): #ciclo de 1 al numero dado
        zahl *= i #incremento multiplicativo 
        print(i, "! =", zahl)