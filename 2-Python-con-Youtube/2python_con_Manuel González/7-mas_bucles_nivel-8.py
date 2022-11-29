"""
for elemento in 'artefacto':
	print(elemento)

for numero in [1,2,3,4,5,6]:
	print(numero)
"""

"""
dias_semana = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')

for dia in dias_semana:
	print(dia)"""

# Programa que va mostrando en pantalla en cuenta atras, los numeros del 10 al 0, utilizar bucle for
"""
for i in range(10, -1, -1):
	print(i)
"""

"""
for i in range(11):
	print(10 - i)
"""

# Programa que va mostrando en pantalla en cuenta atras, los numeros del 10 al 0, utilizar bucle while.

"""
i = 10
while i >= 0:
	print(i)
	i -= 1
"""

# Hacer  un programa que pida 5 numeros y los va sumando.
# Al final muestra el resultado.

"""suma = 0
for i in range(5):
	n = float(input('Introduce un numero: '))
	suma += n
print('La suma de los numeros es: ',suma)
"""

# Programa que va pidiendo numeros y los va sumando hasta que alcanza 100 o mas. entonces para y muestra el total.

"""suma = 0
while  suma < 100:
	n = int(input('Introduce un numero: '))
	suma  += n
print('La suma es: ',suma)
"""


# ***********************************
"""
letras = ['f', 'g', 'h', 'j', 'l', 'm', 'p', 's']	

encontrado = False

for i in letras:
	if i == 'm':
		encontrado = True

if encontrado:
	print('La letra esta')
else:
	print('La letra no esta')
"""

# Programa que pida un numero al usuario. Si ese numero + algun número de una lista dada = 100, el programa dice que cumple la condicion.
# Usar:
# operador in
# bucle for-in

"""
# 100 - num in lista
lista = [28, 36, 43, 52, 61, 75, 84, 97]
numero = float(input('Dime un numero: '))
if 100 - numero in lista:
	print('El numero  cumple la condicion')
else:
	print('El numero no  cumple la condicion')
"""

"""
# num + elemento == 100
lista = [28, 36, 43, 52, 61, 75, 84, 97]
numero = float(input('Dime un numero: '))
encontrado = False
for elemento in lista:
	if numero + elemento == 100:
		encontrado = True
if encontrado:
	print('El numero cumple la condicion')
else:
	print('El numero no  cumple la condicion')
"""

# Programa que compruebe cuantas veces está un número en un a lista dada.
"""
lista = [28, 36, 43, 52, 43, 61, 75, 43, 84, 43, 43, 97, 43]
num = 43
veces = 0
for i in lista:
	if i == num:
		veces += 1
print('El numero aparece: ',veces, ' veces en la lista')
"""
# 1- Tenemos una tupla con los meses. cuales tienen la latra 'b'
# 2- Como los guardariamos
"""
meses = ('Enero', 'Febrero','Marzo', 
		'Abril', 'Mayo', 'Junio',
		 'Julio', 'Agosto', 'Septiebre',
		  'Octubre', 'Noviebre', 'Diciembre')

meses_con_b = []

for mes in meses:
	if 'b' in mes:
		meses_con_b  += [mes] 
print(meses_con_b)
"""

# Prorgrama que comprueba si un elemento está en una lista y nos dice en que posicion (no indice)
# posicion(indice + 1)  se encuentra
"""
lista = [2, 5, 90, 23, 45, 87, 54, 11, 38]
elemento = 54
"""
# utiliza un tipo range para recorrer la lista por sus índices.

"""for i in range(len(lista)):
	if lista[i] == elemento:
		print('El elemento: ', elemento, ' está en la posicion', i+1)

"""

# Programa que muestre la Tabla de multiplicar de un numero que la damos.
"""
num = int(input('Dame un numero y te devuelvo la tabla Al Toque!: '))
for i in range(1,11):
	print(num, '*', i, '=', num * i) 
"""

# Programa que compruebe si un numero está dentro de una secuencia.
# sentencia break.
"""
numero = 20
secuencia = range(1, 101)
for i in secuencia:
	if i == numero:
		print('Tenemos el numero')
		break
	else:
		print('No es el numero que buscamos')
print('Estamos fuera del bucle')
"""

# Tenemos una lista de temperatúras. Hay que comprobar que todas las temperaturas estas entre 18 y 25 incluidos. si alguna no cumple la concicion se para el programa y lo indica, sino, va mostrando que la temperatura es correcta.
"""
temperaturas = [19,22,21,24,23,27,21,20,19,18,21,20]


for t in temperaturas:
	if 17 < t < 25:# if t < 18 or t > 25:es lo mismo cambiaria de lugar el break
		print('Temperatura correcta')
	else:
		print('Temperatura fuera del rango')
		break
"""

# Programa que pide que adivines un numero del 1 al 10.
# cuando adivines, se para.
"""
## Hecho con bandera.

numero = 5
jugando = True

while jugando:
	intento = int(input('Adivina un numero del 1 al 10: '))
	if numero == intento:
		print('Has acertado')
		jugando = False
	else:
		print('No has aceertado.\nSigue jugando')

"""
"""
## Hecho con break.
numero = 9

while True:
	intento = int(input('Adivina un numero del 1 al 10: '))
	if numero == intento:
		print('Has acertado')
		break
	else:
		print('No has aceertado.\nSigue jugando')
"""

# Juego que pide adivinar una letra, y te pide latras constantemente hasta que la adivine, y recien se detiene.
# se puede probar con todas menos la "w", en cuyo caso, muestra que esa letra no está permitida y se para el programa.

"""letra = 's'
while True:
	intento = input('Que letra estoy pensando?: ')
	if intento != letra:
		if intento == 'w':
			print('La letra no está permitida')
			break
		else:
			print('No has Acertado')
	else:
		print('Has acertado.')
		break"""

# Sentencia continue
# Programa que muestre las letras de una palabra a exepción de la 'h'
"""
palabra = 'zanahoria'

for letra in palabra:
	if  letra == 'h':
		continue
	print(letra)
"""

# Programa que muestra si los numeros de una lista son positivos o negativos,
# a ecepción del cero, que se lo salta.

numeros = [1, 4, -3, 5, 0, 7, -2, 6]

for n in numeros:
    if n == 0:
        continue
    if n > 0:
        print('El numero', n, 'es positivo')
    else:
        print('El numero', n, ' es negativo')
