mapa=[
    [".",".",".","."],
    [".",".",".","."],
    [".","a",".","b"],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#recorriendo la matriz con ciclos anidados
#ciclo externo para manejar filas(i)
for i in range(filas):
    #ciclo interno para manejar columnas (j)
    for j in range(columnas):
        #verificamos si encontramos el tesoro
        if mapa[i][j]=="a":
            print(f"tesosro encontrado en la posicion [{i}][{j}]")
        if mapa[i][j]=="b":
            print(f"tesosro encontrado en la posicion [{i}][{j}]")

