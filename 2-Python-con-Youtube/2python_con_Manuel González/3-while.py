"""
if 2 < 3:
	print("Hola")
"""
"""
while 2 < 3:
	print("Hola")  Bucle infinito
"""


## Mostrar una secuencia del 1 al 11
"""
print("Inicio del programa 1 al 11")

n = 1
while n <= 11:
	print(n)
	n += 1  

print("Fin del programa 1 al 11")

"""

## Mostrar en pantallla una secuencia como la anterior pero rango de 20 al 10
"""
print("Inicio del programa 22 al 11")
n = 22  

while n >= 11:
	print(n)
	n -= 1 

print("Fin del programa 22 al 11")
"""

## Programa que pregunte al usuario si quiere seguir jugando

"""print("Vamos a Jugar.")

jugando = "s"

while jugando == "s":
	print("Seguir jugando.")
	jugando = input("¿Quiueres seguir jugando (s/n) ?")

print("Fin del programa")"""

## Programa que pida numero entre 10 y 20. Si es True, que diga que está en el rango y que pida otro numero hasta que le pase un numero fuera del rango, y finalice el programa.

"""
numero = int(input("Introduce un numero entre el rango de 10 y 20:... "))


while n >= 10 and n <=20:....
o
while 10 <= n <= 20:....
o
usar rango...
"""
"""
while numero in range(10, 21):
	print("Estás en el rango")
	numero = int(input("Introduce otro numero:... "))
else:
	print("Te has salido del rango.")

print("Fin del programa.")
"""

## Revive el programa del juego y agragamos el numero de iteracion ¿Cuantas veces iteramos dentro del bucle

"""
print("Vamos a Jugar.")

jugando = "s"
veces = 0

while jugando == "s":
	veces = veces + 1 # añade las veces que hemos jugado
	print("Seguir jugando.")
	print("Hemos jugado: ", veces, " veces")
	jugando = input("¿Quiueres seguir jugando (s/n) ?")

print("Fin del programa")
"""

## Pedir adivina un numero del 1 al 10 y que pida constantemente hasta que lo adivine, añade un contador que te diga los intentos que he necesitado. Conviene crear tres variables y usar un else. 

"""
intentos = int(input("Hola! \nAdivina un numero del 1 al 10: "))
n = 3
veces = 1
while intentos != n:
	intentos = int(input("Mmmm..No! \nIntenta adivinar nuevamente del 1 al 10!: "))
	veces += 1
else:
	print("Has Acertádo !!! ")
	print("Has necesitado", str(veces), " veces" )
"""


## Programa que sume los numeros del 1 al 10
"""
comprobacion = 1+2+3+4+5+6+7+8+9+10
print("Comprobacion: ",comprobacion)

n = 1
suma = 0 
while n <= 10:
	suma += n
	n += 1
print("Resultado suma", suma)
"""


## Programa que sume los pares que hay entre el 1 y el 20 

"""
n = 1
suma = 0
while n <= 20:
	if n % 2 == 0:
		suma += n
	n += 1
print("Resultado suma es: ",suma) 
"""


## Programa que pida numero de inicio y numero de final y que sume todos los numeros multiplos de 3 que hay entre ellos. Comprobacion con n inicio 119 y n final 132

"""
comprobacion = 120+123+126+129+132
print("Comprobacion: ",comprobacion)
suma = 0
inicio = int(input("Dame un numero inicial: "))
final = int(input("Dame otro numero final: "))
while  inicio <= final:
	if inicio % 3 == 0:
		suma += inicio
	inicio += 1
print("Resultado suma es: ",suma) 
"""
## Programa que pida contraseña y hasta que sea correcta, no pasara el bucle
# LUEGO AGREGAR QUE PIDA USUARIO
"""
print("Bienvenido al sistema")
usuario = 'El Mago'
intento_user = input("Introduce el usuario: ")

while intento_user != 'El Mago':
	print("El usuario No es correcto")
	intento_user = input(("Intenta de nuevo introducir el Usuario")) 
print("El Usuario es corrrecto")

contraseña = 'resistencia'
intento_contraseña = input("Ahora, Introduce la contraseña: ")

while intento_contraseña != 'resistencia':
	print("La contraseña no es correcta: ")
	intento_contraseña = input("Introduce la contraseña nuevamente: ")
print("La contraseña Es correcta.")
print("Estás dentro...")
"""

# Otro modo Me gusta más mi metodo, el de arriba
"""
print("Bienvenido al sistema")

usuario = 'El Mago'
contraseña = 'resistencia'

intento_user = input("Introduce el usuario: ")
intento_contraseña = input("Ahora, Introduce la contraseña: ")

while intento_user != usuario or intento_contraseña != contraseña:
	print("El usuario o la contraseña No es correcto")
	intento_user = input(("Introduce el usuario: "))
	intento_contraseña = input("Introduce la contraseña: ")
else:
	print("Usuario y contraseña Es correcta.")
	print("Estás dentro...")
"""

## Uso de Banderas, con el programa anterior mismo
"""
print("Bienvenido al sistema")

usuario = 'El Mago'
contraseña = 'resistencia'
entrando = True
while entrando:
	intento_u = input("Introduse tu Usuario: ")
	intento_c = input("Introduse tu contraseña: ")
	if intento_u == usuario and intento_c == contraseña:
		print ("El usuario y la contraseña son correctas.")
		entrando = False
	else:
		print("Usuario o contraseña Icorrectas.")
print("Entramos..")
"""

## Juego que pregunta un numero del 1 al 5 y luego una vocal.
## Tienes 100 puntos, si aciertas 1 de ellos, te quita 2 puntos,
## si no aciertas ninguno te quita 5 puntos.
## El programa No se acaba hasta que acierte los 2.
## Cuando se acaba el programa te dice cuantos puntos te quedan

print("Inicio del Juego ! .")

n = '3'
v = 'o'
puntos = 100
jugando = True


while jugando:
	intento_n = input("Introduce un numero del 1 al 5: ")
	intento_v = input("Introduce una vocal: ")

	if intento_n != n and intento_v != v:
		puntos -= 5
		print("No has acertado ninguno. Te quedan: ", puntos, " puntos, adelante.")
	elif intento_n != n or intento_v != v:
		puntos -= 2
		print("Has acertado uno. Te quedan", puntos, " puntos.")
	else:
		print("Has acertado. Tus puntos restantes son: ", puntos, " puntos.")
		jugando = False

print("Fin del Juego")