"""
Reglas generales de las funciones:

1- No se ejecuta una funcion a no se que sea llamada
2- La pueddo llamar las veces que quiera
3- Primero hay que definir la funcion, y despues llamarla
4- Primero van los parámetros requeridos y al final los opcionales

"""
# FUNCIONES CON '1lugarparapensar'


# FUNCIIONES SIN PARAMETROS
"""
defmiFuncion():
	#cojunto de instrucciones
"""
def derechos_humanos():
	print('*Derecho a la vida')
	print('*Derecho a la igualdad ante la ley')
	print('*Derecho a la propiedad privada')
	print('*Derecho a la educacion')
derechos_humanos()

def derechos_mayorDeEdad():
	print('**Derecho a votar')
	print('**Derecho a trabajar.. ?? :)' )
	print('**A hacerle caso al sistema')



# FUNCIONES CON PARAMETROS
"""
def miFuncion2(parametro1, parametro2):
	#conjunto de instrucciones
"""
def mayoria_de_edad(nombre, edad):
	print(f'Según la edad de {nombre}, sus derechos son: ')
	if edad >= 18:
		derechos_humanos()
		derechos_mayorDeEdad()
	else:
		derechos_humanos()
mayoria_de_edad('Sebas', 45)
mayoria_de_edad('Rosa', 60)
mayoria_de_edad('Juan', 12)
# Puedo cambiar el orden de la llamada pero aclarando que
mayoria_de_edad(edad=12, nombre='Julieta')



# FUNCIONES CON PARAMETROS OPCIONALES
"""
def miFuncion3(parametro1, parametro2=valorPorDefecto):
	#conjunto de instrucciones
"""

def mayoria_de_edad2(edad,nombre='Desconocido'):
	print(f'Según la edad de {nombre}, sus derechos son: ')
	if edad >= 18:
		derechos_humanos()
		derechos_mayorDeEdad()
	else:
		derechos_humanos()
mayoria_de_edad2(15)
