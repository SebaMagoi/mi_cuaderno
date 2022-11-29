#   Capítulo 4: Funciones
#   Definición de las funciones

# def saludar():
# 	print("Hola que tal?")
# saludar()
# saludar()
# saludar()

# Funciione con argumentos
# def saludo(nombre):
# 	print("Hola", nombre, "como estas?")
# saludo("Sheila")

# #Funciones que retornan un resultado

# def suma(a,b):
# 	resultado = a + b
# 	return resultado
# valor = suma(10, 12)
# print(valor)
# valor = suma(22,10) 
# print(valor)

# def sumaDos(a,b):
#     return a + b
# valorDos = sumaDos(22,11)
# print(valorDos)

# def sonIguales(num1, num2):
#  	return num1 == num2
# verdad = sonIguales(22,22)
# if (verdad):
# 	print("Son iguales")
# else:
# 	print("soSon diferentes")

# print(verdad)	
# verdad = sonIguales(3,5)
# print(verdad)

# Funciones con argumentos por defecto

# def saludar_por_defecto(nombre="dushe"):
# 	print("Hola", nombre, "Que tal?")

# saludar_por_defecto()
# saludar_por_defecto("Sheila")

# Funciones quee retornan varios valores

# def suma_y_resta(a,b):
# 	suma = a + b
# 	resta = a - b
# 	return suma, resta
# 	#return a+b, a-b # en una linea

# resultado1, resultado2 = suma_y_resta(10, 5)
# print("Los resultados son:\nSuma: " + str(resultado1) + "\nResta: " + str(resultado2))


"""
EJERCICIO 1: Función máximo -> Dados dos números, la función debe encontrar cuál de los dos es el más grande y retornarlo.Extra: Se deben comprobar que los argumentos de la función sean
de tipo int o float. Si alguno de los dos no lo es, mostrar un mensaje de error y retornar False."""

# def maximo(num1, num2):
# 	if ((type(num1)==int or type(num1)==float) and (type(num2)==int or type(num2)==float)):
# 		if (num1 > num2):
# 			return num1
# 		else:
# 			return num2
# 	else:
# 		print("Error! pone numeros boludo")
# 		return False
		

# num = maximo(121, 2222)
# if(type(num) != bool):
# 	print("El maximo es :" + str(num))

# num = maximo(12, "HUevo frito")
# if(type(num) != bool):
# 	print("El maximo es :" + str(num))

"""
EJERCICIO 2: Mini calculadora. Pedirle al usuario una operación y dos números. 
Las operaciones pueden ser suma, resta, potencia. Si introduce una operación diferente a estas, mostrar un mensaje de error. Si la operación es correcta, mostrar el resultado.
"""

"""print("Apartado 6: Ejercicio 2. Mini calculadora")

print("Las operaciónes son: suma, resta, multiplicacion, division, potencia")

def calculadora():

	operacion = input("¿Que operacion deceas realizar?: ")

	if (not(operacion == "suma" or operacion == "resta" or operacion == "multiplicacion" or operacion == "division" or operacion == "potencia")):
		print("La Oeracion es incorrecta.\nLas operaciónes son:\nsuma\nresta\nmultiplicacion\ndivision\npotencia")
		return 

	num1= float(input("Introduce El 1° numero: "))
	num2= float(input("Introduce El 2° numero: "))

	if (operacion == "suma"):
		print(num1 + num2)
	elif (operacion == "resta"):
		print(num1 - num2)
	elif (operacion == "multiplicacion"):
		print(num1 * num2)
	elif (operacion == "division"):
		print(num1 / num2)
	elif ( operacion == "potencia"):
		print(num1 ** num2)
	else:
		print("La Oeracion es incorrecta.\nLas operaciónes son:\nsuma\nresta\nmultiplicacion\ndivision\npotencia")

calculadora()"""

