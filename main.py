from model.punto import Punto
#<<<<<<< HEAD
# from model.rectangulo import Rectangulo
# from model.cuadrado import Cuadrado
# from model.triangulo import Triangulo
# from utils.combinatoria import Combinatoria
# from graphics.graficos import dibujar_puntos
#=======
from model.cuadrado import validacionCuadrado
from model.rectangulo import validacionRectangulo
from model.triangulo import validacionTriangulo
from utils.combinatoria import combinaciones
from graphics.graficos import dibujarPuntos

lista1 = [Punto(0, 1), Punto(2, 0), Punto(2, 2), Punto(0, 2)]
lista2 = [Punto(3, 1), Punto(2, 2), Punto(1, 1), Punto(4, 5), Punto(2,5)]
lista3 = [Punto(0, 1), Punto(5, 1), Punto(3, 2), Punto(1, 2), Punto(3,1)]
lista4 = [Punto(1, 1), Punto(3, 4), Punto(2, 3), Punto(3, 1)]
listaPuntos = [lista3]

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
#>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632

if __name__ == "__main__":
    print("Proyecto ADA I")

#<<<<<<< HEAD
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

    # puntos = [
    #     Punto(0, 0), Punto(0, 2), Punto(2, 2), Punto(2, 0)
    # ]

    # ##dibujar_puntos(puntos)

    # # Rectángulos y cuadrados
    # print("Combinaciones de 4 puntos:")
    # cuadrados_detectados = []
    # rectangulos_detectados = []

    # for grupo in Combinatoria.combinaciones_de_4(puntos):
    #     if Cuadrado.es_cuadrado(grupo):
    #         coordenadas = [(p.x, p.y) for p in grupo]
    #         if coordenadas not in cuadrados_detectados:
    #             cuadrados_detectados.append(coordenadas)
    #             print("Cuadrado:", coordenadas)
    #     elif Rectangulo.es_rectangulo(grupo):
    #         coordenadas = [(p.x, p.y) for p in grupo]
    #         if coordenadas not in rectangulos_detectados:
    #             rectangulos_detectados.append(coordenadas)
    #             print("Rectángulo:", coordenadas)

    # print("\nTotal cuadrados detectados:", len(cuadrados_detectados))
    # print("Total rectángulos detectados:", len(rectangulos_detectados))


    # # Triángulos
    # print("\nCombinaciones de 3 puntos:")
    # for grupo in Combinatoria.combinaciones_de_3(puntos):
    #     if Triangulo.es_rectangulo(grupo):
    #         print("Triángulo rectángulo:", [(p.x, p.y) for p in grupo])
    #     elif Triangulo.es_acutangulo(grupo):
    #         print("Triángulo acutángulo:", [(p.x, p.y) for p in grupo])




#=======
    for lista in (listaPuntos):
        dibujarPuntos(lista)
        analizarLista(lista)


#>>>>>>> 9db5f56897128f2fe38e4226e8fd616d806d2632
