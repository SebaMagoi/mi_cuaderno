 #   Capítulos 6: Listas

#   Apartado 1: Repaso de conceptos básicos

"""numeros = [1,2,3,4,5]
primera_posicion = numeros[0]
longitud = len(numeros)
print(f'El primer valor es : {primera_posicion}\nla longitud de la lista es: {longitud}')

print("Iterar sobre los elementos de una lista llamada numeros: ")
for num in numeros:       #   Iterar sobre los elementos de una lista
    print(num)
"""
#   Apartado 2: Indexado y sublistas
"""
lista = ['Ella es','mi','amor','especial','prepactado']
print(lista)

ultima_posicion = lista [-1]
print(ultima_posicion)

pen_ultimo = lista [-2]
print(pen_ultimo)

subLista = lista[1:4]
print(subLista)

subLista = lista[:2]
print(subLista)

subLista = lista[:4]
print(subLista)

subLista = lista[2:]
print(subLista)

subLista = lista[1:]
print(subLista)

subLista = lista[-3:-2]
print(subLista)

subLista = lista[-4:-1]
print(subLista)"""

#   Apartado 3: Comprobar si una lista contiene o no un elemento


lista = ['Ella es','mi','amor','especial','prepactado']
palabra = 'amor'
palabra2 = 'melocoton'

if palabra in lista:
	print('La palabra existe en la lista')

if palabra2 not in lista:
	print('La palabra no existe en la lista')

print(lista)
print(palabra)
print(palabra2)

