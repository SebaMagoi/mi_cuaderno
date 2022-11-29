#   Capítulo 3: Booleanos, condicionales y entrada de usuario.

#   Entrada de datos del usuario. Identificación del tipo de datos.

"""edad = input("Introduce tu edad por favor: ")
tipo_de_dato = type(edad)
print(edad)
print(tipo_de_dato)

# Booleans, IF

verdadero = True
falso = False

if(falso == True):
	print("Soy Verdadero!!!")

if (falso == True):
	print("Son iguales")

if(falso == False):
	print("Si Soy Falso!!!")"""

#   Operadores de Compraración ==, !=, <, >, >=, <=
#   Operadores de Compraración else, elif

"""edad = input("Introduce tu edad por favor: ")
edad = int(edad)

if(edad >= 18):
    print("Eres mayor de edad, puedes entrar")
elif(edad < 0):
    print("Eso es imposible")
elif(edad < 15):
    print("Eres adolescente aun")
else:
    print("Eres menor, no puedes entrar")

print("Fin del if")"""

#   Operadores Lógicos and, or, not


"""edad = input("Introduce tu edad por favor: ")
edad = int(edad)
if(type(edad) == int):
        if (edad > 120 or edad < 0):
            print(' Dale, No jodas! Decime tu edaaaad')
        elif(edad > 18 and edad < 65):
            print('Puedes pasar')
        elif(edad < 18 and edad > 15):
            print('Aun no puedes pasar eres adolesenete')
        else:
            print('No ha sucedido ninguna de las condiciones')
else:
    print('La edad debe ser un numero entero')
"""

"""#   Ejercicio: Comprobar si un número introducido por el usuario es par.
#              si el usuario no introduce un número, o el número es decimal
#              el programa debe avisar de que los datos no son correctos.

# PISTAS:
#   isdigit, isdecimal, num%2 = 0"""

"""texto = 'Hola'
print(texto.isnumeric())
txt = '22'
print(txt.isnumeric())"""

num = input('Introduce uun Número por favor: ')

# isnumeric devuelve True or False

if (not(num.isnumeric())):
    print('Datos incorrectos, El dato debe ser un Número')
else:
    num = int(num)
    if(num%2==0):
        print('El numero es Par')
    else:
        print('Es Impar')













