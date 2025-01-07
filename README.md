# Reto_7

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
if __name__=="__main__":
    for i in range(1, 101):#se indica el rango del listado
        print(i, "^2=", i ** 2)#se imprime en pantalla los numeros con sus cuadrados
```
2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
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
```
3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
if __name__=="__main__":
    num = int(input("Ingrese el numero por el cual desea iniciar la cuenta regresiva: "))
    print()
    if num % 2 != 0:#si la variable n es impar se convierte un impar
        num = num-1
    for num in range(num, 1, -2):#se define el rango y el paso de dos en dos decreciente
        print(num)
```
4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
if __name__=="__main__":
    num = int(input("Ingrese el numero hasta donde quiere que vaya la lista de factoriales: "))
    zahl : int  = 1
    for i in range(1, num+1):
        fact : int = i*zahl #operacion de factorial
        zahl = fact #reasignacion de valores
        print(i, "! =", fact)
```
5. Calcular el valor de 2 elevado a la potencia n usando ciclos *for*.
```python
if __name__=="__main__":
    num = int(input("Ingrese la potencia de dos que desea calcular: "))
    zahl : int = 1
    for i in range(1, num+1):#se genera el ciclo for hasta el exponente ingresado
        cahl : int = 2 * zahl #se inicia por la potencia de 1
        zahl = cahl # se sobreescriben las variables y se
        #multiplica por dos de nuevo cuantas veces sea necesario
    print("2^", i, "=", cahl)
```
6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. **Disclaimer:** Trate de no utilizar el operador de potencia (**).
```python
if __name__=="__main__":
    base = int(input("Ingrese la base: "))
    pot = int(input("Ingrese la potencia: "))
    zahl : int = 1
    for i in range(1, pot+1):#se genera el ciclo for hasta el exponente ingresado
        cahl : int = base * zahl #se inicia por la potencia de 1
        zahl = cahl # se sobreescriben las variables y se
        #multiplica por la base de nuevo cuantas veces indique la potencia
    print(base, "^", i, "=", cahl)
```
7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
if __name__=="__main__":
    for i in range(1, 10):#incremento del numero a multiplicar
        print("Tabla del ", i, ':')
        for n in range(1, 10):#incremento del multiplicando
            print(i, 'x', n, '=', i*n)
        print()
```
8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

```python
if __name__=="__main__":
    for i in range(1, 101):#se indica el rango del listado
        print(i, "^2=", i ** 2)#se imprime en pantalla los numeros con sus cuadrados
```
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

```python
if __name__=="__main__":
    for i in range(1, 101):#se indica el rango del listado
        print(i, "^2=", i ** 2)#se imprime en pantalla los numeros con sus cuadrados
```
