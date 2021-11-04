import sys
#entrada de datos
valor_estandar=float(sys.argv[1])
cant_usuarios_normales=float(sys.argv[2])
cant_usuarios_premiun = float(sys.argv[3])
cant_usuarios_en_periodo_de_prueba= float(sys.argv[4])
gastos = float(sys.argv[5])
#operaciones
ganancias_usuarios_estandar = valor_estandar*cant_usuarios_normales
ganancias_usuarios_premiun = 2*valor_estandar*cant_usuarios_premiun
ganancias = ganancias_usuarios_estandar + ganancias_usuarios_premiun

utilidades = ganancias - gastos 

print('Las utilidades son {}'.format(utilidades))