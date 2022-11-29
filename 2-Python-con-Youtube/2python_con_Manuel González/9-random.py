import time
import random
# print(dir(random))
# Genera un numero aleatorio int
# print(random.randint(1, 10))
"""
Juego que genera un numero aleatorio del 1 al 100 y te pide que lo adivines.
Se te va indicando si el numero introducido es mayor que el que hay que adivinar.
Tiene 7 intentos, si no, el programa se termina y te dice que has perdido.
"""

"""
numero = random.randint(1, 100) 
intentos = 0

jugando = True

print('Adivina un numero del uno al 100: ')

while jugando:
    intentos += 1
    if intentos <= 7:
        eleccion = int(input('Dime un numero: '))
        if eleccion == numero:
            print('Has acertado!!!\nHas usado: ', intentos, ' intentos.')
        elif eleccion > numero:
            print('Debes Disminuir. \nLlevas', intentos, ' intentos.')
        elif eleccion < numero:
            print('Debes Aumentar. \nLlevas', intentos, ' intentos.')
    else:
        print('Se terminaron los intentos.Comienzas de nuevo?...')
        jugando = False
"""

# Funcion choice de random

# print(random.choice([1, 2, 3]))

"""
# Mejorar el juego anterior con random.choice

numero = random.randint(1, 100)
intentos = 0

opciones_alto = ['Uff, te has pasado.',
                 'Demasiado alto.',
                 'Valla alto.',
                 'Dale, no tan alto.']

opciones_bajo = ['Valla, Te has quedado corto.',
                 'Ufff, un poco bajo.',
                 'Demasiado bajo.',
                 'Dale, no tan alto.']
jugando = True

while jugando:
    intentos += 1

    alto = random.choice(opciones_alto)
    bajo = random.choice(opciones_bajo)

    if intentos <= 7:
        eleccion = int(input('Dime un numero: '))
        if eleccion == numero:
            print('Has acertado!! Has usado:', intentos, ' intentos.')
            jugando = False
        elif eleccion > numero:
            print(alto, 'Llevas', intentos, ' intentos.')
        elif eleccion < numero:
            print(bajo, 'Llevas', intentos, ' intentos.')
    else:
        print('Se terminaron los intentos.Comienzas de nuevo?...')
        jugando = False
"""
"""
# Programa que simula 100 tiradas de moneda y comprueba cuantas veces sale, cada resultado posible.
import random
caras = 0
cruces = 0
for i in range(100):
    tirada = random.choice(['cara', 'cruz'])
    # tirada = random.randint(1, 2)
    if tirada == 'cara':  # if tirada == 1:
        caras += 1
    elif tirada == 'cruz':  # if tirada == 2:
        cruces += 1
print('Han salido', caras, ' caras, y ', cruces, 'cruces')
"""


# Juego de piedra papel o tijera
# hacer que me permita seguir jugando hasta que decida salir del bucle
"""
jugando = True
while jugando:
    print('Jugamos una Partída de piedra, papel o tijeras?: ')
    ordenador = random.choice(['piedra', 'papel', 'tijeras'])
    jugador = input('Elije una opcion: ')

    if jugador == 'piedra':
        if ordenador == 'piedra':
            print('Ordenador elije "piedra". Empate')
        elif ordenador == 'papel':
            print('El ordenador elije "papel" Papel envuelve a Piedra Ordenador Gana')
        else:
            print('Ordenador elije "tijeras". Piedra rompe Tijeras Tu Ganas')
    elif jugador == 'papel':
        if ordenador == 'piedra':
            print('Ordenador elije "Piedra",.Papel envuelve piedra. Tu Ganas!')
        elif ordenador == 'papel':
            print('Ordenador elije "Papel". Empate.')
        else:
            print('Ordenador elije "Tijeras", Tijeras cortan Papel. Ordenador gana')
    elif jugador == 'tijeras':
        if ordenador == 'piedra':
            print('Ordenador elije "Piedra", Piedra rompe Tijeras. Ordenador Gana')
        elif ordenador == 'papel':
            print('Ordenador elije "Papel", Tijeras cortan Papel. Tu Ganas')
    else:
        print('No has elejido una opcion correcta')

    seguir = ''

    while seguir != 'n' or seguir != 's':
        seguir = input('Quieres volver a jugar (s/n): ')
        if seguir == 'n':
            jugando = False
            break
        elif seguir == 's':
            break
        else:
            print('No te he entendido')
"""


"""
     ** Modulo time **
"""
# print(dir(time))
# print(help(time.time))

# Programa donde jugamos a que pase el tiempo
"""
inicio = time.time()

while True:
    print('Estamos Jugando...')
    final = time.time()
    if final - inicio >= 3:
        break
print('Fin del juego')
print('Tiempo del juego: ', final - inicio)
"""
"""inicio = time.time()

for i in range(23):
    print(23-i)
    time.sleep(1)
final = time.time()
print('Tiempo: ', final - inicio - 1)
"""


# Calcula la suma se los numeros del 1 al un millón:
# 1+2+3+4+5+6+7 ... 1.000.000
# Hacer con un 'while' y con un 'for' y mide el tiempo de ejecucuón

# time.time()
# time.perf_counter() *
# time.clock()

inicio = time.perf_counter()

"""suma = 0
n = 1
while n < 1_000_001:
    suma += n
    n += 1
final = time.perf_counter()
print('La suma es:', suma)
print('Tiempo con while: ', final - inicio)
"""
"""
inicio = time.perf_counter()
suma = 0
for i in range(1, 1_000_001):
    suma += i
final = time.perf_counter()
print('La suma es:', suma)
print('Tiempo con while: ', final - inicio)
"""

# nos devuelve un numero entero dentro del rango que le pasamos
print(random.randint(1, 10))
# si le pasamos una lista y la función choice, me devuelve un elemento de esa lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(lista))

# La función 'random.shuffle', no nos devuelve nada, simplemente baraja los elementos de la lista que le pasemos. Los ordena de forma aleatoria

print(random.shuffle(lista))  # no imprime nada sin embago
print(lista)  # los ha entreverado

# random.sample(lista, 3)
# Lleva 2 argumentos y el numero de elementos aleatorios que va a tomar de esa lista. Me devuelve una lista con 3 elementos de la lista aleatoriaamente, en otra lista.

muestra = random.sample(lista, 3)
print(muestra)

# Juego de memoria. Te muestra4 colores y te da 3 segundos para recordarlos en el orden en que aparecian.
# Si aciertas te los vuelve a mostrar en oren distinto.
