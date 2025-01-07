# Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los 
# números pares desde 2 hasta 1000.

if __name__=="__main__":
    print("Numeros impares:")
    for i in range(1, 1000):
            if i%2 != 0:#se confirma que sea impar 
                #el numero no es divisible sobre 2
                print(i)
    print("\nNumeros pares:")
    for i in range(2, 1001):
        if i%2 == 0:#se confirma que sea par
            #el numero es divisible sobre 2
            print(i)