import string

def gen(numero):
    abecedario = string.ascii_lowercase
    contar = 0
    acumulador = ""
    for letra in abecedario:
        acumulador += letra
        contar += 1
        if contar == numero:
            break
    print(acumulador)


def letra_o(number):
    if number % 2 == 0:
        number +=1
    for fila in range(number):
        if number == 1:
            print("*")
        elif fila%(number-1) ==  0:
            print("*"*number)
        else:
            print("*"+" "*(number-2)+"*")


def letra_i(number):
    if number % 2 == 0:
        number +=1
    for fila in range(number):
        if number == 1:
            print("Debe ser un numero mayor que uno")
        elif fila%(number-1) ==  0:
            print("*"*number)
        else:
            print(" "*int(number/2)+"*"+" "*int(number/2))




def letra_x(number):

    if number % 2 == 0:
        number +=1
    
    for fila in range(number):
        for columna in range(number):
            if fila == columna or (fila+columna)==(number-1):
                print("*", end='')
            else:
                print(' ', end='')
        print()



