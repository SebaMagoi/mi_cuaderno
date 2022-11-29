# Ejercicios de Bucles

"""Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

# Ejercicio 1

"""palabra = input('Dame una palabra...\ny te la multiplicare por 10...')
for i in range(1,10):
	print(palabra)"""


# Ejercicio 2

"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

edad = int(input('Introduce tu edad: '))
for i in range(0, edad):
    print(f'Edad y años cumplidos: {i + 1}')


# Ejercicio 3

"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""

# Solucion de alf

"""n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")"""


"""
num = int(input('Ingresa un numero entero: '))

for i in range(num + 1):
	if num % 2 != 0:
		print(i, end =',')"""


# Ejercicio 4

"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""


"""n = int(input("Introduce un número entero positivo: "))
for i in range(n+1):
	print(n, end =',')
	n -= 1"""


# Ejercicio 5

"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

"""Formula para calcular el valor futuro de una cantidad
VF = M(1 + i) ** n 
VF=valor futuro 
M=monto a invertir
i=interes
N=numero de periodos (años)
"""


"""monto = float(input('Monto: '))
interes = float(input('Interes: '))
anios = int(input('Años: '))

for i in range(anios):
	monto = monto * (1 + interes) ** anios
	print(f'el dinero obtenido despues de {i + 1} anios es de ${monto} ')"""


# solucion por alf
"""amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))

# En español
# Transformado a f string por el Sebas

cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
for i in range(años):
	cantidad *= 1 + interes / 100
	print(f'Capital obtenido luego de ahorrar {i + 1}° año/s es de $ {round(cantidad, 2)}')"""

# Ejercicio 6


"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido."""

# solucion1
"""n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")"""

"""# solucion2
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))"""


"""numero = int(input('Escribe Número: '))
for i in range(numero+1):
	print('*' * i)
	for j in range(numero+1):
		print(end='')"""


# 	Ejercicio 7

"""Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10."""

# por alf
"""for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")"""


# Version Sebas con Miguel reyes
"""for i in range(10):
	print(f'{i + 1} * 1 = {(i + 1) * 1 }')
	print(f'{i + 1} * 2 = {(i + 1) * 2 }')
	print(f'{i + 1} * 3 = {(i + 1) * 3 }')
	print(f'{i + 1} * 4 = {(i + 1) * 4 }')
	print(f'{i + 1} * 5 = {(i + 1) * 5 }')
	print(f'{i + 1} * 6 = {(i + 1) * 6 }')
	print(f'{i + 1} * 7 = {(i + 1) * 7 }')
	print(f'{i + 1} * 8 = {(i + 1) * 8 }')
	print(f'{i + 1} * 9 = {(i + 1) * 9 }')
	print(f'{i + 1} * 10 = {(i + 1) * 10 }')
	print('')"""


#  Ejercicio 8

# 	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

#! i = 1 | j = 1 - 2  -> esta no se toma en cuenta 1° iter
#! i = 3 | j = 3 - 2 = 1  -> 2°iter
#! i = 5 | j = 5 - 2 = 3
#! i = 7 | j = 7 - 2 = 5
#! i = 9 | j = 8 - 2 = 7
#! i = 11 | j = 11 -2 = 9

"""n = int(input('Escribe un numero entero: '))

for i in range(1,( n + 1), 2):
	for j in range(i, 0, -2):
		print(j, end='')
	print('')"""


# Ejercicio 9

# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

"""pwd = input('Escribe tu contraseña: ')
contrasenia = 'Abracadabra'

while pwd != contrasenia:
	intento = input('Contraseña es incorrecta, intenra de nuevo: ')
	if intento == contrasenia:
		print('Bienvenido')
		break"""


# Ejercicio 10

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

"""n = int(input('Escribe un numero para saber sie es primo o no: '))
i = 2
while n % i != 0:
	i += 1
if i == n:
	print(f'El numero: {n} es primo')
else:
	print(f'El numero: {n} no es primo')"""

# por alf 1

"""n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")"""

# por alf 2
"""n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")"""


# Ejercicio 11

# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# por alf
"""word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])"""


"""palabra = input('Escribe una palabra: ')

for i in range(len(palabra) -1, -1, -1):
	print(palabra[i])"""


# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

"""frase = input('Escribe una frase: ')
letra = input('Escribe una letra: ')
cont = 0

for i in frase:
	if i in letra:
		cont += 1
print(f'{letra} aparece {cont} de veces en la frase')"""


# Ejercicio 13

# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

# por alf

"""while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)"""
"""
while True:
    palabra = input('Escribe algo: ')
    if palabra == 'salir':
        break"""
