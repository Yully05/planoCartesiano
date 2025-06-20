def son_iguales(a, b):
        # Comparación manual con margen de tolerancia
        diferencia = a - b
        if diferencia < 0:
            diferencia = -diferencia
        return diferencia <= 0.00001
    

def ecDistancia(punto1, punto2):
    dis = (((punto2.x - punto1.x)**2 + (punto2.y - punto1.y)**2)**0.5)
    return dis

def productoPunto(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def anguloRecto(p1, p2, p3):
    v1 = (p1.x - p2.x, p1.y - p2.y)
    v2 = (p3.x - p2.x, p3.y - p2.y)
    return abs(productoPunto(v1, v2)) < 0.00001 # diferencia absoluta (abs) = 1x10^-6 = 1e-6

# recursiva para calcular todas las distancias entre pares de puntos
def calcularDistancia(puntos, i=0, j=1, distancia=None):
    #i indice del primer punto / j indice del segundo punto
    # asegura de no repetir ni comparar un punto consigo mismo
    if distancia is None:
        distancia = []

    if i >= len(puntos) - 1:
        return distancia

    if j >= len(puntos):
        return calcularDistancia(puntos, i + 1, i + 2, distancia)

    distancias = ecDistancia(puntos[i], puntos[j])
    distancia.append(distancias)
    return calcularDistancia(puntos, i, j + 1, distancia)



