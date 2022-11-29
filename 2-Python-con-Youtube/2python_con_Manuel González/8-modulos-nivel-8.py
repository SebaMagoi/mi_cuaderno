## Para usar la libreria con  todos los modulos imprtamos math
import math

## Hallar Area de un circulo
# A = pi r 2
"""
radio = float(input('Dime el radio de la circunferencia: '))
area =  math.pi * (radio **2)
print('El Area es: ', area,'.')
"""
## O podemos importar solo lo que vamos a usar del moduo PI de la libreria math. 

# from math import pi, from math import pi, sqrt, 
# o from math import *
"""
from math import pi

## Para ver cuales funciones tiene éste módulo (dir(modulo))
dir(math)
print(math.sqrt(9))
"""

"""
## Hallar Per

radio = float(input('Dime el radio de la circunferencia: '))
perimetro = 2 * pi * radio
print('El perímetro es: ', perimetro,'.')
"""
## Teorema de pitágoras
# a**2 + b**2 = c**2 --> c = raiz a**2 + b**2

# Hacer un programa que calcule la hipotenusa pasandole los lados del triángulo rectángulo pasandole los valores de los lados a y b. 

# Comprobacion ->a(3) y b(4) = c(5). 
"""
from math import sqrt
a = float(input('Dime uno de los catetos: '))
b = float(input('Dime otro de los catetos: '))

c = math.sqrt(a**2 + b**2)
print('El vaor de la Hipotenusa es: ', c)
"""
## Perimetro de la elipse
## p = 2PI ((raiz r**2 + s**2)/2)
from math import pi, sqrt
r = 3
s = 7
p = 2 * pi * sqrt((r ** 2 + s ** 2)/2)
print(p)