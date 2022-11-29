
#   Capítulo 5: Bucles

#   Breve introducción a las listas

"""numeros =[1,2,3,4,5,6]
# La posicion en la listas van desde el cero hasta la posicion LONGITUD -1
print(numeros)
print(numeros[0])
print(numeros[3])
print(numeros[-1])

print(len(numeros))
texto = ['Seba','sebá','Termo']
variado = ['Seba',' Y ','Sophia',True, 9.0]

# La posicion en la listas van desde el cero hasta la posicion LONGITUD -1
print(texto[len(texto)-1 ])
print(texto[2])
# Las 2 dan el mismo resultado

print(variado)
print(texto[3])
print(variado[0:3])"""


# Bucle for

"""for i in range(5):
    print(i)"""

"""for x in range(2, 12,2):
    print(x)"""


"""
#   Mini ejemplo, imprimir solo las vocales de una palabra
frase = 'Bien Dushe segui adelante'
for letra in frase:
    if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
        print('Es una vocal ',letra)
    else:
        print('Es una consonante ',letra)
        """

#   Mini ejemplo, iterar sobre una lista

"""numeros = [22,33,44,55]
for numero in numeros:
    print(numero)
    numero += 10
    print(numero)
print(numeros)

for indice in range(len(numeros)):
    numeros[indice] += 10
print(numeros)"""


#   Bucles While

"""i = 0
while(i < 12):
    print(i)
    i += 1


contador = 12 # contador inicia valiliendo cer0
while (contador < 23):
	print(contador)
	contador+=1
"""

# Encontrar la primera 'a en una frase 

"""letraEncontrada = False
letra = 'a'
frase = 'En este momentro estoy buscando la letra:  a '
indice = 0

while(not(letraEncontrada)):
    if(frase[indice] == 'a'):
        letraEncontrada = True
        print(f'Ya hemos encontrado la letra: {letra} en la posicion: {indice}')
    else:
        indice += 1"""

# El mismo ejemplo pero  con un for

# Implementando break, continue, y pass

"""frase = 'En este momentro estoy buscando la letra:  y '
letra = 'y'
for c in frase:
    if(c == letra):
        print(f'Letra {letra} encontrada en la posicion {frase.index(c)}!!') 
        print(f'Letra {c}')
        break
    else:
        print('No hemoos encontrado letra')"""

# Continue

"""frase = 'Hola Sophia'
letra = 'a'
cont = 0

for c in frase:
    if(c == letra):
        cont += 1
        print(f'La letra fue encontrada {cont} veces ')
        continue
        print('No se encontró la letra')"""

"""# Pass
lista = [0,11,22,43]
for sophi in lista:
    if(sophi == 11):
        pass
    print(f'El valor de Sophi es: {sophi} ')

def funcionCutre(arg1, arg2):
    pass
def funcionCutre(arg1, arg2):
    pass"""

#   Else
"""frase = "Todos los caracteres de una frase"
cont = 0
for caracter in frase:
    cont += 1
    if(caracter == 'l'):
        break
else:
    print(f'La frase contiene {cont} caracteres')"""


#   Ejercicio: El usuario debe adivinar un número entre 0 y 10.
#   El programa deberá pedir que el usuario introduzca un número
#   y debe decir si ha acertado, si el número es menor o mayor que
#   el que ha introducido.

"""num = int(input("Intricuce un numero de entre el --1 y el 10-- por favor: "))
numero_guardado = 3
if(type(num) == int):
    if(num > 0):
        while(num < 11):
mal rumbiado
"""
numero_correcto = 7
def pedirYcomprobar(numAAdivinar):
    numUser = int(input("Intricuce un numero de entre el --1 y el 10-- por favor: "))
    if(numUser==numAAdivinar):
        print('El numero es correcto, Has Acertado')
        return True
    elif(numUser > numAAdivinar):
        print('Casi... El numero debe ser menor')
        return False
    elif (numUser < numAAdivinar):
        print('casi... El numero debe ser mayor')
        return False

"""while(True):
    if(pedirYcomprobar(numero_correcto)):
        break"""# una segunda forma de hacerlo es:

while(not(pedirYcomprobar(numero_correcto))):
    pass
else:
    print('Fin del Juego')    