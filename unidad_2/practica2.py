#crear un diccionario en python
inventario={
    "lapiz": 10,
    "cuaderno" :5,
    "borrador" :8
}
producto = input("producto :")
cantidad = int(input("cantidad : "))
if producto in inventario:
    if cantidad <= inventario[producto]:
       print("AUTORIZA")
       inventario[producto] -= cantidad
    else:
       print("rechaza menos por que  no hay tanto")
else:
       print("rechaza no existe")

print(inventario)