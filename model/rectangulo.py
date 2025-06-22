from utils.operaciones import ecDistancia
from utils.ordenamiento import ordenarLista

def validacionRectangulo(puntos):

    if len(puntos) != 4:
        return False

    #calcula todas las distancias entre 2 puntos. c(4,2) 6 combinaciones
    distancias = []
    for i in range(4):
        for j in range(i + 1, 4):
            distancia = ecDistancia(puntos[i], puntos[j])
            distancias.append(distancia)

    distancias = ordenarLista(distancias)

    # validar si 2 lados iguales + 2 lados iguales + 2 diagonales iguales
    resultado = (
        distancias[0] > 0 and
        distancias[0] == distancias[1] and  #lados pequeños
        distancias[2] == distancias[3] and  #lados largos
        distancias[4] == distancias[5]      # diagonales
    )

    return resultado

