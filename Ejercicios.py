#1 Realizar un programa dónde se imprima tu nombre.
def nombre(n):
    print(n)
       
nombre("pablo")

#2 Con el programa visto en la clase del viernes 11, en dónde se hacían una serie 
#de operaciones matemáticas, añadir lo siguiente: 
# - Un parámetro que sirva para identificar el operador de la función y, en 
#función del mismo, realizar la operación y posterior almacenamiento en la lista. 
# - Añadir una nueva operación, que es el elevado (símbolo **)
import numbers

def operaciones (N1, N2): 
    num1 = N1
    num2 = N2
    resultado = 0
    listaResultados = [0,0,0,0,0]

    if isinstance(num1, numbers. Number) and isinstance (num2, numbers. Number):

        #Suma de dos valores (+)
        listaResultados[0]= num1 + num2

        #Resta de dos valores (-)
        listaResultados[1] = num1 - num2
        
        #Multiplicación de dos valores (*) 
        listaResultados [2] = num1 * num2

        #División de dos valores (/) 
        listaResultados [3] = num1 / num2

        #Potencia de dos valores (**)
        listaResultados [4] = num1 ** num2

        for i in range (0, len(listaResultados)): 
            print("El resultado de la operación es..") 
            print(listaResultados[i])
            
operaciones (4,2)

#3 Realizar un programa que pasándome como parámetro un número, determinar si es múltiplo de 2 o no.

import numbers

def numero(n):
    num = n

    if isinstance(num, numbers. Number):
        if (num % 2 == 0):
            print ("Es múltiplo de 2")
        else:
            print ("No es múltiplo de 2")

numero(16)
#4 Realizar un programa que, pasándole como parámetro un valor, debe de realizar las siguientes acciones: 
# - En caso de que el color que introduzca el usuario sea “verde” o “VERDE”, debe de mostrarse el siguiente mensaje: “Usted puede pasar sin problema”. 
# - En caso de que el color que introduzca el usuario sea “amarillo” o “AMARILLO”, debe de mostrarse el siguiente mensaje: “Usted puede pasar con dificultades”. 
# - En caso de que el color que introduzca el usuario sea “rojo” o “ROJO”, debe de mostrarse el siguiente mensaje: “Usted no puede pasar bajo ningún concepto”.
def color(c):
    if (c=="VERDE") or (c=="verde"):
        print("Usted puede pasar sin problema")
    if(c=="AMARILLO") or (c=="amarillo"):
        print("Usted puede pasar con dificultades")
    if (c=="ROJO") or (c=="rojo"):
        print("Usted no puede pasar bajo ningún concepto")

color("VERDE")


#5 Realizar un programa que cuente desde el 1 hasta el 100 (ambos incluidos) y los imprima uno a uno.
import numbers

i=0

for i in range(0, 101):
        print(i)


#6 Realizar un programa que cuente desde el 1 hasta el 100 (ambos incluidos) e imprima por pantalla, sólo los números que son pares. 
import numbers

i=0

for i in range(0, 101):
    if (i % 2 == 0):
        print(i)

  
#7 Realizar un programa que cuente desde el 1 hasta el 100 (ambos incluidos) e imprima por pantalla, sólo los números que sean múltiplos de tres.
import numbers

i=0

for i in range(0, 101):
    if (i % 3 == 0):
        print(i)
