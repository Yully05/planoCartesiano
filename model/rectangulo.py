from utils.operaciones import Operaciones
from utils.ordenamiento import Ordenamiento

class Rectangulo:

    def es_rectangulo(puntos):
        if len(puntos) != 4:
            return False
        
        puntos_ordenados = Ordenamiento.ordenar_por_sentido_horario(puntos)
        A, B, C, D = puntos[0], puntos[1], puntos[2], puntos[3]
        v1 = Operaciones.vector(A, B)
        v2 = Operaciones.vector(B, C)
        v3 = Operaciones.vector(C, D)
        v4 = Operaciones.vector(D, A)

        angulos = 0
        if Operaciones.producto_punto(v1, v2) == 0:
            angulos += 1
        if Operaciones.producto_punto(v2, v3) == 0:
            angulos += 1
        if Operaciones.producto_punto(v3, v4) == 0:
            angulos += 1
        if Operaciones.producto_punto(v4, v1) == 0:
            angulos += 1

        return angulos == 4
