from model.punto import Punto
from model.rectangulo import Rectangulo
from model.cuadrado import Cuadrado
from model.triangulo import Triangulo
from utils.combinatoria import Combinatoria
from graphics.graficos import dibujar_puntos

if __name__ == "__main__":
    print("Proyecto ADA I")

    # lista_puntos = [
    #     Punto(0, 0),
    #     Punto(2, 0),
    #     Punto(2, 2),
    #     Punto(0, 2)
    # ]

    # lista_puntos2 =[
    #     Punto()
    # ]

    # dibujar_puntos(lista_puntos)
    # print("hice cambios")

    puntos = [
        Punto(0, 0), Punto(0, 2), Punto(2, 2), Punto(2, 0)
    ]

    ##dibujar_puntos(puntos)

    # Rectángulos y cuadrados
    print("Combinaciones de 4 puntos:")
    cuadrados_detectados = []
    rectangulos_detectados = []

    for grupo in Combinatoria.combinaciones_de_4(puntos):
        if Cuadrado.es_cuadrado(grupo):
            coordenadas = [(p.x, p.y) for p in grupo]
            if coordenadas not in cuadrados_detectados:
                cuadrados_detectados.append(coordenadas)
                print("Cuadrado:", coordenadas)
        elif Rectangulo.es_rectangulo(grupo):
            coordenadas = [(p.x, p.y) for p in grupo]
            if coordenadas not in rectangulos_detectados:
                rectangulos_detectados.append(coordenadas)
                print("Rectángulo:", coordenadas)

    print("\nTotal cuadrados detectados:", len(cuadrados_detectados))
    print("Total rectángulos detectados:", len(rectangulos_detectados))


    # Triángulos
    print("\nCombinaciones de 3 puntos:")
    for grupo in Combinatoria.combinaciones_de_3(puntos):
        if Triangulo.es_rectangulo(grupo):
            print("Triángulo rectángulo:", [(p.x, p.y) for p in grupo])
        elif Triangulo.es_acutangulo(grupo):
            print("Triángulo acutángulo:", [(p.x, p.y) for p in grupo])




