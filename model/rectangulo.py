<<<<<<< HEAD
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
=======
from utils.operaciones import anguloRecto

def validacionRectangulo(puntos):
    if len(puntos) != 4:
        return False

    p = puntos
    return (
        anguloRecto(p[0], p[1], p[2]) and
        anguloRecto(p[1], p[2], p[3]) and
        anguloRecto(p[2], p[3], p[0]) and
        anguloRecto(p[3], p[0], p[1])
    )
>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632
