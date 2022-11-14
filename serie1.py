nombre = input("¿Cuál es tu nombre?")
edad = int (input("¿Cuántos años tienes?"))
sumaedad = edad + 1
print(nombre, "tu siguiente cumpleaños sera", sumaedad)

cuenta = int(input("¿Cuál es total de la cuenta?"))
comensales= int (input("¿Cuántas personas comieron?"))
division = cuenta/comensales
print("Cada persona debera pagar: ", division)

dias = int(input("Introduce una cantidad de dias: "))
horas = dias*24
minutos = horas*60
segundos = minutos*60
print("En ", dias " dias hay ", horas,  " horas, ", minutos, " minutos y ", segundos, " segundos." )

kilo = int(input("Introduce un número de kilos: "))
libra = kilo * 2.204
print("Es igual a ", libra, " libras.")

grande = int(input("Introduce un número mayor a 100: "))
pequeño = int(input("Introduce un número menor a 10: "))
division = grande/pequeño
print(Pequeño, "cabe en ", grande, ", " division, " veces.")