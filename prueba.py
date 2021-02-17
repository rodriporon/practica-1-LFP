def busqueda_binaria_recursiva(arreglo, busqueda, izquierda, derecha):
    if izquierda > derecha:
        return -1
    indiceDelElementoDelMedio = (izquierda + derecha) // 2
    elementoDelMedio = arreglo[indiceDelElementoDelMedio]
    if elementoDelMedio == busqueda:
        return indiceDelElementoDelMedio
    if busqueda < elementoDelMedio:
        return busqueda_binaria_recursiva(arreglo, busqueda, izquierda, indiceDelElementoDelMedio - 1)
    else:
        return busqueda_binaria_recursiva(arreglo, busqueda, indiceDelElementoDelMedio + 1, derecha)

antiguo_arreglo = ['4','7','8','8']
arreglo = list(map(int, antiguo_arreglo))
print(arreglo)
print("Vamos a buscar en la siguiente lista:", arreglo)
busqueda = 8
indice = busqueda_binaria_recursiva(arreglo, busqueda, 0, len(arreglo) -1)
print("El elemento {} está en el índice {}".format(busqueda, indice))


m = [i for i, x in enumerate(arreglo) if x==busqueda]
print(m)
if m == []:
    print('Está vacía')

indices = []
for i in range(len(arreglo)):
    print(i, arreglo[i])
    if arreglo[i] == busqueda:
        indices.append(i)
        
print(indices)
