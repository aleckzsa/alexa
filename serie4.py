numero = float(input("Introduce un número con muchos puntos decimales: "))
print(numero*2)


num = float(input("Introduce un número con muchos numeros decimales: "))
respuesta = num*2
print (respuesta)
print (round(respuesta, 2))

import math
numeroo = int(input("Introduce un numero mayor a 500: "))
respuesta = math.eqrt(numeroo)
print (round(respuesta, 2))


import math
print(round(math.pi,5))


import math
radio = int(input("Introduce el radio del cirulo: "))
area = math.pi* (radio*2)
print (area)


import math
radio = int(input("Introduce el radio del circulo: "))
profundidad = int(input("Introduce la profundidad: "))
area = math.pi*(radio*2)
volumen = area * profundidad
print(round(volumen,3))


numero1 =int(input("Introduce un número: "))
numero2 =int(input("Introduce otro número: "))
respuesta1= numero1//numero2
respuesta2= numero1%numero2
print(numero1, " dividido entre ", numero2, " es ", respuesta1, " con ", respuesta2, " restantes.")


print("1) cuadrado")
print("2) triangulo")
print()
seleccion = int(input("Introduce un número: "))
if seleccion = 1:
    lado = int(input("Introduce la longitud de un lado: "))
    area = lado*lado
    print("El área de tu forma seleccionada es ", area)
elif seleccion= 2:
    base = int(input("Introduce la longitud de la base: "))
    altura = int(input("Introduce la altura del triángulo: "))
    area = (base*altura)/2
    print("El área de tu forma elegida es ", area)
else:
print("Opcion incorrecta seleccionada.")