from model.rectangulo import Rectangulo
from utils.operaciones import Operaciones
from utils.ordenamiento import Ordenamiento

class Cuadrado:

    
    def es_cuadrado(puntos):
        if len(puntos) != 4:
            return False

        puntos_ordenados = Ordenamiento.ordenar_por_sentido_horario(puntos)

        if not Rectangulo.es_rectangulo(puntos_ordenados):
            return False

        d1 = Operaciones.distancia(puntos_ordenados[0], puntos_ordenados[1])
        d2 = Operaciones.distancia(puntos_ordenados[1], puntos_ordenados[2])
        d3 = Operaciones.distancia(puntos_ordenados[2], puntos_ordenados[3])
        d4 = Operaciones.distancia(puntos_ordenados[3], puntos_ordenados[0])

        return (
            Operaciones.son_iguales(d1, d2)
            and Operaciones.son_iguales(d2, d3)
            and Operaciones.son_iguales(d3, d4)
        )

