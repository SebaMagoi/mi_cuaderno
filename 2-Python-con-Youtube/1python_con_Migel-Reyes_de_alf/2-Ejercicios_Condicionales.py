# Ejercicio 1- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
 
"""edad = int(input("Introduce tu edad por favor: "))
if edad >= 18:
	print("si eres mayor de edad")
else:
	print("No eres mayor de edad")"""

# Ejercicio 2 

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

"""contrasena = 'tesla'
password = input('¿Cual es la contrasena?: ')
password = password.lower()  # transforma todo en mayusculas
# password = password.upper() # Transforma todo a minuscula
if contrasena == password:
	print('Bienvenido')
else:
	print("Contrasena incorrecta")
	"""

# Ejercicio 3

# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor(Denominador) es cero el programa debe mostrar un error.

"""numerador = int(input('Escribe un numerador'))
denominador = int(input('Escribe un denominador'))
if denominador == 0:
	print('Error no es posible la division entre cero')	
else:
	print(f'La division de {numerador} entre {denominador} es {numerador / denominador}')"""


# Ejercicio 4

# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
numero = int(input(" escribe un numero: "))
if numero % 2 == 0:
	print(f"El numero {numero} es par")
else:
	print(f"El numero {numero} es impar")"""

# Ejercicio 5

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
edad = int(input('¿Cuantos anios tienes?: '))
ingresos = int(input('¿Cuanto es tu ingreso mensual?: '))
if edad > 16 and ingresos >= 1000:
	print('Tienes que pagar')
else:
	print('No tienes que pagar')"""


# Ejercicio 6

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

"""nombre = input("¿Cual es tu nombre?: ")
sexo = input("¿Cual es tu sexo? (H o M): ")
grupo = ""

if ((nombre.lower() < 'm' and sexo == 'M') or (nombre.lower() > 'n' and sexo == 'H')):
	grupo = 'A'
else:
	grupo = 'B'

print(f'{nombre} perteneces al grupo {grupo}')"""

# La solucion 1 de alf:
# Ejercicio 6

"""name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

# La solucion 2 de alf:
# Ejercicio 6

name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)"""


# Ejercicio 7

# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

"""	Renta				Tipo impositivo
Menos de 10000€				5%
Entre 10000€ y 20000€		15%
Entre 20000€ y 35000€		20%
Entre 35000€ y 60000€		30%
Más de 60000€				45%

 Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""
 # por alf
"""# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')"""



# Ejercicio 8

"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4. o 0.6, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel"""

"""Nivel		Puntuación
Inaceptable			0.0
Aceptable			0.4
Meritorio			0.6

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario."""

# Por alf

"""bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))"""

# Ejercicio 9

# Por alf

"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€."""

"""edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")"""



# Ejercicio 10

# Por alf

"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""


# Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza

if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t1- Pimiento\n\t2- Tofu\n")

    ingrediente = input("Introduce el ingrediente que deseas: ")

    print("Pizza vegetariana con mozzarella, tomate y ", end="")
	
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")