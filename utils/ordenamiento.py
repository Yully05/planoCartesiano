"""def ordenarBubbleSort(figuras): # ordena la lista de los diccionarios figuras. por clave area y el valor

    n = len(figuras) #cantidad figuras
    for i in range(n): #ciclo principal n veces asegura todas las comparaciones entre pares
        for j in range(0, n - i - 1): #bucle interno compara areas y realiza los intercambios
            if figuras[j]['area'] > figuras[j + 1]['area']:
                figuras[j], figuras[j + 1] = figuras[j + 1], figuras[j]
    return figuras
"""

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

