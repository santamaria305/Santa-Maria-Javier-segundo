
colores=["azul","morado","rojo","amarillo","verde"]
color=input("ingresa el color:")#naranja
encontrado=False
for contador in colores: #recorre los elementos de la lista 
    print(contador)
    #si el color actual es "rojo", detener el bucle
    if contador==color:
        print("color encontrado! saliendo del bucle ")
        encontrado=True
        break 
if  not encontrado:
    print("el color ,",color,"no se encontro")