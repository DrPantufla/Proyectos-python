num_parrafos = int(input("Ingrese el numero de parrafos requerido: \n"))
lorem = '''     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce diam ipsum, 
ultricies ut lorem vel, sollicitudin iaculis sapien. Suspendisse pellentesque at tellus id 
viverra. Suspendisse porta et magna ac interdum. Suspendisse potenti. Orci varius natoque 
penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque ultrices augue 
massa, id dictum odio blandit a. Pellentesque ligula mauris, vestibulum vel iaculis sed, lobortis 
sed risus. Aliquam blandit magna eget ipsum fermentum tempor. Cras ut ultrices libero, nec porta 
neque. Curabitur ornare tellus in dui blandit, vel tristique odio fermentum. Pellentesque 
scelerisque aliquet mattis. Pellentesque quis ultrices ex.?\n'''

for parrafo in range(num_parrafos):
    print(lorem)
