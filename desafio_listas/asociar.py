import functools

def promedio(lista):
    calculo = (functools.reduce(lambda a, b: a + b, lista ))/len(lista)
    return calculo

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
 11, 11, 12, 12, 12, 12, 13, 13,
 13, 13, 14, 14, 14, 14, 15, 15,
 15, 16, 16, 17, 17, 17, 18, 18,
 18, 18, 19, 19, 19, 20, 20, 20,
 20, 20, 22, 23, 24, 24, 24, 24, 25]

distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
 17, 28, 14, 20, 24, 28, 26, 34, 34,
 46, 26, 36, 60, 80, 20, 26, 54, 32,
 40, 32, 40, 50, 42, 56, 76, 84, 36,
 46, 68, 32, 48, 52, 56, 64, 66, 54,
 70, 92, 93, 120, 85]

promedio_velocidad = promedio(velocidad)
promedio_distancia = promedio(distancia)

juntar_listas = list(zip(velocidad, distancia))

contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0

for x,y in juntar_listas:
    if x<promedio_velocidad:
        contador_1 += 1
    if x<promedio_velocidad and y>promedio_distancia:
        contador_2 += 1
    if x>promedio_velocidad:
        contador_3 += 1
    if x>promedio_velocidad and y<promedio_distancia:
        contador_4 += 1
print(f"Velocidad bajo el promedio ocurre {contador_1} veces.")
print(f"Velocidad bajo el promedio y distancia sobre el promedio ocurre {contador_2} veces.")
print(f"Velocidad sobre el promedio ocurre {contador_3} veces")
print(f"Velocidad sobre el promedio y distancia bajo el promedio ocurre {contador_4} veces")


