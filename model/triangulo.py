<<<<<<< HEAD
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
=======
from utils.operaciones import ecDistancia

def validacionTriangulo(puntos):

    if len(puntos) != 3:
            return "invalido"
    a = ecDistancia(puntos[0], puntos[1])
    b = ecDistancia(puntos[1], puntos[2])
    c = ecDistancia(puntos[2], puntos[0])
    lados = sorted([a, b, c])
    
    if abs(lados[0]**2 + lados[1]**2 - lados[2]**2) < 0.000006: #1e-6
        return "rectangulo"
    elif lados[2]**2 < lados[0]**2 + lados[1]**2:
        return "acutangulo"
    else:
        return "otro"
    
def area(puntos):
    pass
>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632
