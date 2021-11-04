import sys

precio = float(sys.argv[1])
cant_usuarios = float(sys.argv[2])
gastos = float(sys.argv[3])

utilidades_ano_anterior = ''
if len(sys.argv) > 4:
    utilidades_ano_anterior = float(sys.argv[4])
else:
    utilidades_ano_anterior = 1000

print(sys.argv) 


    
    
