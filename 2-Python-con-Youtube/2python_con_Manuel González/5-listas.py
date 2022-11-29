mascotas = ['gato', 'perro', 'canario','cocodrilo']
# print(mascotas)

mascotas[3] = 'tortuga'
# print(mascotas)
## Crea secuencias de tuplas o listas segun convega

dias_semana = ('lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo')

dias_entrenamiento = ['lunes', 'miercoles', 'viernes']
# print(dias_semana)
# print(dias_entrenamiento)
"""
mi_tupla = ()
mi_tupla = mi_tupla + (1,2,3)
print(mi_tupla)
mi_tupla = mi_tupla + (4,)
print(mi_tupla)
mi_tupla += (5,6,7,8,9)
print(mi_tupla)

mi_lista = []
print(mi_lista)
mi_lista = mi_lista + [1,2,3,4]
print(mi_lista)
mi_lista += [5,6,7,8,9]
print(mi_lista)
mi_lista_M = mi_lista * 2
print(mi_lista_M)
"""
## Crea una lista que contenga los numeros enteros del 1 al 100 utilizando un bucle while, y partiendo de una lista vacia

lista = []
n = 1
while n <= 100:
	lista = lista + [n]
	n += 1
print(lista)		