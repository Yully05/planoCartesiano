from utils.operaciones import ecDistancia
from utils.ordenamiento import ordenarLista

def validacionCuadrado(puntos):
        if len(puntos) != 4: #verifica que haya 4 puntos
            return False
        
        # calcula todas las distancias entre 2 puntos. c(4,2) 6 combinaciones
        distancias = []
        for i in range(4):
            for j in range(i+1, 4):
                distancia = ecDistancia(puntos[i], puntos[j])
                distancias.append(distancia)
        
        distancias = ordenarLista(distancias) #ordena las distancias

        resultado = (distancias[0] > 0 and ## evita puntos repetidos
                    distancias[0] == distancias[1] == distancias[2] == distancias[3] and #lados iguales
                    distancias[4] == distancias[5]) #largas diagonales iguales
        #4 lados iguales y 2 diagonales iguales
        
        return resultado

def area(puntos):
    lado = ecDistancia(puntos[0], puntos[1])
    area = lado * lado
    return area
