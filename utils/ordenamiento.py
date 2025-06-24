def ordenarLista(lista): #menor a mayaor

    listaOrdenada = []

    while lista:
        menor = lista[0]
        for dato in lista:
            if dato < menor:
                menor = dato
        listaOrdenada.append(menor)
        lista.remove(menor)

    # copiar los valores ordenados a la lista original
    for i in range(len(listaOrdenada)):
        lista.append(listaOrdenada[i])

    return lista

