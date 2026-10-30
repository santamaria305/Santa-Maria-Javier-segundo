 #creando u diccionario en python
personas={
    "nombre":"santa maria",
    "edad": 16,
    "profesion":"ingenieria",
    "estudiante":True
}
print(personas)
#accediendo a un valor en especifico
print(personas["nombre"])
print(personas["estudiante"])
#se puede usar  en metodo .get() .(SET)
#es util por que no da error si la clave no existe
print(personas.get("edad"))
#modificar un valor existente
personas["edad"]=16
print(personas.get("edad"))
#agregar un par(clave:valor)
personas["ciudad"]="san pepe ranch"
print(personas)
#recorrer  un diccionario con un bucle
for clave,valor in personas.items():
    print(f"{clave}:{valor}")