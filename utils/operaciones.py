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

#metodos para el calculo de las areas de cada figura
def areaCuadrado(puntos):
    lado = ecDistancia(puntos[0], puntos[1])
    area = lado * lado
    return area

def areaRectangulo(puntos):
    lado1 = ecDistancia(puntos[0], puntos[1])
    lado2 = ecDistancia(puntos[1],puntos[2])
    area = lado1*lado2
    return area

def areaTriangulo(puntos):  #formula de heron para calcular el area de cualquier triangulos conociendo solo las distancias
    a = ecDistancia(puntos[0], puntos[1])
    b = ecDistancia(puntos[1], puntos[2])
    c = ecDistancia(puntos[2], puntos[0])
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area