#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a 
#un número natural n ≥ 2 dado

if __name__=="__main__":
    num = int(input("Ingrese el numero por el cual desea iniciar la cuenta regresiva: "))
    print()
    if num % 2 != 0:#si la variable n es impar se convierte un impar
        num = num-1
    for num in range(num, 1, -2):#se define el rango y el paso de dos en dos decreciente
        print(num)