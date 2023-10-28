def multiplicacion(a, b):
    print(f'el resultado de la multiplicacion de {a} y {b} es {a*b}')
    print(f'y el anterior es {par(a*b)}')

def par(a):
    if(a%2==0):
        return(f"el numero {a} es par")
    else:
        return(f"el numero {a} es impar")

print("inicia el software")
multiplicacion(3,5)

print(par(34))