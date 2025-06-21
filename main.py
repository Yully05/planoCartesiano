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
listaPuntos = [lista1]

def analizarLista(lista):
    contCuadrados = 0
    cuadrados = []
    contRectangulos = 0
    rectangulos = []
    contTrianRectangulo = 0
    triangulosRectangulos = []
    contTriAcutangulo = 0
    triangulosAcutangulos = []

    combinaciones4 = combinaciones(lista, 4) #combinaciones de 4 puntos para cuadrados y rectangulos
    for puntos in combinaciones4:
        if validacionCuadrado(puntos):
            contCuadrados += 1
            cuadrados.append({"puntos": puntos})
        elif validacionRectangulo(puntos):
            contRectangulos += 1
            rectangulos.append({"puntos": puntos})

    combinaciones3 = combinaciones(lista, 3) #combinaciones de 3 puntos para triaungulos
    for puntos in combinaciones3:
        tipo = validacionTriangulo(puntos)
        if tipo == "rectangulo":
            contTrianRectangulo +=1
            triangulosRectangulos.append({"puntos": puntos})
        elif tipo == "acutangulo":
            contTriAcutangulo +=1
            triangulosAcutangulos.append({"puntos": puntos})

    print("Cuadrados:", contCuadrados, len(cuadrados))
    print("Rectangulos:", contRectangulos, len(rectangulos))
    print("Triangulos rectangulos:", contTrianRectangulo, len(triangulosRectangulos))
    print("Triangulos acutagulos:", contTriAcutangulo, len(triangulosAcutangulos))

    #return cuadrados + rectangulos + triangulosRectangulos+ triangulosAcutangulos

if __name__ == "__main__":
    print("Proyecto ADA I")


    for lista in (listaPuntos):
        analizarLista(lista)
        dibujarPuntos(lista)
        

