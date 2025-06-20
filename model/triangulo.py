
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
