tupla = (11,22,33,21,17,62)
print(tupla)
print(type(tupla))

re_tupla = (33, 'hola', 'mundo', 22, True, (3,6,9), ['a', 'b', 'c'])
print(re_tupla)
print(len(re_tupla))
print(re_tupla[0])# 33
print(re_tupla[5][2])# 9
print(re_tupla[6][1])# 'b'
print(re_tupla[1:3])

recontra_tupla = tupla + re_tupla

print(recontra_tupla)

## Tenemos tres tuplas:

## Crea una tupla a partir de ellas que contenga las mascotas 

mamiferos = ('tigre', 'gato', 'león', 'delfín', 'elefante')
reptiles = ('tortuga','serpiente','cocodrilo','dragón')
aves = ('aguila', 'quetsal', 'bhúo', 'buitre', 'paloma')
compañeros = mamiferos + reptiles + aves
print(compañeros)