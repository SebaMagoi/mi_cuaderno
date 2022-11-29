"""a = 'altura'
b = 'parte'
c = 'cristal'
d = b[:4] + c[2:3] + a[2:]
print(d)

print('El largo es: ', len('partitura'))"""

# Mostrar en pantalla las letras que forman la palabra "Mariposa"
"""n = 0
cadena = "mariposa"
long = len(cadena)

while n <= long -1:
	print(cadena[n])
	n += 1"""

## Comprobar cuantas veces aparece el caracter 'o,
## con o sin tilde, en la siguiente cadena de caracteres.

cadena = """Muchos años después, frente al pelotón de fusilamiento, el coronel Auréliano Buendia había de recordar aquellla tarde remota en que su padre lo llevó a conocer el hielo."""
"""i = 0 
longitud  = len(cadena)
veces = 0
while i <= longitud -1:
	if cadena[i] == 'o' or cadena[i] == 'ó':
		veces += 1
	i += 1
print("La letra 'o' y 'ó' aparece: ", veces, ' veces')"""

## Operador in
"""print('a' in 'artefacto')
print('la' not in 'artefacto')"""

## visto ésto:
## Programa que diga las vocales que tiene una palabra
"""
palabra = input('Dime una palabra: ')

vocales = 'aeiouáéíóú'
indice = 0
num_vocales = 0 

while indice <= len(palabra)-1:
	if palabra[indice] in vocales:
		num_vocales += 1
	indice += 1
print('El numero de vocales de la palabra es: ', num_vocales)
"""

## Programa que diga las vocales y las consonantes que tiene una palabra que introduce el usuario

palabra = input("Dime una palabra: ")
vocales = 'aeiouáéíóú'
i = 0
num_vocales = 0
num_conosnantes = 0

while i <= len(palabra) -1:
	if palabra[i] in vocales:
		num_vocales += 1
	elif palabra[i] not in vocales:
		num_conosnantes += 1 
	total_letras = num_vocales + num_conosnantes
	i+=1
print('El numero de vocales de la palabra es: ', num_vocales)
print('El numero de consonantes de la palabra es: ', num_conosnantes)
print("El total de letras de la palabra es: ", total_letras)
