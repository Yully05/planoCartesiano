from model.punto import Punto
from model.cuadrado import validacionCuadrado
from model.rectangulo import validacionRectangulo
from model.triangulo import validacionTriangulo
from utils.combinatoria import combinaciones
from graphics.graficos import dibujarPuntos
from graphics.figuras import menu
from utils.areas import areaFiguras

lista1 = [Punto(0, 1), Punto(2, 0), Punto(2, 2), Punto(0, 2)]
lista2 = [Punto(3, 1), Punto(1, 2), Punto(1, 1), Punto(4, 5), Punto(2,5)]
lista3 = [Punto(1, 1), Punto(2, 1), Punto(2, 2), Punto(1, 2), Punto(3,1)] #cuadrado
lista4 = [Punto(1, 1), Punto(1, 3), Punto(2, 3), Punto(2, 1)] #rectangulo
lista5 = [Punto(0, 0), Punto(2, 0), Punto(2, 2), Punto(0, 2)] #cuadrado
lista6 = [Punto(1, 0), Punto(1,2)]
listaPuntos = [lista2]

def analizarLista(lista):
    contCuadrados = 0
    contRectangulos = 0
    contTrianRectangulo = 0
    contTriAcutangulo = 0

    # diccionario para almacenar figuras key tipo
    figuras = {
    "cuadrado": [],
    "rectangulo": [],
    "triangulo rectangulo": [],
    "triangulo acutangulo": []
    }

    combinacionesCuadrados = combinaciones(lista, 4) #combinaciones de 4 puntos para cuadrados y rectangulos
    for puntos in combinacionesCuadrados:
        if validacionCuadrado(puntos):
            contCuadrados += 1
            figuras["cuadrado"].append({"nombre": "cuadrado", "puntos": puntos})
        elif validacionRectangulo(puntos):
            contRectangulos += 1
            figuras["rectangulo"].append({"nombre": "rectangulo", "puntos": puntos})

    combinacionesTriangulos = combinaciones(lista, 3) #combinaciones de 3 puntos para triaungulos
    for puntos in combinacionesTriangulos:
        tipo = validacionTriangulo(puntos)
        if tipo == "rectangulo":
            contTrianRectangulo +=1
            figuras["triangulo rectangulo"].append({"nombre": "triangulo rectangulo", "puntos": puntos})
        elif tipo == "acutangulo":
            contTriAcutangulo +=1
            figuras["triangulo acutangulo"].append({"nombre": "triangulo acutangulo", "puntos": puntos})

    print("Los puntos de la lista generan:\n")
    print("     Cuadrados:", contCuadrados)
    print("     Rectangulos:", contRectangulos)
    print("     Triangulos rectangulos:", contTrianRectangulo)
    print("     Triangulos acutagulos:", contTriAcutangulo)

if __name__ == "__main__":
    print("\nProyecto ADA I\n")

    for lista in (listaPuntos):
        analizarLista(lista)

        if len(lista) < 3:
            print("\nNo es posible formar ninguna figura")
        else:
            areaFiguras([lista])
            dibujarPuntos(lista)
            menu(lista)

