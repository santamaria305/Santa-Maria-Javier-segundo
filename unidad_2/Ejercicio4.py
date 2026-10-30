 
promedio=[10,7,6,9,7] 
#1. encontra el promedio mas bajo usando el ciclo for
#suponemos inicialmente que el promedio mas bajo es el primer elemento
promedio_bajo=promedio[0] #el cero es por que es por donde mi lista va a empezar en este caso con el  10
promedio_alto=promedio[0]
for contador in promedio:#for recorre los elemntos de una lista 
    if contador<promedio_bajo:
        promedio_bajo=contador
    if contador>promedio_alto:
        promedio_alto=contador
print(promedio_alto)
print(promedio_bajo)