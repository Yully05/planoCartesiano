from utils.operaciones import ecDistancia
from utils.ordenamiento import ordenarLista

def validacionTriangulo(puntos):

    if len(puntos) != 3:
        return "invalido"
    
    #distancias por cada lado
    a = ecDistancia(puntos[0], puntos[1])
    b = ecDistancia(puntos[1], puntos[2])
    c = ecDistancia(puntos[2], puntos[0])

    lados = ordenarLista([a,b,c]) #para tomar lado c mas largo como hipotenusa

    #si cumple terorema de  pitagoras a2 + b2 = c2
    pitagoras = abs(lados[0]**2 + lados[1]**2 - lados[2]**2)
    if pitagoras < 0.000006: #1e-6 tolerancia para errores por decimales float. diferencia absoluta abs
        return "rectangulo"
    
    #si a2 + b2 > c2
    elif lados[0]**2 + lados[1]**2 > lados[2]**2:
        return "acutangulo"
    else:
        return "no es rectangulos ni acutangulo"
    
def area(puntos):
    pass
