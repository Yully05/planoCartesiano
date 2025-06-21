import matplotlib.pyplot as plt  # type: ignore
from utils.combinatoria import combinaciones
from model.rectangulo import validacionRectangulo
from model.cuadrado import validacionCuadrado
from model.triangulo import validacionTriangulo

def dibujarPuntos(listaPuntos):
    # Dibujar todos los puntos sin unirlos en en el plano
    for punto in listaPuntos:
        dibujarPunto(punto)
    dibujarPlano()   

    #dibujar rectangulos y cuadrados unidos por las lineas en el plano
    # combinaciones4 = combinaciones(listaPuntos, 4)
    # for puntos in combinaciones4:
    #     if validacionCuadrado(puntos):
    #         dibujarFigura(puntos)
    #     elif validacionRectangulo(puntos):
    #         dibujarFigura(puntos)

    # Dibujar triángulos
    # combinaciones3 = combinaciones(listaPuntos, 3)
    # for puntos in combinaciones3:
    #     tipo = validacionTriangulo(puntos)
    #     if tipo in ("rectangulo", "acutangulo"):
    #         dibujarFigura(puntos)
    # dibujarPlano() 
def cuadrados(listaPuntos):
    combinaciones4 = combinaciones(listaPuntos, 4)
    for puntos in combinaciones4:
        if validacionCuadrado(puntos):
            dibujarFigura(puntos)
    dibujarPlano()

def rectangulos(listaPuntos):
    combinaciones4 = combinaciones(listaPuntos, 4)
    for puntos in combinaciones4:
        if validacionRectangulo(puntos):
            dibujarFigura(puntos)
    dibujarPlano()

def CuadradosYRectangulos(listaPuntos):
    combinaciones4 = combinaciones(listaPuntos, 4)
    for puntos in combinaciones4:
        if validacionCuadrado(puntos):
            dibujarFigura(puntos)
        elif validacionRectangulo(puntos):
            dibujarFigura(puntos)
    dibujarPlano()

# def cuadradosyRect(listaPuntos):
#     dibujarFigura(listaPuntos)
#     combinaciones4 = combinaciones(listaPuntos, 4)
#     for puntos in combinaciones4:
#         if validacionCuadrado(puntos):
#             dibujarFigura(puntos)
#         elif validacionRectangulo(puntos):
#             dibujarFigura(puntos)
#     dibujarPlano()

def triangulos(listaPuntos):
    combinaciones3 = combinaciones(listaPuntos, 3)
    for puntos in combinaciones3:
        tipo = validacionTriangulo(puntos)
        if tipo in ("rectangulo", "acutangulo"):
            dibujarFigura(puntos)
    dibujarPlano()

def dibujarPunto(punto):
    plt.scatter(punto.x, punto.y, color='red')
    plt.text(punto.x + 0.1, punto.y + 0.1, f'({punto.x},{punto.y})')  

def dibujarPlano():
    plt.axhline(-1,color='gray')
    plt.axvline(-1,color='gray')
    plt.grid(True)
    plt.axis('equal')
    plt.title("Figuras y puntos en el plano")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.show()

def dibujarFigura(puntos):
    # Unir puntos en orden y volver al punto inicial
    for punto in puntos:
        dibujarPunto(punto)
    x = [p.x for p in puntos] + [puntos[0].x]
    y = [p.y for p in puntos] + [puntos[0].y]
    plt.plot(x, y,color='green', linewidth=2)
    
    

