from model.punto import Punto
from graphics.graficos import dibujar_puntos

if __name__ == "__main__":
    print("Proyecto ADA I")

    lista_puntos = [
        Punto(0, 0),
        Punto(2, 0),
        Punto(2, 2),
        Punto(0, 2)
    ]

    dibujar_puntos(lista_puntos)
    print("hice cambios")
