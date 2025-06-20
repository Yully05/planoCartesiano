<<<<<<< HEAD
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

=======
from utils.operaciones import ecDistancia

def validacionCuadrado(puntos):
        if len(puntos) != 4:
            return False
        d = [ecDistancia(puntos[i], puntos[j]) for i in range(4) for j in range(i+1, 4)]
        d.sort()
        return d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5]  # 4 lados iguales y 2 diagonales iguales

def area(puntos):
    lado = ecDistancia(puntos[0], puntos[1])
    return lado * lado
>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632
