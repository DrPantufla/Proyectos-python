import sys
precio_venta = float(sys.argv[1])
usuarios = int(sys.argv[2])
gastos = float(sys.argv[3])

utilidades = precio_venta * usuarios - gastos

print('Las utilidades son {}'.format(utilidades))
