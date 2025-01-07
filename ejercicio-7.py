#Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

if __name__=="__main__":
    for i in range(1, 10):#incremento del numero a multiplicar
        print("Tabla del ", i, ':')
        for n in range(1, 10):#incremento del multiplicando
            print(i, 'x', n, '=', i*n)
        print()