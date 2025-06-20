import matplotlib.pyplot as plt  # type: ignore
from utils.combinatoria import combinaciones
from model.rectangulo import validacionRectangulo
from model.cuadrado import validacionCuadrado
from model.triangulo import validacionTriangulo

def dibujarPuntos(listaPuntos):
    # Dibujar todos los puntos
    for punto in listaPuntos:
        plt.scatter(punto.x, punto.y, color='red')
        plt.text(punto.x + 0.1, punto.y + 0.1, f'({punto.x},{punto.y})')

    # Dibujar cuadrados y rectángulos
    combinaciones4 = combinaciones(listaPuntos, 4)
    for puntos in combinaciones4:
        if validacionCuadrado(puntos):
            dibujarFigura(puntos)
        elif validacionRectangulo(puntos):
            dibujarFigura(puntos)

    # Dibujar triángulos
    combinaciones3 = combinaciones(listaPuntos, 3)
    for puntos in combinaciones3:
        tipo = validacionTriangulo(puntos)
        if tipo in ("rectangulo", "acutangulo"):
            dibujarFigura(puntos)

    plt.axhline(0, color='grey')
    plt.axvline(0, color='grey')
    plt.grid(True)
    plt.axis('equal')
    plt.title("Figuras y puntos en el plano")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.show()


def dibujarFigura(puntos):
    # Unir puntos en orden y volver al punto inicial
    x = [p.x for p in puntos] + [puntos[0].x]
    y = [p.y for p in puntos] + [puntos[0].y]
    plt.plot(x, y,color='green', linewidth=2)


