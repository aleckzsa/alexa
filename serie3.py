nombre = input("Introduce tu primer nombre: ")
longitud = len(nombre)
print(longitud)


pn = input("Introduce tu primer nombre:")
apellido = input("Introduce tu apellido: ")
nombre = pn+ " " + apellido
longitud= len (nombre)
print (nombre)
print (longitud)


prn = input("Introduce tu primer nombre en minúsculas: ")
apellid = input("Introduce tu apellido en minúsculas: ")
prn = prn.title()
apellid = apellid.title()
nombree = prn + " " + apellid
print(nombree)


rima = input("Introduce la primer linea de una rima infantil: ")
longitud = len(rima)
print ("Esta frase tiene ", longitud, " letras.")
ni = int(input("Introduce un numero inicial."))
nf = int(input("Introduce un numero final."))
parte = (rima[ni:nf])
print(parte)


palabra = input("Introduce una palabra: ")
palabra = palabra.upper()
print (palabra)


tnombre = input("Introduce tu primer nombre: ")
if ln(tnombre)< 5:
    apellido = input("Introduce tu apellido: ")
  tnombre= tnombre+apellido
    prit(tnombre.upper())
else:
prit(tnombre.lower())


palabra = input("Por favor, introduce una palabra: ")
primera = palbra[0]
longitud = len(palabra)
resto = palabra [1: longitud]
if primera != "a" and first != "e" and first != "o" and first != "u":
    palabranueva = resto + primera + "ay"
else:
palabranueva = palabra + "way"
print(palabranueva.lower())