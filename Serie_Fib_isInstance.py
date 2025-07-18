import numbers

def fib(n):
    #Se define la variable de la función fib, que es n
    a = 0
    b = 1

    # isInstance nos permite comprobar si la variable n es un número
    if isinstance(n, numbers.Number): 
        while a < n:
            print(a, end='')
            a = b
            b = a + b 
            print()
    else: 
    #En caso de que no lo sea, hace un print diciendo que no lo es
        print("Eso no es un número")

fib(10000)
