from utils.combinatoria import combinaciones
from model.cuadrado import validacionCuadrado
from model.rectangulo import validacionRectangulo
from model.triangulo import validacionTriangulo
from utils.operaciones import areaTriangulo
from utils.operaciones import areaRectangulo
from utils.operaciones import areaCuadrado

def figura(tipo, puntos, area):
    return {
        "tipo": tipo,
        "puntos": puntos,
        "area": area
    }

def areaFiguras(listaPuntos): #se crea el metodo con la lista que guarda el area de las figuradas creadas
    figuras = []
    identificador = 1 #cuentas las areas encontradas

    for puntos in listaPuntos:
        combinaciones3 = combinaciones(puntos, 3)
        combinaciones4 = combinaciones(puntos, 4)

        for i in combinaciones3:
            tipo = validacionTriangulo(i) #sacar el area de cada triangulo segun corresponda
            if tipo != "invalido":
                if tipo== "rectangulo" or tipo=="acutangulo": #se validad que no tome figuras diferentes a los triangulos
                    area = areaTriangulo(i)
                    figuras.append(figura(f"#{identificador} Triangulo {tipo} ",i,area))
                    identificador += 1
        
        for i in combinaciones4: #sacar el area de cada cuadrado o rectangulo segun corresponda
            if validacionCuadrado(i):
                area = areaCuadrado(i)
                figuras.append(figura(f"#{identificador} Cuadrado ",i,area))
                identificador += 1
            elif validacionRectangulo(i):
                area = areaRectangulo(i)
                figuras.append(figura(f"#{identificador} Rectangulo ",i,area))
                identificador += 1

    #imprimir los resultados de las areas identificadas
    for f in figuras:
        print("\nNombre:", f["tipo"])
        print("Área:", f["area"])
        print("Puntos:", [(p.x, p.y) for p in f["puntos"]])
        print("-------------------------------")
        