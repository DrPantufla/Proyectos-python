import string
contrasena = input("Ingrese contraseña: \n").lower()
abecedario = string.ascii_lowercase
intentos = 0
for letra in contrasena:
    for letra_en_abecedario in abecedario:
        intentos += 1
        if letra == letra_en_abecedario:
            break
print("{} intentos".format(intentos))

    
    