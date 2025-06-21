
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
#>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632
