carrito=[]#se deja la lista vacia
cantidad=int(input("¿cuantosproductos quieres agrgar al carrito"))# el usuario nos dira cuantos productios
for contador in range(cantidad):#el contador siempre ira pues nos ayuda a contar
    producto=input(f"ingresa el productucto{contador+1}")
    carrito.append(producto)
print("\n tu lista de compra es:")
print(carrito)