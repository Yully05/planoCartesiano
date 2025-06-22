def iguales(a, b):
        # comparacion manual con margen de tolerancia
        diferencia = a - b
        if diferencia < 0:
            diferencia = -diferencia
            return diferencia <= 0.00001
    

def ecDistancia(punto1, punto2):
    dis = (((punto2.x - punto1.x)**2 + (punto2.y - punto1.y)**2)**0.5)
    return dis

#producto punto entre dos vectores
def productoPunto(vector1, vector2):
    return vector1[0]*vector2[0] + vector1[1]*vector2[1]

#verifica si el angulo entre dos vectores es recto
def anguloRecto(punto1, punto2, punto3):
    vector1 = (punto1.x - punto2.x, punto1.y - punto2.y)
    vector2 = (punto3.x - punto2.x, punto3.y - punto2.y)
    return abs(productoPunto(vector1, vector2)) < 0.00001 # diferencia absoluta (abs) = 1x10^-6 = 1e-6

# recursiva para calcular todas las distancias entre pares de puntos
#i indice del primer punto / j indice del segundo punto
# asegura de no repetir ni comparar un punto consigo mismo
def calcularDistancia(puntos, i=0, j=1, distancia=None):
    
    if distancia is None:
        distancia = []

    if i >= len(puntos) - 1:
        return distancia

    if j >= len(puntos):
        return calcularDistancia(puntos, i + 1, i + 2, distancia)

    distancias = ecDistancia(puntos[i], puntos[j])
    distancia.append(distancias)
    return calcularDistancia(puntos, i, j + 1, distancia)



