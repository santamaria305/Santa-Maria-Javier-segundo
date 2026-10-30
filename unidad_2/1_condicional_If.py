edad=int(input("introduce tu edad:"))
if edad >= 0 and edad <= 3:
    print("aun eres bebe")
elif edad >= 4 and edad <= 11:
    print("eres un niño")
elif edad >= 12 and edad <= 18:
    print("eres un adolescente")
elif edad >= 18 and edad <= 29:
    print("eres un joven")
elif edad >= 30 and edad <= 40:
    print("eres un chavo-ruco")
elif edad >= 41 and edad <= 100:
    print("eres un adulto")
else:
    print("estas robando oxigeno")
