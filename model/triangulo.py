from utils.operaciones import Operaciones
from utils.ordenamiento import Ordenamiento

class Triangulo:

    def es_rectangulo(p):
        if len(p) != 3:
            return False
        d1 = Operaciones.distancia(p[0], p[1])
        d2 = Operaciones.distancia(p[1], p[2])
        d3 = Operaciones.distancia(p[2], p[0])
        a, b, c = Ordenamiento.ordenar3(d1, d2, d3)
        return c == a + b

    def es_acutangulo(p):
        if len(p) != 3:
            return False
        d1 = Operaciones.distancia(p[0], p[1])
        d2 = Operaciones.distancia(p[1], p[2])
        d3 = Operaciones.distancia(p[2], p[0])
        a, b, c = Ordenamiento.ordenar3(d1, d2, d3)
        return c < a + b
