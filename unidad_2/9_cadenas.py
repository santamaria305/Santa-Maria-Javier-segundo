#cadenas y concatenacion con (+)
cadena1='hola'
cadena2="mundo"
multilinea="""Esto es una cadena 
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadenas y repeticion
eco="ja"*4
print(eco)
#cambiar una cadena de mayusculas a minusculas
tu_nombre='santa maria'
print(tu_nombre.upper())
#cambiar una cadena de mayusculas a minusculas
print(tu_nombre.lower())
#remplazar texto en una cadena
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de concatenar cadenas con valores (f-string)
edad=16
nombre='santa maria'
mensaje=f"hola,me llamo {nombre} y tengo\n{edad}años"
print(mensaje)
#contar los caracteres de una cadena
texto= "felicidades por aun continuar en el CECY!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contriene la misma palabra
oracion="aprender python es divertido"
if "java" in oracion:
    print("encontrado")
else:
    print("no esta")
#validar contenido de una cadena
ncadena="12"
print(ncadena.isalpha())
print(ncadena.isdigit())