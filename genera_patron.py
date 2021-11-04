fila = int(input("Ingresar numero de filas deseado: \n"))

for numero in range(1,fila+1):
    suma = ""
    for n in range(1,numero+1):
        suma = suma + str(n)
    print(suma)


