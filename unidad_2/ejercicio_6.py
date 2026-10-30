#creando una matriz
matriz=[
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
    ["j","k","l"],
    ["m","n","ñ"],
    ["o","p","q"],
    ["r","s","t"],
    ["u","v","w"],
    ["x","y","z"]
]
for i  in range(0,9):
    #ciclo interno para los indices de las columnas (j)
    for j in range(0,3):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")



