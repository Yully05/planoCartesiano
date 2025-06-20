class Operaciones:
    def distancia(p1,p2):
        distanciaX = p1.x-p2.x
        distanciaY = p1.y-p2.y
        return distanciaX*distanciaY + distanciaY*distanciaY  #sin usar la raiz cuadrada
    

    def vector(p1,p2):
        return ((p2.x - p1.y, p2.y - p1.y))
    
    def producto_punto(v1, v2):
        return v1[0] * v2[0] + v1[1] * v2[1]
    

def son_iguales(a, b):
        # Comparación manual con margen de tolerancia
        diferencia = a - b
        if diferencia < 0:
            diferencia = -diferencia
        return diferencia <= 0.00001
    
