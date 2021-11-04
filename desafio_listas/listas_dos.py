import functools

lista_uno = [['Mazda RX4', 21.0, 6, False, 4], ['Merc 240D', 24.4, 4, True, 2], ['Merc 280', 19.2, 6, True, 4], 
['Valiant', 18.1, 6, True, 1], ['Merc 450SL', 17.3, 8, False, 3], ['Toyota Corolla', 33.9, 4, True, 1]]

def promedio(lista):
    calculo = (functools.reduce(lambda a, b: a + b, lista ))/len(lista)
    return calculo

lista_index_uno = []
lista_index_dos = []
lista_index_cuatro = []

for auto in lista_uno:
    lista_index_uno.append(auto[1])
    lista_index_dos.append(auto[2])
    lista_index_cuatro.append(auto[4])

print(promedio(lista_index_uno))
print(promedio(lista_index_dos))
print(promedio(lista_index_cuatro))
