"""print(range(12))
print(5 in range(12))

a = list(range(7,45,7 ))
print(a)
print(len(a))"""


## Programa qie pida un numero entero qie este en el rango de 18 y 25, y que siga pidiendo mientras e numero ingresado se mantenga en el rangp
"""probando = True

while probando:
	n = int(input('Introduce un numero entre el rango de 18 y 25: '))
	if n in range(18, 26):
		print('Estas dentro del rango')
	else:
		print('Estas fuera del rango')
		probando = False"""

## Juego ruleta de los colores

print('Adivina los 5 colores de la Ruleta de colores. \nconsigue puntos hasta fallar')

colores = ['azul','amarillo','rojo','verde', 'blanco']
puntos = 0

jugando = True
while jugando:
	color = input('DIme un color: ')
	if color in colores:
		puntos += 1
		print('Acertaste')
		print('Tienes: ',puntos, ' punto')
	else:
		puntos -= 1
		print('Fallaste')
		print('Tienes: ',puntos, ' punto')
		jugando = False
	if puntos == 5:
			print('Fin del prograna')	
			break
