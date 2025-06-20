from model.punto import Punto
from model.cuadrado import validacionCuadrado
from model.rectangulo import validacionRectangulo
from model.triangulo import validacionTriangulo
from utils.combinatoria import combinaciones
from graphics.graficos import dibujarPuntos

lista1 = [Punto(0, 1), Punto(2, 0), Punto(2, 2), Punto(0, 2)]
lista2 = [Punto(3, 1), Punto(2, 2), Punto(1, 1), Punto(4, 5), Punto(2,5)]
lista3 = [Punto(0, 1), Punto(5, 1), Punto(3, 2), Punto(1, 2), Punto(3,1)]
lista4 = [Punto(1, 1), Punto(3, 4), Punto(2, 3), Punto(3, 1)]
lista5 =[Punto(0, 0), Punto(2, 0), Punto(4, 0), Punto(4, 2), Punto(2,2), Punto(0,2)]
listaPuntos = [lista2]

def analizarLista(lista):
    cuadrados = 0
    rectangulos = 0
    triangulos_r = 0
    triangulos_a = 0

    combinaciones4 = combinaciones(lista, 4) #combinaciones de 4 puntos para cuadrados y rectangulos
    for puntos in combinaciones4:
        if validacionCuadrado(puntos):
            cuadrados += 1
        elif validacionRectangulo(puntos):
            rectangulos += 1

    combinaciones3 = combinaciones(lista, 3) #combinaciones de 3 puntos para triaungulos
    for puntos in combinaciones3:
        tipo = validacionTriangulo(puntos)
        if tipo == "rectangulo":
            triangulos_r += 1
        elif tipo == "acutangulo":
            triangulos_a += 1

    print("Cuadrados:", cuadrados)
    print("Rectangulos:", rectangulos)
    print("Triangulos rectangulos:", triangulos_r)
    print("Triangulos acutagulos:", triangulos_a)

if __name__ == "__main__":
    print("Proyecto ADA I")


    for lista in (listaPuntos):
        dibujarPuntos(lista)
        analizarLista(lista)

