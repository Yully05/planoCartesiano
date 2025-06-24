from utils.operaciones import ecDistancia, anguloRecto
from utils.ordenamiento import ordenarLista

def validacionRectangulo(puntos):
    if len(puntos) != 4:
        return False

    #confirmar que los 4 angulos sean rectos
    esRecto1 = anguloRecto(puntos[0], puntos[1], puntos[2])
    esRecto2 = anguloRecto(puntos[1], puntos[2], puntos[3])
    esRecto3 = anguloRecto(puntos[2], puntos[3], puntos[0])
    esRecto4 = anguloRecto(puntos[3], puntos[0], puntos[1])

    if not (esRecto1 and esRecto2 and esRecto3 and esRecto4):
        return False  #No todos los ángulos son rectos

    #Verificar que existan dos lados iguales y otros dos lados iguales
    lados = [
        ecDistancia(puntos[0], puntos[1]),
        ecDistancia(puntos[1], puntos[2]),
        ecDistancia(puntos[2], puntos[3]),
        ecDistancia(puntos[3], puntos[0]),
    ]
    lados = ordenarLista(lados)

    #Validar 2 pares de lados iguales
    if lados[0] > 0 and lados[0] == lados[1] and lados[2] == lados[3] and lados[0] != lados[2]:
        return True

    return False


