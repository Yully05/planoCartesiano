import matplotlib.pyplot as plt
from utils.combinatoria import combinaciones
from model.rectangulo import validacionRectangulo
from model.cuadrado import validacionCuadrado
from model.triangulo import validacionTriangulo

def dibujarPuntos(listaPuntos): # graficar todos los puntos en el plano
    plt.figure() #nueva ventana para graficar
    for punto in listaPuntos:
        dibujarPunto(punto)

    dibujarPlano()
    plt.title("Puntos en el plano")
    plt.show()


def dibujarCuadrados(listaPuntos):
    plt.figure()
    combinacionesCuadrado = combinaciones(listaPuntos, 4)
    for puntos in combinacionesCuadrado:
        if validacionCuadrado(puntos):
            dibujarFigura(puntos)
    dibujarPlano()
    plt.title("Cuadrados en el plano")
    plt.show()


def dibujarRectangulos(listaPuntos):
    plt.figure() #crea una nueva figura
    combinacionesRectangulo = combinaciones(listaPuntos, 4)
    for puntos in combinacionesRectangulo:
        if validacionRectangulo(puntos):
            dibujarFigura(puntos)
    dibujarPlano()
    plt.title("Rectangulos en el plano")
    plt.show()


def dibujarTriangulosRectangulos(listaPuntos):
    plt.figure()
    combinacionesTriangulo = combinaciones(listaPuntos, 3)
    for puntos in combinacionesTriangulo:
        tipo = validacionTriangulo(puntos)
        if tipo in ("rectangulo"):
            dibujarFigura(puntos)
    dibujarPlano()
    plt.title("Triangulos rectangulos en el plano")
    plt.show()


def dibujarTriangulosAcutangulos(listaPuntos):
    plt.figure()
    combinacionesTriangulo = combinaciones(listaPuntos, 3)
    for puntos in combinacionesTriangulo:
        tipo = validacionTriangulo(puntos)
        if tipo in ("acutangulo"):
            dibujarFigura(puntos)
    dibujarPlano()
    plt.title("Triangulos acutangulos en el plano")
    plt.show()


def dibujarPunto(punto): #grafica unicamente los puntos necesarios
    plt.scatter(punto.x, punto.y, color='red')
    plt.text(punto.x + 0.1, punto.y + 0.1, f'({punto.x},{punto.y})')


def dibujarPlano():
    plt.axhline(-1,color='gray')
    plt.axvline(0-1,color='gray')
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")


def dibujarFigura(puntos):
    if len(puntos) < 3:
        print("No hay suficientes puntos para formar una figura")
        return
    
    # unir puntos en orden y volver al punto inicial
    for punto in puntos:
        dibujarPunto(punto)
    x = [p.x for p in puntos] + [puntos[0].x]
    y = [p.y for p in puntos] + [puntos[0].y]
    plt.plot(x, y,color='green', linewidth=2)
    plt.title("Figuras en el plano")
