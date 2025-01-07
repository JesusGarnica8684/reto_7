#Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
if __name__=="__main__":
    num = int(input("Ingrese el numero hasta donde quiere que vaya la lista: "))
    zahl : int  = 1
    for i in range(1, num+1):
        fact : int = i*zahl #operacion de factorial
        zahl = fact #reasignacion de valores
        print(i, "! =", fact)