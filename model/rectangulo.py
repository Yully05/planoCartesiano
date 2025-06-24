# from utils.operaciones import ecDistancia
# from utils.ordenamiento import ordenarLista

# def validacionRectangulo(puntos):

#     if len(puntos) != 4:
#         return False

#     #calcula todas las distancias entre 2 puntos. c(4,2) 6 combinaciones
#     distancias = []
#     for i in range(4):
#         for j in range(i + 1, 4):
#             distancia = ecDistancia(puntos[i], puntos[j])
#             distancias.append(distancia)

#     distancias = ordenarLista(distancias)

#     # validar si 2 lados iguales + 2 lados iguales + 2 diagonales iguales
#     resultado = (
#         distancias[0] > 0 and
#         distancias[0] == distancias[1] and  #lados pequeños
#         distancias[2] == distancias[3] and  #lados largos
#         distancias[4] == distancias[5]      # diagonales
#     )
#     return resultado
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


