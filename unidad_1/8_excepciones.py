try:
#ejemplo 1 sin manejo de excepciones
 numero1=int(input("ingresa el primer numero"))
 numero2=int(input("ingresa el segundo numero"))
 resultado=numero1/numero2
 print(resultado)
except ZeroDivisionError:
 print("DIVISION ENTRE CERO FALLIDA")
except ValueError:
    print("SOLO INTRODUCE NUMEROS")