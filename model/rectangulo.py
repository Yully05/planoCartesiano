
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

