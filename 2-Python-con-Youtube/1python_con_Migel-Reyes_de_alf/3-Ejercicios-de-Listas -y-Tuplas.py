import math 

# Ejercicios de Listas y Tuplas

# Ejercicio 1

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

# yo
"""asignaturas_listas = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
asignaturas_tupla = ('Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua')  

asignaturas_listas.append('Programacion')

print(f'La lista de las asignaturas_listas es: {asignaturas_listas}')
print(f'La tupla de las asignaturas_tuplas es: {asignaturas_tupla}')"""


# Ejercicio 2

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

# yo
"""asignaturas_listas = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
for asignatura in asignaturas_listas:
	print(f'Yo estudio {asignatura}')

# Funcionaria con una tupla?
asignaturas_tupla = ('Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua') 
for asignatura in asignaturas_tupla:
	print(f'Yo estudio{asignatura}')"""



# Ejercicio 3

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# yo
"""asignaturas_lista = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
calificaciones_lista = []

for asignatura in asignaturas_lista:
	calificacion = float(input(f'Que calificacion obtuviste en {asignatura}?: '))
	calificaciones_lista.append(calificacion)

for i in range(len(asignaturas_lista)):
	print(f'En {asignaturas_lista[i]} conseguiste {calificaciones_lista[i]} ')"""


# Ejercicio 4

#  Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva(elejir  6 numeros diferentes entre 1 y 49), los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# yo
"""numeros_ganadores = []
for i in range(6):
	numeros_ganadores.append(int(input('Escribe un numero ganador: ')))
numeros_ganadores.sort() # Ordena los numeros de menor a mayor
print(f'Los numeros ganadores son: {numeros_ganadores}')"""




# Ejercicio 5

# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# por alf
"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")"""


"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")"""



# yo
"""n = list(range(0,11))
print(n[::-1])"""





#Ejercicio 6

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# por alf 
"""subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))"""

# por alf
"""subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))"""


# yo

"""asignaturas_lista = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
asignaturas_a_repetir = []

for asignatura in asignaturas_lista:
	nota = float(input(f'Que nota obtuviste en : {asignatura} '))
	if nota < 7:
		asignaturas_a_repetir.append(asignatura)
print(f'Debes repetir : {asignaturas_a_repetir} ')"""






# Ejercicio 7

# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# por alf
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i-1)
print(alphabet)"""

# por alf 2
"""alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i-1)
print(alphabet)"""


# yo
"""alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(alfabeto),0 , -1):
	if i % 3 ==0:
		alfabeto.pop(i-1)
print(alfabeto)"""

# comprobacion
"""for i in range(len(alfabeto),0 , -1):
	print(f'Soy i fuera del if: {i}')
	if i % 3 ==0:
		print(f'Soy i dentro del if: {i}')
		alfabeto.pop(i-1)
print(alfabeto)"""





# Ejercicio 8

# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

# por alf
"""
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
"""

# en español
"""palabra = input("Introduce una palabra: ")
reversa_palabra = palabra
palabra = list(palabra)
reversa_palabra = list(reversa_palabra)
reversa_palabra.reverse()
if palabra == reversa_palabra:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")"""

# yo, Miguel Reyes
"""palabra = list(input('Escribe una palabra '))

if palabra[::] == palabra[:: -1]:
	print(f'palabra Es Palindromo ')
else:		
	print(f'palabra No es Palindromo ')"""




# Ejercicio 9

# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# por alf
"""
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
"""

# yo
"""palabra = list(input('Escribe una palabra: '))

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

for letra in palabra:
	if letra == 'a' or letra == 'A':
		contador_a +=1
	elif letra == 'e' or letra == 'E':
		contador_e +=1
	elif letra == 'i' or letra == 'I':
		contador_i +=1		
	elif letra == 'o' or letra == 'O':
		contador_o +=1
	elif letra == 'u' or letra == 'U':
		contador_u +=1
print(f' La letra a aparece :{contador_a} veces')
print(f' La letra e aparece :{contador_e} veces')
print(f' La letra i aparece :{contador_i} veces')
print(f' La letra o aparece :{contador_o} veces')
print(f' La letra u aparece :{contador_u} veces')"""




# Ejercicio 10

# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

# por alf 
"""prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))"""

# yo
"""precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort()
print(f'El numero mas pequeño de la lista {precios} es: {precios[0]} ')
print(f'El numero mas grande de la lista {precios} es: {precios[-1]} ')"""







# Ejercicio 11

# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

# por alf
"""a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) """

# yo

# *escalar(1,2,3) + (-1, 0, 2) = [1 * -1] + [2 * 0] + [3 * 2] = [-1 + 0 + 6] = 5
"""
v1 = (1,2,3)
v2 = (-1,0,2)

producto_escalar = 0

for i in range(len(v1)):
	producto_escalar += v1[i] * v2[i]
print(f'El producto escalar de {v1} * {v2} = {producto_escalar} ')"""







# Ejercicio 12
# Escribir un programa que almacene las matrices
"""
A = 1 2 3       y B = -1 0
	4 5 6              0 1
					   1 1	
"""
# en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

# por alf
"""a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]	
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])"""


# yo
"""import numpy as np

a = np.array([ [1,2,3],
			[4,5,6] ]) # 2x3

b = np.array([ [-1,0],
			[0,1],
			[1,1] ]) # 3x2

# (2x3) * (3x2) = (2x2)

print(a@b)"""





# Ejercicio 13

# Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

# por alf
"""sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)"""


# yo
import statistics

muestra = input('Introduce una muestra de numeros: ')
muestra = list(muestra.split(','))
print(muestra)

for i in range(len(muestra)):
    muestra[i] = int(muestra[i])

promedio = sum(muestra) / len(muestra)# suma de datos / la cantidad de datos
desviacion_standar =  statistics.stdev(muestra)
print(f'El promedio de: {muestra} es {promedio} y la desviaion standart es {desviacion_standar} ')








